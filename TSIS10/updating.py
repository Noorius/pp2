import psycopg2
from config import config

def update_data(id_,name):
    conn = None
    num_row = 0
    update = '''UPDATE student
                SET fio = %s
                WHERE id = %s '''

    try:
        param = config()
        conn = psycopg2.connect(**param)
        cur = conn.cursor()

        cur.execute(update,(name,id_))
        num_row = cur.rowcount

        conn.commit()
        cur.close()
    except(Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    print(num_row)

update_data(3,"Anna Semenovich")