# ВЫПОЛНЕНИЕ ИТОГОВОГО ЗАДАНИЯ УРОКА 13
Есть вот такой вот список покупок.

purchases = [
{"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
{"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
{"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
{"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3}
]

item — название товара,
category — категория товара,
price — цена за единицу товара,
quantity — количество единиц, купленных за один раз.
Вам нужно реализовать несколько функций для анализа данных:

# total_revenue(purchases): 
  Рассчитайте и верните общую выручку (цена * количество для всех записей).

# items_by_category(purchases): 
  Верните словарь, где ключ — категория, а значение — список уникальных товаров в этой категории.
# expensive_purchases(purchases, min_price): 
  Выведите все покупки, где цена товара больше или равна min_price.
# average_price_by_category(purchases): 
  Рассчитайте среднюю цену товаров по каждой категории.
# most_frequent_category(purchases): 
Найдите и верните категорию, в которой куплено больше всего единиц товаров (учитывайте поле quantity).

## Ваш скрипт должен выводить отчёт по каждому из следующих пунктов:

- Общая выручка.
- Список товаров по категориям.
- Список покупок, где цена превышает заданное значение.
- Средняя цена товаров по категориям.
- Категория с наибольшим числом проданных товаров.
## Формат вывода должен соответствовать шаблону вида

Общая выручка: 21.0
Товары по категориям: {'fruit': ['apple', 'banana'], 'dairy': ['milk'], 'bakery': ['bread']}
Покупки дороже 1.0: [{'item': 'apple', 'category': 'fruit', 'price': 1.2, 'quantity': 10}, {'item': 'milk', 'category': 'dairy', 'price': 1.5, 'quantity': 2}, {'item': 'bread', 'category': 'bakery', 'price': 2.0, 'quantity': 3}]
Средняя цена по категориям: {'fruit': 0.85, 'dairy': 1.5, 'bakery': 2.0}
Категория с наибольшим количеством проданных товаров: fruit

### В  ответе укажите ссылку на ваш git-репозиторий.

### ВЫПОЛНЕНИЕ РАБОТЫ
Мной было принято решение не упрощать себе жизнь и выполнить все с помощью SQL. Хотя на PANDAS было и проще и быстрее.

 - начальные данные были записаны в файл 'data.txt'
 - в скрипте 'read_data_from_file.py' реализовано чтение данных
 - в скрипте 'write_data_to_file.py' реализована построчная запись результатов в файл 'report.txt'
 - 'database.ini' - config-file подключения к базе . 
 - 'config.py' - чтение config-файла
 - 'connect.py' - подключение к базе
 - создана база данных 'purchases_db'
 - в 'db_query.py' реализовано создание таблиц и выполнения запросов к базе
 - в 'main.py' созданы требуемые функции.
 - результат записан в 'report.txt'

### Перед выполнением скрипта 'main.py' нужно удалить файл с результатами
Иначе, результаты будут задублированы  
