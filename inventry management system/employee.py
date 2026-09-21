import tkinter as tk
from tkinter import ttk, messagebox
import pymysql

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "pakistan"
DB_NAME = "inventory_db"


def connect_database():
    try:
        return pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            charset="utf8mb4"
        )
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return None


def setup_database():
    try:
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = connection.cursor()

        cursor.execute(
            f"""
            CREATE DATABASE IF NOT EXISTS {DB_NAME}
            CHARACTER SET utf8mb4
            COLLATE utf8mb4_unicode_ci
            """
        )

        connection.commit()
        cursor.close()
        connection.close()

        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS employees (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(150) NOT NULL,
                phone VARCHAR(30) NOT NULL,
                gender VARCHAR(20),
                address VARCHAR(255)
            )
            """
        )

        connection.commit()
        cursor.close()
        connection.close()

        return True

    except Exception as e:
        messagebox.showerror("Database Setup Error", str(e))
        return False


def employee_form(parent, show_main_page):

    if not setup_database():
        return

    for widget in parent.winfo_children():
        widget.destroy()

    employee_frame = tk.Frame(parent, bg="#f2f2f2")
    employee_frame.pack(fill="both", expand=True)

    tk.Label(
        employee_frame,
        text="employee Management",
        font=("Arial", 24, "bold"),
        bg="#f2f2f2",
        fg="#101b4d"
    ).pack(pady=5)

    tk.Button(
        employee_frame,
        text="← Dashboard",
        command=show_main_page,
        bg="#455c68",
        fg="white",
        font=("Arial", 11, "bold"),
        padx=15,
        pady=3
    ).pack(anchor="w", padx=20)

    form_frame = tk.Frame(
        employee_frame,
        bg="white",
        bd=1,
        relief="solid"
    )
    form_frame.pack(fill="x", padx=20, pady=5)

    tk.Label(
        form_frame,
        text="employee ID",
        bg="white",
        font=("Arial", 11)
    ).grid(row=0, column=0, padx=10, pady=10)

    id_entry = tk.Entry(form_frame, width=25)
    id_entry.grid(row=0, column=1, padx=10, pady=10)
    id_entry.config(state="readonly")

    tk.Label(
        form_frame,
        text="employee Name",
        bg="white",
        font=("Arial", 11)
    ).grid(row=1, column=0, padx=10, pady=10)

    name_entry = tk.Entry(form_frame, width=25)
    name_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(
        form_frame,
        text="Email",
        bg="white",
        font=("Arial", 11)
    ).grid(row=0, column=2, padx=10, pady=10)

    email_entry = tk.Entry(form_frame, width=25)
    email_entry.grid(row=0, column=3, padx=10, pady=10)

    tk.Label(
        form_frame,
        text="Phone",
        bg="white",
        font=("Arial", 11)
    ).grid(row=1, column=2, padx=10, pady=10)

    phone_entry = tk.Entry(form_frame, width=25)
    phone_entry.grid(row=1, column=3, padx=10, pady=10)

    tk.Label(
        form_frame,
        text="Gender",
        bg="white",
        font=("Arial", 11)
    ).grid(row=0, column=4, padx=10, pady=10)

    gender_combo = ttk.Combobox(
        form_frame,
        values=["Male", "Female", "Other"],
        width=23,
        state="readonly"
    )
    gender_combo.grid(row=0, column=5, padx=10, pady=10)

    tk.Label(
        form_frame,
        text="Address",
        bg="white",
        font=("Arial", 11)
    ).grid(row=1, column=4, padx=10, pady=10)

    address_entry = tk.Entry(form_frame, width=25)
    address_entry.grid(row=1, column=5, padx=10, pady=10)

    table_frame = tk.Frame(employee_frame, bg="#f2f2f2")
    table_frame.pack(fill="both", expand=True, padx=20)

    search_frame = tk.Frame(table_frame, bg="#f2f2f2")
    search_frame.pack(fill="x", pady=5)

    tk.Label(
        search_frame,
        text="Search employee:",
        bg="#f2f2f2",
        font=("Arial", 11, "bold")
    ).pack(side="left", padx=5)

    search_entry = tk.Entry(search_frame, width=35)
    search_entry.pack(side="left", padx=5)

    columns = (
        "ID",
        "Name",
        "Email",
        "Phone",
        "Gender",
        "Address"
    )

    employee_table = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings"
    )

    for col in columns:
        employee_table.heading(col, text=col)
        employee_table.column(col, width=150)

    employee_table.pack(
        fill="both",
        expand=True,
        pady=10
    )

    def get_next_id():

        connection = connect_database()

        if connection is None:
            return

        try:
            cursor = connection.cursor()

            cursor.execute(
                "SELECT COALESCE(MAX(id), 0) + 1 FROM employees"
            )

            next_id = cursor.fetchone()[0]

            cursor.close()
            connection.close()

            id_entry.config(state="normal")
            id_entry.delete(0, tk.END)
            id_entry.insert(0, str(next_id))
            id_entry.config(state="readonly")

        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def clear_fields():

        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        gender_combo.set("")
        address_entry.delete(0, tk.END)

        employee_table.selection_remove(
            employee_table.selection()
        )

        get_next_id()
        name_entry.focus()

    def load_employees():

        employee_table.delete(
            *employee_table.get_children()
        )

        connection = connect_database()

        if connection is None:
            return

        try:
            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT id, name, email, phone, gender, address
                FROM employees
                ORDER BY id DESC
                """
            )

            records = cursor.fetchall()

            for emp in records:
                employee_table.insert(
                    "",
                    tk.END,
                    values=emp
                )

            cursor.close()
            connection.close()

            get_next_id()

        except Exception as e:
            messagebox.showerror(
                "Database Error",
                str(e)
            )

    def add_employee():

        name = name_entry.get().strip()
        email = email_entry.get().strip()
        phone = phone_entry.get().strip()
        gender = gender_combo.get().strip()
        address = address_entry.get().strip()

        if not name:
            messagebox.showwarning(
                "Warning",
                "Please enter employee name."
            )
            name_entry.focus()
            return

        if not email:
            messagebox.showwarning(
                "Warning",
                "Please enter email."
            )
            email_entry.focus()
            return

        if not phone:
            messagebox.showwarning(
                "Warning",
                "Please enter phone."
            )
            phone_entry.focus()
            return

        connection = connect_database()

        if connection is None:
            return

        try:
            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO employees
                (name, email, phone, gender, address)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (
                    name,
                    email,
                    phone,
                    gender,
                    address
                )
            )

            connection.commit()

            cursor.close()
            connection.close()

            load_employees()
            clear_fields()

            messagebox.showinfo(
                "Success",
                "employee added successfully!"
            )

        except Exception as e:
            connection.rollback()
            connection.close()

            messagebox.showerror(
                "Database Error",
                str(e)
            )

    def select_employee(event):

        selected = employee_table.selection()

        if not selected:
            return

        values = employee_table.item(
            selected[0],
            "values"
        )

        id_entry.config(state="normal")
        id_entry.delete(0, tk.END)
        id_entry.insert(0, values[0])
        id_entry.config(state="readonly")

        name_entry.delete(0, tk.END)
        name_entry.insert(0, values[1])

        email_entry.delete(0, tk.END)
        email_entry.insert(0, values[2])

        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, values[3])

        gender_combo.set(values[4])

        address_entry.delete(0, tk.END)
        address_entry.insert(0, values[5])

    def update_employee():

        selected = employee_table.selection()

        if not selected:
            messagebox.showwarning(
                "Warning",
                "Please select an employee first."
            )
            return

        employee_id = employee_table.item(
            selected[0],
            "values"
        )[0]

        name = name_entry.get().strip()
        email = email_entry.get().strip()
        phone = phone_entry.get().strip()
        gender = gender_combo.get().strip()
        address = address_entry.get().strip()

        if not name or not email or not phone:
            messagebox.showwarning(
                "Warning",
                "Please fill all required fields."
            )
            return

        connection = connect_database()

        if connection is None:
            return

        try:
            cursor = connection.cursor()

            cursor.execute(
                """
                UPDATE employees
                SET
                    name = %s,
                    email = %s,
                    phone = %s,
                    gender = %s,
                    address = %s
                WHERE id = %s
                """,
                (
                    name,
                    email,
                    phone,
                    gender,
                    address,
                    employee_id
                )
            )

            connection.commit()

            cursor.close()
            connection.close()

            load_employees()
            clear_fields()

            messagebox.showinfo(
                "Success",
                "employee updated successfully!"
            )

        except Exception as e:
            connection.rollback()
            connection.close()

            messagebox.showerror(
                "Database Error",
                str(e)
            )

    def delete_employee():

        selected = employee_table.selection()

        if not selected:
            messagebox.showwarning(
                "Warning",
                "Please select an employee first."
            )
            return

        employee_id = employee_table.item(
            selected[0],
            "values"
        )[0]

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this employee?"
        )

        if not confirm:
            return

        connection = connect_database()

        if connection is None:
            return

        try:
            cursor = connection.cursor()

            cursor.execute(
                """
                DELETE FROM employees
                WHERE id = %s
                """,
                (employee_id,)
            )

            connection.commit()

            cursor.close()
            connection.close()

            load_employees()
            clear_fields()

            messagebox.showinfo(
                "Success",
                "employee deleted successfully!"
            )

        except Exception as e:
            connection.rollback()
            connection.close()

            messagebox.showerror(
                "Database Error",
                str(e)
            )

    def search_employee():

        search_text = search_entry.get().strip()

        employee_table.delete(
            *employee_table.get_children()
        )

        connection = connect_database()

        if connection is None:
            return

        try:
            cursor = connection.cursor()

            value = "%" + search_text + "%"

            cursor.execute(
                """
                SELECT
                    id,
                    name,
                    email,
                    phone,
                    gender,
                    address
                FROM employees
                WHERE
                    CAST(id AS CHAR) LIKE %s
                    OR name LIKE %s
                    OR email LIKE %s
                    OR phone LIKE %s
                    OR gender LIKE %s
                    OR address LIKE %s
                ORDER BY id DESC
                """,
                (
                    value,
                    value,
                    value,
                    value,
                    value,
                    value
                )
            )

            records = cursor.fetchall()

            cursor.close()
            connection.close()

            for emp in records:
                employee_table.insert(
                    "",
                    tk.END,
                    values=emp
                )

            if not records:
                messagebox.showinfo(
                    "Search",
                    "employee not found."
                )

        except Exception as e:
            messagebox.showerror(
                "Database Error",
                str(e)
            )

    def show_all_employees():

        search_entry.delete(
            0,
            tk.END
        )

        load_employees()

    tk.Button(
        search_frame,
        text="Search",
        command=search_employee,
        bg="#167b7b",
        fg="white",
        font=("Arial", 10, "bold"),
        padx=15,
        pady=5
    ).pack(side="left", padx=5)

    tk.Button(
        search_frame,
        text="Show All",
        command=show_all_employees,
        bg="#455c68",
        fg="white",
        font=("Arial", 10, "bold"),
        padx=15,
        pady=5
    ).pack(side="left", padx=5)

    button_frame = tk.Frame(
        employee_frame,
        bg="#f2f2f2"
    )

    button_frame.pack(pady=10)

    tk.Button(
        button_frame,
        text="➕ Add employee",
        command=add_employee,
        bg="#167b7b",
        fg="white",
        font=("Arial", 10, "bold"),
        padx=20,
        pady=8
    ).pack(side="left", padx=5)

    tk.Button(
        button_frame,
        text="✏ Update employee",
        command=update_employee,
        bg="#e67e22",
        fg="white",
        font=("Arial", 10, "bold"),
        padx=20,
        pady=8
    ).pack(side="left", padx=5)

    tk.Button(
        button_frame,
        text="🗑 Delete employee",
        command=delete_employee,
        bg="#c0392b",
        fg="white",
        font=("Arial", 10, "bold"),
        padx=20,
        pady=8
    ).pack(side="left", padx=5)

    tk.Button(
        button_frame,
        text="✖ Clear",
        command=clear_fields,
        bg="#777777",
        fg="white",
        font=("Arial", 10, "bold"),
        padx=20,
        pady=8
    ).pack(side="left", padx=5)

    employee_table.bind(
        "<<TreeviewSelect>>",
        select_employee
    )

    load_employees()