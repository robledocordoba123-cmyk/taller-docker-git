-- Migración inicial: crea la tabla usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Datos de ejemplo (opcional, útil para probar GET al iniciar)
INSERT INTO usuarios (nombre, email) VALUES
    ('Admin SENA', 'admin@sena.edu.co')
ON CONFLICT (email) DO NOTHING;