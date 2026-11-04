# PRIMERA VERSION DE LA BASE DE DATOS

CREATE DATABASE IF NOT EXISTS portfolio;
USE portfolio;

# BASE DE DATOS DEL USUARIO, NOMBRE_USUARIO Y EMAIL NO PUEDE REPETIRSE
# PUEDE QUE SIRVE TENER LA FECHA DE CREACION O PUEDE QUE NO. REVISAR
CREATE TABLE usuarios (
    id_usuario                INT AUTO_INCREMENT,
    nombre_usuario    VARCHAR(50)  NOT NULL UNIQUE,
    email             VARCHAR(255) NOT NULL UNIQUE,
    nombre            VARCHAR(100) NOT NULL,
    apellido          VARCHAR(100) NOT NULL,
    password_hash     VARCHAR(255) NOT NULL,
    fecha_creacion    DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id_usuario)
);

# LOS PROYECTOS TIENEN UN ID_USUARIO, DE AHI SE RELACIONA PARA QUE  UN PROYECTO TENGA UN USUARIO, PERO UN USUARIO PUEDE TENER MUCHOS PROYECTOS
# ETAPA TIENE PARAMETROS FIJOS (COMIENZO, DESARROLLO, ETC) LO VEMOS DESDE EL FRONTEND ESO CON UN SELECT
CREATE TABLE proyectos (
    id_proyecto          INT AUTO_INCREMENT,
    id_usuario           INT NOT NULL,
    nombre               VARCHAR(100) NOT NULL,
    descripcion          VARCHAR(500) NOT NULL,
    etapa                VARCHAR(50) NOT NULL,
    fecha_creacion       DATETIME DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion  DATETIME,
    fecha_finalizacion   DATETIME,
    fecha_limite         DATETIME,
    PRIMARY KEY (id_proyecto),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

# ESTA TABLA SE CREA A PARTIR DE CONECTAR CON LA API DEL DOCENTE Y TRAER TODOS LOS 
# LENGUAJES UNA SOLA VEZ, DESPUES HABRIA QUE VER CADA CUENTO O EN QUE MOMENETO # LA ACTUALIZACIMOS
CREATE TABLE lenguajes (
    id_lenguaje          INT NOT NULL,
    nombre               VARCHAR(50) NOT NULL,
    PRIMARY KEY (id_lenguaje)
);
# LO MISMO QUE LA ANTERIOR PERO CON TECNOLOGIAS
CREATE TABLE tecnologias (
    id_tecnologia        INT NOT NULL,
    nombre               VARCHAR(100) NOT NULL,
    categoria            VARCHAR(100) NOT NULL,
    PRIMARY KEY (id_tecnologia)
);

# TABLA DE RELACION QUE UNO UN ID_DE USUARIO CON UN ID_DE LENGUAJE,
# SE AGREGA EL NIVEL, TAMBIEN HAY OPCIONES FIJAS, LO MANEJAMOS DESDE EL 
# FRONTEND CON UN SELECT. ACA SE EMPIEZA A USAR ON DELETE CASCADE POR SI SE BORRA 
# EL USUARIO TAMBIEN SE BORRAN TAMBIEN TODOS LOS DATOS DE ÉL EN OTRAS TABLAS
# LA PRIMARY KEY ES LA COMBINACION DE LOS DOS ID PORQUE DE ESA MANERA NOS 
# ASEGURAMOS DE QUE NO SE VA A REPETIR y PODEMOS BUSCAR SI DETERMINADO USUARIO 
# SABE DETERMINADO LENGUAJE. ESTO ES IGUAL CON HABILIDADES
CREATE TABLE habilidades_lenguaje (
    id_usuario           INT NOT NULL,
    id_lenguaje          INT NOT NULL,
    nivel                VARCHAR(50) NOT NULL,
    PRIMARY KEY (id_usuario, id_lenguaje),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_lenguaje) REFERENCES lenguajes(id_lenguaje)
);

# LO MISMO QUE LA ANTERIOR PERO CON TECNOLOGIAS
CREATE TABLE habilidades_tecnologia (
    id_usuario           INT NOT NULL,
    id_tecnologia        INT NOT NULL,
    nivel                VARCHAR(50) NOT NULL,
    PRIMARY KEY (id_usuario, id_tecnologia),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_tecnologia) REFERENCES tecnologias(id_tecnologia)
);

# TABLA DE RELACION, UN PROYECTO PUEDE TENER MUCHO LINKS, SE AGREGA TIPO QUE 
# ES OPCIONES FIJAS MANEJADAS DESDE EL FRONT Y LA URL
CREATE TABLE links_proyecto (
    id_link              INT AUTO_INCREMENT,
    id_proyecto          INT NOT NULL,
    tipo                 VARCHAR(50) NOT NULL,
    url                  VARCHAR(500) NOT NULL,
    PRIMARY KEY (id_link),
    FOREIGN KEY (id_proyecto) REFERENCES proyectos(id_proyecto) ON DELETE CASCADE
);

# TABLA DE RELACION PARA VER LOS LENGUAJES USADOS EN UN PROYECTO
# NO GUARDA INFORMACION NUEVA, SOLO RELACIONA, UNE EL ID DEL PROYECTO CON UN ID # DE UN LENGUAJE
CREATE TABLE proyecto_lenguaje (
    id_proyecto          INT NOT NULL,
    id_lenguaje          INT NOT NULL,
    PRIMARY KEY (id_proyecto, id_lenguaje),
    FOREIGN KEY (id_proyecto) REFERENCES proyectos(id_proyecto) ON DELETE CASCADE,
    FOREIGN KEY (id_lenguaje) REFERENCES lenguajes(id_lenguaje)
);

# TABLA DE RELACION PARA VER LAS TECNOLOGIAS USADAS EN UN PROYECTO
# NO GUARDA INFORMACION NUEVA, SOLO RELACIONA
CREATE TABLE proyecto_tecnologia (
    id_proyecto          INT NOT NULL,
    id_tecnologia        INT NOT NULL,
    PRIMARY KEY (id_proyecto, id_tecnologia),
    FOREIGN KEY (id_proyecto) REFERENCES proyectos(id_proyecto) ON DELETE CASCADE,
    FOREIGN KEY (id_tecnologia) REFERENCES tecnologias(id_tecnologia)
);
