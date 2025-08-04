import pandas as pd
import mysql.connector

def get_mysql_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="0817",
        database="churn_db"
    )
    query = "SELECT * FROM customers"
    df = pd.read_sql(query, conn)
    conn.close()
    return df
