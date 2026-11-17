-- Usuario en localhost --
-- Crear un nuevo usuario con una contraseña segura
CREATE USER 'user_portfolio'@'localhost' IDENTIFIED BY 'api_portfolio_grupo_21';

-- Conceder todos los privilegios en la base de datos 
GRANT ALL PRIVILEGES ON portfolio.* TO 'user_portfolio'@'localhost' WITH GRANT OPTION;

-- Aplicar los cambios de privilegios
FLUSH PRIVILEGES;

-- Verificar los privilegios del nuevo usuario
SHOW GRANTS FOR 'user_portfolio'@'localhost';