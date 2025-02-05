import mysql.connector
from mysql.connector import Error

def create_database():
    try:
       
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Rowzay_27" 
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error:
        print(f"Error connecting to MySQL")

    finally:
        
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()