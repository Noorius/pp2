import psycopg2
from config import config

def queue():
    conn = None

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("SELECT * FROM student ORDER BY id ASC")
        print(cur.rowcount)
        #row = cur.fetchone()
        rows = cur.fetchall()

        #while row is not None:
        #    print(row)
        #    row = cur.fetchone()
        for row in rows:
            print(row)

        cur.close()

    except(Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

queue()
    