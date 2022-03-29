-- Создание таблицы если она отсутствует без этого IF NOT EXISTS будует просто создание
-- далее название таблицы и в скобках столбци сначала идет название через пробел тип хранимых данных и ограничения если есть
-- основные типы данных varchar строка int целое число и т.д.
-- ограничения not null не может быть пустым, primary key первичный ключ (уникальное значение и не может быть пустым)
-- Конструкциия FOREIGN KEY (country_id) REFERENCES country (country_id) это связь поля одной таблицы с полем в другой
-- тоесть country_id в таблице city равен  country_id в таблице country (country_id в таблице country должен быть уникальным)
-- в таблице где не указан primary key первичным ключем является ROWID id по умолчанию создается и обслуживается самим sqlite.
CREATE TABLE IF NOT EXISTS city(
    name varchar not null,
    code int,
    country_id int not null,
    FOREIGN KEY (country_id) REFERENCES country (country_id)
);

CREATE TABLE country(
    country_id int primary key,
    name varchar not null,
    code int
)