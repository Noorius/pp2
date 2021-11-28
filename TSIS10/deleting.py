import psycopg2
from config import config

def delete(idi):
    conn = None
    delete_sql = "DELETE FROM student WHERE id = %s"
    num_rows = 0

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()

        cursor.execute(delete_sql,(idi,))
        num_rows = cursor.rowcount

        conn.commit()

        cursor.close()
    except(Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            
delete(3)
