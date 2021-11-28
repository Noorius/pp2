import psycopg2
from config import config

def create_table():
    commands = (
    '''CREATE TABLE student (
        id SERIAL PRIMARY KEY, 
        fio varchar(100) UNIQUE NOT NULL
    )
    ''',
    '''CREATE TABLE payment (
        id INT NOT NULL,
        payed INT,
        loan INT,
        PRIMARY KEY (id),
        FOREIGN KEY(id)
            REFERENCES student (id)
    )
    ''',
    '''CREATE TABLE personal(
        id INT NOT NULL,
        adress varchar(100) NOT NULL,
        phone INT NOT NULL,
        PRIMARY KEY(id),
        FOREIGN KEY(id)
            REFERENCES student (id)
    )    
    ''')
    
    conn = None
    
    try:
        param = config()
        conn = psycopg2.connect(**param)

        cur = conn.cursor()
        
        for command in commands:
            cur.execute(command)
        
        cur.close()
        conn.commit()
    
    except(Exception,psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

create_table()