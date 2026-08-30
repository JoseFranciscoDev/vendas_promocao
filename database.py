from mysql import connector

connection_config = {
    "user": "scott",
    "password": "password",
    "host": "127.0.0.1",
    "database": "employees",
}
connection = connector.connect(**connection_config)


def run_query(query):
    if connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
