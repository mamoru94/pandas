import psycopg2
def return_message():
    try:
        # Подключение к базе данных
        conn = psycopg2.connect(database="etl", user="etl", password="password", host="localhost", port="5432")

        # Создание курсора
        cur = conn.cursor()

        # Выполнение запроса на выборку данных
        cur.execute("SELECT message FROM etl.kafka")

        # Извлечение данных
        rows = cur.fetchall()

        # Закрытие курсора и соединения с базой данных
        cur.close()

        # Обработка данных
        messages = []
        for row in rows:
            messages.append(row[0])
        return messages

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        if conn is not None:
            conn.rollback()
            conn.close()

messages = return_message()
print(messages)