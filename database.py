from mysql import connector

connection_config = {
    "user": "scott",
    "password": "password",
    "host": "127.0.0.1",
    "database": "employees",
}
conection = connector.connect(**connection_config)
