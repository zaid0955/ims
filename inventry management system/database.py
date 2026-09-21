import pymysql
from tkinter import messagebox


def connect_database():

    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="pakistan",
            database="inventory_db"
        )

        return connection

    except pymysql.Error as error:

        messagebox.showerror(
            "Database Error",
            f"Could not connect to database:\n{error}"
        )

        return None


def create_database():

    try:

        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="pakistan"
        )

        cursor = connection.cursor()

        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS inventory_db"
        )

        connection.commit()

        cursor.close()
        connection.close()

    except pymysql.Error as error:

        messagebox.showerror(
            "Database Error",
            str(error)
        )


def create_product_table():

    connection = connect_database()

    if connection is None:
        return

    try:

        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                category VARCHAR(100) NOT NULL,
                supplier VARCHAR(100) NOT NULL,
                name VARCHAR(100) NOT NULL,
                price DECIMAL(10,2) NOT NULL,
                quantity INT NOT NULL,
                status VARCHAR(50) NOT NULL
            )
        """)

        connection.commit()

        cursor.close()
        connection.close()

    except pymysql.Error as error:

        messagebox.showerror(
            "Database Error",
            str(error)
        )