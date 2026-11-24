USE portfolio;

INSERT INTO usuarios (db_nombre_usuario, db_email, db_nombre, db_apellido, db_password_hash, db_fecha_creacion) VALUES
('usuario1', 'usuario1@example.com', 'Usuario', 'Uno', 'password1', NOW()),
('usuario2', 'usuario2@example.com', 'Usuario', 'Dos', 'password2', NOW()),
('usuario3', 'usuario3@example.com', 'Usuario', 'Tres', 'password3', NOW());

INSERT INTO categoria_proyecto (db_nombre_categoria) VALUES
('Desarrollo Web'),
('Aplicaciones Móviles'),
('Aplicaciones de Escritorio'),
('Ciencia de Datos'),
('Videojuegos'),
('Inteligencia Artificial');

INSERT INTO proyectos (db_id_usuario, db_nombre_proyecto, db_descripcion, db_etapa, db_fecha_creacion, db_fecha_actualizacion, db_fecha_finalizacion, db_fecha_limite, db_id_categoria_proyecto) VALUES
(1, 'Proyecto Web 1', 'Descripción del Proyecto Web 1', 'En Progreso', NOW(), NOW(), NULL, NULL, 1),
(2, 'Proyecto Móvil 1', 'Descripción del Proyecto Móvil 1', 'En Progreso', NOW(), NOW(), NULL, NULL, 2),
(3, 'Proyecto de Ciencia de Datos 1', 'Descripción del Proyecto de Ciencia de Datos 1', 'En Progreso', NOW(), NOW(), NULL, NULL, 4);

INSERT INTO habilidades_lenguaje (db_id_usuario, db_lenguaje, db_nivel) VALUES
(1, 'Python', 'Avanzado'),
(1, 'JavaScript', 'Intermedio'),
(2, 'Java', 'Avanzado'),
(2, 'Kotlin', 'Intermedio'),
(3, 'R', 'Avanzado'),
(3, 'SQL', 'Intermedio');

INSERT INTO habilidades_tecnologia (db_id_usuario, db_tecnologia, db_nivel) VALUES
(1, 'React', 'Avanzado'),
(1, 'Node.js', 'Intermedio'),
(2, 'Android Studio', 'Avanzado'),
(2, '.Net Framework', 'Intermedio'),
(3, 'Git', 'Avanzado'),
(3, 'Pandas', 'Intermedio');

INSERT INTO links_proyecto (db_id_proyecto, db_tipo, db_url) VALUES
(1, 'Repositorio', 'https://github.com/usuario1/proyecto1'),
(2, 'Repositorio', 'https://github.com/usuario2/proyecto2'),
(3, 'Repositorio', 'https://github.com/usuario3/proyecto3');

INSERT INTO proyecto_lenguaje (db_id_proyecto, db_id_lenguaje) VALUES
(1, 1), -- Proyecto Web 1 usa Python
(1, 2), -- Proyecto Web 1 usa JavaScript
(2, 3), -- Proyecto Móvil 1 usa Java
(2, 4), -- Proyecto Móvil 1 usa Kotlin
(3, 5), -- Proyecto de Ciencia de Datos 1 usa R
(3, 6); -- Proyecto de Ciencia de Datos 1 usa SQL

INSERT INTO proyecto_tecnologia (db_id_proyecto, db_id_tecnologia) VALUES
(1, 1), -- Proyecto Web 1 usa React
(1, 2), -- Proyecto Web 1 usa Node.js
(2, 3), -- Proyecto Móvil 1 usa Android Studio
(2, 4), -- Proyecto Móvil 1 usa .Net Framework
(3, 5), -- Proyecto de Ciencia de Datos 1 usa Git
(3, 6); -- Proyecto de Ciencia de Datos 1 usa Pandas