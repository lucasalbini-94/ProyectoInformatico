<<<<<<< HEAD
=======
# TERCERA VERSIÓN
# Revise detalles de sintaxis y emprolije los comentarios

>>>>>>> 7d94a73f6235690a169fcdad73044fef080f90df
CREATE DATABASE IF NOT EXISTS portfolio;
USE portfolio;

# Datos básicos del usuario.
# nombre_usuario y email NO pueden repetirse (UNIQUE).
# fecha_creacion: pendiente de revisar si aporta valor; se deja para dar información den el portoflio de hacer cuento es usuario

CREATE TABLE usuarios (
    id              INT AUTO_INCREMENT,
<<<<<<< HEAD
    nombre_usuario  VARCHAR(50)  NOT NULL UNIQUE,
    email           VARCHAR(255) NOT NULL UNIQUE,
    nombre          VARCHAR(100) NOT NULL,
    apellido        VARCHAR(100) NOT NULL,
    password_hash   VARCHAR(255) NOT NULL,
    fecha_creacion  DATETIME DEFAULT CURRENT_TIMESTAMP,
=======
    db_nombre_usuario  VARCHAR(50)  NOT NULL UNIQUE,
    db_email           VARCHAR(255) NOT NULL UNIQUE,
    db_nombre          VARCHAR(100) NOT NULL,
    db_apellido        VARCHAR(100) NOT NULL,
    db_password_hash   VARCHAR(255) NOT NULL,
    db_fecha_creacion  DATETIME DEFAULT CURRENT_TIMESTAMP,
>>>>>>> 7d94a73f6235690a169fcdad73044fef080f90df
    PRIMARY KEY (id)
);

CREATE TABLE categoria_proyecto (
<<<<<<< HEAD
    id_categoria      INT AUTO_INCREMENT,
    nombre_categoria  VARCHAR(50) NOT NULL UNIQUE,
    PRIMARY KEY (id_categoria)
=======
    id      INT AUTO_INCREMENT,
    db_nombre_categoria  VARCHAR(50) NOT NULL UNIQUE,
    PRIMARY KEY (id)
>>>>>>> 7d94a73f6235690a169fcdad73044fef080f90df
);

CREATE TABLE proyectos (
    id                    INT AUTO_INCREMENT,
<<<<<<< HEAD
    id_usuario            INT NOT NULL,
    nombre_proyecto       VARCHAR(100) NOT NULL,
    descripcion           VARCHAR(500) NOT NULL,
    etapa                 VARCHAR(50)  NOT NULL,
    fecha_creacion        DATETIME DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion   DATETIME,
    fecha_finalizacion    DATETIME,
    fecha_limite          DATETIME,
    id_categoria_proyecto INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id_usuario)            REFERENCES usuarios(id),
    FOREIGN KEY (id_categoria_proyecto) REFERENCES categoria_proyecto(id_categoria)
=======
    db_id_usuario            INT NOT NULL,
    db_nombre_proyecto       VARCHAR(100) NOT NULL,
    db_descripcion           VARCHAR(500) NOT NULL,
    db_etapa                 VARCHAR(50)  NOT NULL,
    db_fecha_creacion        DATETIME DEFAULT CURRENT_TIMESTAMP,
    db_fecha_actualizacion   DATETIME,
    db_fecha_finalizacion    DATETIME,
    db_fecha_limite          DATETIME,
    db_id_categoria_proyecto INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (db_id_usuario)            REFERENCES usuarios(id),
    FOREIGN KEY (db_id_categoria_proyecto) REFERENCES categoria_proyecto(id)
>>>>>>> 7d94a73f6235690a169fcdad73044fef080f90df
);

# Catálogo de lenguajes. Se llama una sola vez a la api. Todavia no sabemos cada cuanto o en 
# que moemento
CREATE TABLE lenguajes (
<<<<<<< HEAD
    id_lenguaje INT NOT NULL,
    nombre      VARCHAR(50) NOT NULL UNIQUE,
    PRIMARY KEY (id_lenguaje)
);

CREATE TABLE tecnologias (
    id_tecnologia INT NOT NULL,
    nombre        VARCHAR(100) NOT NULL UNIQUE,
    categoria     VARCHAR(100) NOT NULL,
    PRIMARY KEY (id_tecnologia)
=======
    id INT NOT NULL,
    db_nombre      VARCHAR(50) NOT NULL UNIQUE,
    PRIMARY KEY (id)
);

CREATE TABLE tecnologias (
    id INT NOT NULL,
    db_nombre        VARCHAR(100) NOT NULL UNIQUE,
    db_categoria     VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
>>>>>>> 7d94a73f6235690a169fcdad73044fef080f90df
);

# nivel: Decidimos no hacer una tabla para valores fijos (BÁSICO, INTERMEDIO, AVANZADO, 
# etc.) van a ser manejados desde el frontend con un <select>.
-- ON DELETE CASCADE: si se borra el usuario, se borran sus habilidades.

