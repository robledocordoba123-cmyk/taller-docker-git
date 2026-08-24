# App CI/CD - Ejercicio

API en FastAPI con pipeline de CI/CD usando GitHub Actions.

## Pipeline
1. Ejecuta tests con pytest
2. Si pasan, construye la imagen Docker (multi-stage build)
3. Publica en DockerHub y GitHub Container Registry (GHCR)
4. Escanea vulnerabilidades con Trivy

## Correr localmente
docker build -t app-cicd-ejercicio .
docker run -p 8000:8000 app-cicd-ejercicio
curl http://localhost:8000/health

![CI/CD](https://github.com/robledocordoba123-cmyk/taller-docker-git/actions/workflows/ci-cd-ejercicio.yml/badge.svg)
