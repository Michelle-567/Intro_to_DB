import mysql.connector

def create_database():
    try:
        # Connect to MySQL server (no database specified)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',            # Replace with your MySQL username
            password='Hybrid-5004#!' # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"❌ Error while connecting to MySQL: {err}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

create_database()
