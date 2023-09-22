#import needed libraries
import psycopg2
import mysql.connector
import pymysql
# source database
def get_conn_mysql():
    conn = pymysql.connect(
        host="localhost",
        user="etl",
        password="etl",
        database="etl"
        )
    # start a connection
    cur = conn.cursor()
    return cur, conn

# target database
def get_conn_postgresql():
    conn = psycopg2.connect(host="localhost",database="etl",user="etl",password="password")
    # start a connection
    cur = conn.cursor()
    return cur, conn