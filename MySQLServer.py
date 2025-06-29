import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (not to a specific database)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',            # Replace with your username
            password='Hybrid-5004#!' # Replace with your password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
            
    except Error as e:
        print(f"❌ Error while connecting to MySQL: {e}")

    finally:
        # Close cursor and connection if they exist
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

# Run the function
create_database()
