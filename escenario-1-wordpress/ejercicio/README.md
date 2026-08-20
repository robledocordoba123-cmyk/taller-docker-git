# Escenario 1 - Ejercicio: WordPress + MariaDB + phpMyAdmin

Variante del ejemplo guiado, con MariaDB en vez de MySQL, phpMyAdmin
como servicio adicional, y todas las credenciales manejadas por
variables de entorno.

## Cambios respecto al ejemplo

- MariaDB 10.11 en lugar de MySQL 8.0.
- phpMyAdmin agregado en el puerto 8081.
- Variables de entorno (.env) en lugar de contraseñas escritas directamente.
- Volumen personalizado: mi_wordpress_data.
- Red personalizada: mi_red_wordpress.

## Cómo levantarlo

1. Copiar la plantilla: `cp .env.example .env`
2. Completar `.env` con tus propias contraseñas.
3. `docker-compose up -d`
4. Acceder:
   - WordPress: http://localhost:8080
   - phpMyAdmin: http://localhost:8081

## Comandos útiles

- `docker-compose logs -f` — ver logs en tiempo real
- `docker-compose down` — detener
- `docker-compose down -v` — detener y borrar datos