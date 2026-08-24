from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import redis
import psycopg2
import os
import json

app = FastAPI(title="API Ejercicio - Redis + PostgreSQL")

redis_client = redis.Redis(
    host=os.environ.get("REDIS_HOST", "redis"),
    port=int(os.environ.get("REDIS_PORT", 6379)),
    decode_responses=True
)

def get_db_connection():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        port=os.environ.get("DB_PORT", 5432),
        user=os.environ.get("DB_USER", "postgres"),
        password=os.environ.get("DB_PASSWORD", "postgres"),
        dbname=os.environ.get("DB_NAME", "cachedb")
    )

def check_rate_limit(ip: str):
    key = f"rate_limit:{ip}"
    current = redis_client.get(key)
    if current is None:
        redis_client.setex(key, 60, 1)
        return True
    if int(current) >= 10:
        return False
    redis_client.incr(key)
    return True

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    ip = request.client.host
    if not check_rate_limit(ip):
        return JSONResponse(status_code=429, content={"detail": "Demasiadas solicitudes, intenta en un minuto"})
    response = await call_next(request)
    return response

@app.get("/")
def index():
    return {"servicio": "API con FastAPI + Redis + PostgreSQL", "status": "activo"}

@app.get("/contador")
def contador():
    valor = redis_client.incr("contador_visitas")
    return {"contador_visitas": valor}

@app.get("/usuarios/{usuario_id}")
def obtener_usuario(usuario_id: int):
    cache_key = f"usuario:{usuario_id}"
    cache = redis_client.get(cache_key)
    if cache:
        return {"origen": "cache", "usuario": json.loads(cache)}

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, nombre, email FROM usuarios WHERE id = %s", (usuario_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    usuario = {"id": row[0], "nombre": row[1], "email": row[2]}
    redis_client.setex(cache_key, 60, json.dumps(usuario))
    return {"origen": "base_de_datos", "usuario": usuario}

@app.get("/cache/estadisticas")
def estadisticas_cache():
    info = redis_client.info()
    return {
        "keys_totales": redis_client.dbsize(),
        "memoria_usada": info.get("used_memory_human"),
        "hits": info.get("keyspace_hits"),
        "misses": info.get("keyspace_misses")
    }
