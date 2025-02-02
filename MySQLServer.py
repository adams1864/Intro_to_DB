import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",  # Change if your MySQL server is running on a different host
            user="root",       # Change to your MySQL username
            password=""        # Add your MySQL password if set
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:  # Use mysql.connector.Error explicitly
        print(f"Error: {e}")

    finally:
        # Close cursor and connection
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Run the function
if __name__ == "__main__":
    create_database()
