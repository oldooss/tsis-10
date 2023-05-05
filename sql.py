import psycopg2
from config import host, user, password, db_name


try:
    #connect to exist database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

    connection.autocommit = True
    # cursor = connection.cursor()

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version: {cursor.fetchone()}")

    #create a new table

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE PhoneBook(
    #         first_name varchar(50) NOT NULL,
    #         phone_number varchar NOT NULL PRIMARY KEY);"""
    #     )
    #     print("[INFO] Table created successfully")

    # adding user

    # name_new = str(input())
    # phone_new = str(input())
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         f"""INSERT INTO phonebook (first_name, phone_number) VALUES
    #         ('{name_new}', '{phone_new}');"""
    #     )

    # adding by using csv

    # with connection.cursor() as cursor:
    #             cursor.execute("""COPY phonebook(first_name, phone_number)
    #                             FROM 'C:/Users/Public/table.csv'
    #                             DELIMITER ','
    #                             CSV HEADER;""")


    # change user first name or phone

    # new_first_name = str(input())
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #        f"UPDATE phonebook SET first_name='{new_first_name}';"""
    #     )

    # delete user or phone

    drop = str(input())
    with connection.cursor() as cursor:
        cursor.execute(f"""DELETE FROM phonebook WHERE first_name = '{drop}' OR phone_number = '{drop}'""")


except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")





































# import psycopg2
#
# conn = psycopg2.connect(host="localhost",
#                         dbname="postgres",
#                         user="postgres",
#                         passward= "Paidos01_",
#                         port=5432)
#
# cur = conn.cursor()
#
#
#     cur.execute("""CREATE TABLE IF NOT EXIST
#     """)
#
#
#
#
# conn.commit()
#
# cur.close()
# conn.close()