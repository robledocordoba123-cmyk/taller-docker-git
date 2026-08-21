CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

INSERT INTO usuarios (nombre, email) VALUES
    ('Ana Torres', 'ana@sena.edu.co'),
    ('Luis Gomez', 'luis@sena.edu.co')
ON CONFLICT (email) DO NOTHING;
