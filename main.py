from read_data_from_file import read_data
from write_data_to_file import write_data
from db_query import get_query_db, create_table

def total_revenue(tbl_name):
    query = 'SELECT sum(price * quantity) AS total_revenue FROM %s;' % (tbl_name)
    answer = get_query_db(query)
    res = answer[0][0]
    print(f'Общая выручка: {res}')
    write_data(f'Общая выручка: {res}')

def items_by_category(tbl_name):
    query = 'SELECT category, array_agg(DISTINCT item) AS items_by_categories FROM %s GROUP BY 1 ORDER BY 1;' % (tbl_name)
    answers = get_query_db(query)
    res = {}
    for answer in answers:
        res[answer[0]] = answer[1]
    print(f'Товары по категориям: {res}')
    write_data(f'Товары по категориям: {res}')
    
def expensive_purchases(tbl_name, min_price=1.0):
    data = read_data('data.txt')
    columns = list(data[0].keys())
    print(columns)
    query = 'SELECT * FROM %s WHERE price > %s;' % (tbl_name, min_price)
    answers = get_query_db(query)
    
    res_1 = list()
    for answer in answers:
        res = dict()
        for i in range(len(columns)):
            res[columns[i]] = answer[i]
        res_1.append(res)
    
    print(f'Покупки дороже {min_price}: {res_1}')
    write_data(f'Покупки дороже {min_price}: {res_1}')
    
def average_price_by_category(tbl_name):
    query = '''
            SELECT category, avg(price) AS avg_price_by_categories
            FROM %s
            GROUP BY 1
            ORDER BY 2;'''% (tbl_name)
    answers = get_query_db(query)
    res = []
    for answer in answers:
        x = {}
        x[answer[0]] = answer[1]
        res.append(x)
        
    print(f'Средняя цена по категориям: {res}')
    write_data(f'Средняя цена по категориям: {res}')

def most_frequent_category(tbl_name):
    query = 'SELECT category, count(quantity) AS best_sail_category FROM %s GROUP BY 1 ORDER BY 2 DESC LIMIT 1;' % (tbl_name)
    answers = get_query_db(query)
    res = answers[0][0]
    print(f'Категория с наибольшим количеством проданных товаров: {res}')
    write_data(f'Категория с наибольшим количеством проданных товаров: {res}')    


if __name__ == '__main__':
    # Считываем данные
    file_data = 'data.txt'
    my_data = read_data(file_data)
    
    # Выбираем название для таблицы в базе данных 'purchases_db'
    table_name = 'purchases'
    
    # Создаем таблицу 'purchases'
    create_table(table_name, my_data)
    
    # Рассчитываем и возвращаем общую выручку (цена * количество для всех записей)
    total_revenue(table_name)
    
    # Возвращаем словарь, где ключ — категория, а значение — список уникальных товаров в этой категории
    items_by_category(table_name)
    
    # Выводим все покупки, где цена товара больше или равна min_price
    price_min = 1.0
    expensive_purchases(table_name, price_min)
    
    # Рассчитываем среднюю цену товаров по каждой категории
    average_price_by_category(table_name)
    
    # Находим и возсращаем категорию, в которой куплено больше всего единиц товаров
    most_frequent_category(table_name)
    