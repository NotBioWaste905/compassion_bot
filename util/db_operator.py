import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def create_db():
    try:
        cursor, connection = connect_to_db()

        sql_create_database = '''CREATE TABLE Q_N_A
                          (ID INT PRIMARY KEY     NOT NULL,
                          PROBLEM        TEXT   NOT NULL,
                          ANSWER         TEXT   NOT NULL); '''
        cursor.execute(sql_create_database)
        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            print("База данных создана.")
            disconnect(cursor, connection)

def connect_to_db():
    connection = psycopg2.connect(user="postgres",
                                  password="1111",
                                  host="localhost")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()
    print("Соединение с PostgreSQL установлено.")

    return cursor, connection

def disconnect(cursor, connection):
    cursor.close()
    connection.close()
    print("Соединение с PostgreSQL закрыто.")

def insert_data():
    pass

def read_data():
    pass

if __name__ == '__main__':
    create_db()
