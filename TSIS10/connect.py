import psycopg2
from config import config

def connect(**params):
    #Connection
    conn = None
     
    try:
        print("Connection to a server")
        conn = psycopg2.connect(**params)

    except(Exception,psycopg2.DatabaseError) as error:
        print(error)

    return conn



