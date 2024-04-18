from dotenv import dotenv_values

# Obtener las variables de entorno de PostgreSQL
postgres_env = dotenv_values(".env.dev")
POSTGRES_PORT_CONTAINER = postgres_env["POSTGRES_PORT_CONTAINER"]
POSTGRES_PORT_PC = postgres_env["POSTGRES_PORT_PC"]
POSTGRES_PASSWORD = postgres_env["POSTGRES_PASSWORD"]
POSTGRES_USER = postgres_env["POSTGRES_USER"]
POSTGRES_DB = postgres_env["POSTGRES_DB"]
POSTGRES_HOST = postgres_env["POSTGRES_HOST"]

# Obtener las variables de entorno de PGAdmin
pgadmin_env = dotenv_values(".env.dev")
PGADMIN_DEFAULT_EMAIL = pgadmin_env["PGADMIN_DEFAULT_EMAIL"]
PGADMIN_DEFAULT_PASSWORD = pgadmin_env["PGADMIN_DEFAULT_PASSWORD"]
PGADMIN_LISTEN_PORT_CONTAINER = pgadmin_env["PGADMIN_LISTEN_PORT_CONTAINER"]
PGADMIN_LISTEN_PORT_PC = pgadmin_env["PGADMIN_LISTEN_PORT_PC"]
