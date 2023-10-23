import psycopg2
def create_connection():
    connection = None
    try:
        # устанавливаем соединение с базой данных
        conn = psycopg2.connect(database="etl", user="etl", password="password", host="localhost", port="5432")
        print("Connection to pgsql DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection