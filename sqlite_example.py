import sqlite3


def create_db():
    """
    Создание базы данных
    :return:
    """
    # Подключение к базе данных если такой нет то он ее создаст
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    # Инициализация указателя через который проводятся все операции с базой
    cursor = sqlite_connection.cursor()

    # Чтение файла с sql инструкциями для создания таблиц в базе данных
    fd = open('data_base.sql', 'r')
    sql_file = fd.read()
    fd.close()

    # Разбиение содержимого файла на отдельные инструкции.
    sql_commands = sql_file.split(';')

    # Собственно исполнение каждой инструкции
    for command in sql_commands:
        try:
            cursor.execute(command)
        except sqlite3.OperationalError as msg:
            print("Command skipped: ", msg)
    # Закрываем соединение
    cursor.close()
    sqlite_connection.close()


def insert_data():
    """
    Добавление данных в базу
    :return:
    """
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    cursor = sqlite_connection.cursor()
    # Строка запроса country (name, code) - таблица и поля которые необходимо заполнить VALUES
    # значение полей через запятую для каждой строки
    sql = "INSERT INTO country (country_id, name, code) VALUES (1, 'Россия', 7), (2, 'Китай', 86)"
    # Выполняем запрос
    cursor.execute(sql)
    # Вносим данные непосредственно в базу.
    sqlite_connection.commit()

    sql = "INSERT INTO city (name, code, country_id) VALUES ('Москва', 495, 1), ('Хабаровск', 4212, 1), " \
          "('Харбин', 0451, 2), ('Пекин', 10, 2)"
    cursor.execute(sql)
    sqlite_connection.commit()

    cursor.close()
    sqlite_connection.close()


def get_data():
    """
    Получение данных
    :return:
    """
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    cursor = sqlite_connection.cursor()
    # Получить все значения из таблицы
    # После SELECT все поля таблицы которые нужны, после FROM сама таблица
    sql_all = "SELECT country_id, name, code FROM country"
    # После WHERE усовие если оно истино добавит строку в выборку.
    sql_one_id = "SELECT country_id, name, code FROM country WHERE country_id = 1"
    # Несколько таблиц после названия таблицы можно указать короткий псевдоним типо (country co) и использовать
    # его вместо имени таблицы
    # конструкция JOIN говорит что нужно добавить к строке таблицы country данные из строки таблицы city которые
    # удовлетворяют условию после оператора ON
    sql_many_table = "SELECT co.country_id, co.name, co.code, ci.name, ci.code " \
                 "FROM country co " \
                 "JOIN city ci ON ci.country_id = co.country_id " \
                 "WHERE co.country_id = 1"
    # выполняем запрос
    cursor.execute(sql_all)
    # cursor.fetchall() - получение всех данных запроса. Является генератором если попробовать
    # выполнить цикл еще раз то список будет пуст.
    for i in cursor.fetchall():
        # i является кортежем из значений полей в порядке указания их после SELECT даже если значения нет вернется None
        print(i)

    cursor.execute(sql_one_id)
    # cursor.fetchone() - выдает записи по одной. Можно выполнять несколько раз и
    # получать новую запись пока они не закончатся.
    data = cursor.fetchone()
    print(data)

    cursor.execute(sql_many_table)
    for i in cursor.fetchall():
        print(i)

    cursor.close()
    sqlite_connection.close()


if __name__ == '__main__':
    # create_db()
    # insert_data()
    get_data()
