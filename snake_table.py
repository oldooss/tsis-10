import psycopg2
from config import host, user, password, db_name


try:

    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")

        print(f"Server version: {cursor.fetchone()}")

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE snake(
                user_name varchar(50) NOT NULL PRIMARY KEY,
                user_score INTEGER NOT NULL );"""
        )

except Exception as error:
    print("error:", error)

finally:
    if connection:
        connection.close()
        print("connection closed")