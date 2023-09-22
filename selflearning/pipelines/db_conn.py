#import needed libraries
import psycopg2
import mysql.connector

# source database
def get_conn_mysql():
    conn = mysql.connector.connect(host="localhost", port=3306, user="etl", password="etl", db="etl")
    # start a connection
    cur = conn.cursor()
    return cur, conn
# target database
def get_conn_postgresql():
    conn = psycopg2.connect(host="localhost",database="etl",user="etl",password="password")
    # start a connection
    cur = conn.cursor()
    return cur, conn