CREATE TABLE habilidades_lenguaje (
<<<<<<< HEAD
    id_usuario  INT NOT NULL,
    id_lenguaje INT NOT NULL,
    nivel       VARCHAR(50) NOT NULL,
    PRIMARY KEY (id_usuario, id_lenguaje),
    FOREIGN KEY (id_usuario)  REFERENCES usuarios(id)     ON DELETE CASCADE,
    FOREIGN KEY (id_lenguaje) REFERENCES lenguajes(id_lenguaje)
=======
    db_id_usuario  INT NOT NULL,
    db_id_lenguaje INT NOT NULL,
    db_nivel       VARCHAR(50) NOT NULL,
    PRIMARY KEY (db_id_usuario, db_id_lenguaje),
    FOREIGN KEY (db_id_usuario)  REFERENCES usuarios(id)     ON DELETE CASCADE,
    FOREIGN KEY (db_id_lenguaje) REFERENCES lenguajes(id)
>>>>>>> 7d94a73f6235690a169fcdad73044fef080f90df
);

# Igual que habilidades_lenguaje pero para tecnologías.
CREATE TABLE habilidades_tecnologia (
<<<<<<< HEAD
    id_usuario    INT NOT NULL,
    id_tecnologia INT NOT NULL,
    nivel         VARCHAR(50) NOT NULL,
    PRIMARY KEY (id_usuario, id_tecnologia),
    FOREIGN KEY (id_usuario)    REFERENCES usuarios(id)       ON DELETE CASCADE,
    FOREIGN KEY (id_tecnologia) REFERENCES tecnologias(id_tecnologia)
=======
    db_id_usuario    INT NOT NULL,
    db_id_tecnologia INT NOT NULL,
    db_nivel         VARCHAR(50) NOT NULL,
    PRIMARY KEY (db_id_usuario, db_id_tecnologia),
    FOREIGN KEY (db_id_usuario)    REFERENCES usuarios(id)       ON DELETE CASCADE,
    FOREIGN KEY (db_id_tecnologia) REFERENCES tecnologias(id)
>>>>>>> 7d94a73f6235690a169fcdad73044fef080f90df
);

# tipo: valores fijos (REPOSITORIO, DEMO, DOCUMENTACIÓN, etc.) manejados desde el 
# frontend.
CREATE TABLE links_proyecto (
<<<<<<< HEAD
    id_link     INT AUTO_INCREMENT,
    id_proyecto INT NOT NULL,
    tipo        VARCHAR(50)  NOT NULL,
    url         VARCHAR(500) NOT NULL,
    PRIMARY KEY (id_link),
    FOREIGN KEY (id_proyecto) REFERENCES proyectos(id) ON DELETE CASCADE
=======
    id     INT AUTO_INCREMENT,
    db_id_proyecto INT NOT NULL,
    db_tipo        VARCHAR(50)  NOT NULL,
    db_url         VARCHAR(500) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (db_id_proyecto) REFERENCES proyectos(id) ON DELETE CASCADE
>>>>>>> 7d94a73f6235690a169fcdad73044fef080f90df
);

# Regla de negocio: un proyecto solo puede usar lenguajes que el usuario dueño del proyecto 
# tenga registrados en habilidades_lenguaje
CREATE TABLE proyecto_lenguaje (
<<<<<<< HEAD
    id_proyecto INT NOT NULL,
    id_lenguaje INT NOT NULL,
    PRIMARY KEY (id_proyecto, id_lenguaje),
    FOREIGN KEY (id_proyecto) REFERENCES proyectos(id)      ON DELETE CASCADE,
    FOREIGN KEY (id_lenguaje) REFERENCES lenguajes(id_lenguaje)
);

CREATE TABLE proyecto_tecnologia (
    id_proyecto   INT NOT NULL,
    id_tecnologia INT NOT NULL,
    PRIMARY KEY (id_proyecto, id_tecnologia),
    FOREIGN KEY (id_proyecto)   REFERENCES proyectos(id)        ON DELETE CASCADE,
    FOREIGN KEY (id_tecnologia) REFERENCES tecnologias(id_tecnologia)
=======
    db_id_proyecto INT NOT NULL,
    db_id_lenguaje INT NOT NULL,
    PRIMARY KEY (db_id_proyecto, db_id_lenguaje),
    FOREIGN KEY (db_id_proyecto) REFERENCES proyectos(id)      ON DELETE CASCADE,
    FOREIGN KEY (db_id_lenguaje) REFERENCES lenguajes(id)
);

CREATE TABLE proyecto_tecnologia (
    db_id_proyecto   INT NOT NULL,
    db_id_tecnologia INT NOT NULL,
    PRIMARY KEY (db_id_proyecto, db_id_tecnologia),
    FOREIGN KEY (db_id_proyecto)   REFERENCES proyectos(id)        ON DELETE CASCADE,
    FOREIGN KEY (db_id_tecnologia) REFERENCES tecnologias(id)
>>>>>>> 7d94a73f6235690a169fcdad73044fef080f90df
);
