from fastapi import FastAPI

app = FastAPI(title="App CICD Ejercicio")

@app.get("/")
def index():
    return {"mensaje": "Hola desde CI/CD con tests y multi-stage", "version": "1.0.0"}

@app.get("/health")
def health():
    return {"status": "healthy"}
