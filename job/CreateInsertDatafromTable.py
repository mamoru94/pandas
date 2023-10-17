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
# Пример данных
return_message()
data = dict(messages[1])
# Получение списка ключей из словаря result
result = { "op": data["op"], "ts": data["ts"], **data["pk"], **data["data"]}
print(result)
keys = list(result.keys())
value = list(result.values())
# Подключение к базе данных
conn = psycopg2.connect(database="etl", user="etl", password="password", host="localhost", port="5432")

# Создание курсора
cur = conn.cursor()

# Формирование строки для запроса на создание таблицы
columns = ", ".join([f"{key} TEXT" for key in keys])
# Формирование строки для запроса на insert таблицы
db_value = ", ".join([f"'{values}'::TEXT" for values in value])
columns_for_insert = ", ".join([f"{key}" for key in keys])
# query
drop_table_query = f"DROP TABLE IF EXISTS etl.testtest CASCADE;"
create_table_query = f"CREATE TABLE IF NOT EXISTS etl.testtest ({columns});"
insert_table_query = f"INSERT INTO etl.testtest ({columns_for_insert}) VALUES ({db_value});"
# Выполнение запроса
cur.execute(drop_table_query)
cur.execute(create_table_query)
cur.execute(insert_table_query)
# сохранение изменений в базе данных
conn.commit()
# Закрытие курсора и соединения
cur.close()
conn.close()