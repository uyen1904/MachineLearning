import sqlite3

import pandas as pd
from django.db.transaction import get_connection

try:
    #Connect to  DB and create a cursor
    sqliteConnection=sqlite3.connect('../databases/Chinook_Sqlite.sqlite')
    cursor=sqliteConnection.cursor()
    print('DB Init')
    #Write a query and execute it with cursor
    query='SELECT * FROM Invoice LIMIT 5;'
    cursor.execute(query)
    #Fetch and output result
    df=pd.DataFrame(cursor.fetchall())
    print(df)
    #Close the cursor
    cursor.close()
#Handle errors
except sqlite3.Error as error:
    print('Error occurred -',error)
#Close DB Connection irrespective of success of failure
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed')


# (1) TOP N Invoice có giá trị từ a->b
def get_invoices(n, a, b):
    try:
        conn = sqlite3.connect('../databases/Chinook_Sqlite.sqlite')
        cursor = conn.cursor()

        query = f'''
            SELECT * FROM Invoice
            WHERE Total BETWEEN {a} AND {b}
            ORDER BY Total DESC
            LIMIT {n}
        '''
        cursor.execute(query)
        df = pd.DataFrame(cursor.fetchall(),
                          columns=[desc[0] for desc in cursor.description])

        cursor.close()
        conn.close()
        return df

    except sqlite3.Error as error:
        print('Error occurred -', error)
        return None
#Demo
print("\n" + "="*50)
print("(1) TOP 5 Invoice có giá trị từ 5 đến 10:")
print(get_invoices(5, 5, 10))


# (2) TOP N khách hàng có nhiều Invoice nhất
def get_customers_most_invoices(n):
    try:
        conn = sqlite3.connect('../databases/Chinook_Sqlite.sqlite')
        cursor = conn.cursor()

        query = f'''
            SELECT 
                c.CustomerId,
                c.FirstName || ' ' || c.LastName AS Name,
                COUNT(i.InvoiceId) AS TotalInvoices
            FROM Customer c
            JOIN Invoice i ON c.CustomerId = i.CustomerId
            GROUP BY c.CustomerId
            ORDER BY TotalInvoices DESC
            LIMIT {n}
        '''
        cursor.execute(query)
        df = pd.DataFrame(cursor.fetchall(),
                          columns=[desc[0] for desc in cursor.description])

        cursor.close()
        conn.close()
        return df

    except sqlite3.Error as error:
        print('Error occurred -', error)
        return None
#Demo
print("\n" + "="*50)
print("(2) TOP 5 khách hàng có nhiều Invoice nhất:")
print(get_customers_most_invoices(9))


# (3) TOP N khách hàng có tổng giá trị cao nhất
def get_customers_highest_revenue(n):
    try:
        conn = sqlite3.connect('../databases/Chinook_Sqlite.sqlite')
        cursor = conn.cursor()

        query = f'''
            SELECT 
                c.CustomerId,
                c.FirstName || ' ' || c.LastName AS Name,
                SUM(i.Total) AS TotalRevenue
            FROM Customer c
            JOIN Invoice i ON c.CustomerId = i.CustomerId
            GROUP BY c.CustomerId
            ORDER BY TotalRevenue DESC
            LIMIT {n}
        '''
        cursor.execute(query)
        df = pd.DataFrame(cursor.fetchall(),
                          columns=[desc[0] for desc in cursor.description])

        cursor.close()
        conn.close()
        return df

    except sqlite3.Error as error:
        print('Error occurred -', error)
        return None
#Demo
print("\n" + "="*50)
print("(3) TOP 5 khách hàng có tổng doanh thu cao nhất:")
print(get_customers_highest_revenue(10))