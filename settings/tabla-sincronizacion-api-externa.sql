-- Esta tabla es creada para guardar un registro de las sincronizaciones con la api externa.
-- En la primera ejecucion de la aplicacion, al no tener registros, se cargan los datos de la api
-- En ejecuciones posteriores, se verifica si la ultima fecha de carga es mayor a un determinado tiempo (Debe evaluarse)
-- En caso de superar ese tiempo, se vuelve a consultar la api y se sincroniza con la copia local
-- Si el tiempo no se cumple, se continua con la copia local directamente

CREATE TABLE IF NOT EXISTS sincronizacion_api(
    id INT AUTO_INCREMENT,
    db_fecha_sincronizacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
)