import psycopg2
import pandas as pd
from config import load_config
from read_data_from_file import read_data
from sqlalchemy import create_engine

def create_table(table_name, data):
    conn = create_engine('postgresql+psycopg2://user:password@localhost:5433/purchases_db')
    df = pd.DataFrame(data)
    df.to_sql(table_name, conn, if_exists='replace', index=False)

def get_query_db(query='', data=0):
    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(query, data)
                rows = cur.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return rows

if __name__ == '__main__':
    ... 