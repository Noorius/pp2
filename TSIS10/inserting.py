import psycopg2 
from config import config

def insert_data(fio):
    sql = '''INSERT INTO student(fio)
            VALUES(%s) RETURNING id;'''
    conn = None
    idi = None

    try:
        param = config()

        conn = psycopg2.connect(**param)
        cur = conn.cursor()

        #cur.execute(sql,(fio,))
        cur.executemany(sql,fio)

        #idi = cur.fetchone()[0]

        conn.commit()
        cur.close()
    except(Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    #print(idi)

insert_data([("Nur Zhetessov",),("Student 1",),("Student 2",)])