import tkinter as tk
from tkinter import ttk, messagebox
import pymysql


# =====================================================
# DATABASE SETTINGS
# =====================================================

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "pakistan"
DB_NAME = "inventory_db"


# =====================================================
# CONNECT DATABASE
# =====================================================

def connect_database():

    try:

        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            charset="utf8mb4"
        )

        return connection

    except Exception as e:

        messagebox.showerror(
            "Database Error",
            str(e)
        )

        return None


# =====================================================
# SETUP DATABASE
# =====================================================

def setup_database():

    try:

        # Connect without database
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            charset="utf8mb4"
        )

        cursor = connection.cursor()

        # Create database
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


        # Connect to inventory database
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            charset="utf8mb4"
        )

        cursor = connection.cursor()


        # =================================================
        # CREATE SUPPLIERS TABLE
        # =================================================

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS suppliers
            (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(100) NOT NULL,
                Email VARCHAR(150) NOT NULL,
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

        messagebox.showerror(
            "Database Setup Error",
            str(e)
        )

        return False


# =====================================================
# SUPPLIER FORM
# =====================================================

def supplier_form(parent, show_main_page):

    if not setup_database():
        return


    # =================================================
    # CLEAR OLD PAGE
    # =================================================

    for widget in parent.winfo_children():
        widget.destroy()


    # =================================================
    # MAIN FRAME
    # =================================================

    supplier_frame = tk.Frame(
        parent,
        bg="#f2f2f2"
    )

    supplier_frame.pack(
        fill="both",
        expand=True
    )


    # =================================================
    # TITLE
    # =================================================

    tk.Label(
        supplier_frame,
        text="Supplier Management",
        font=("Arial", 24, "bold"),
        bg="#f2f2f2",
        fg="#101b4d"
    ).pack(
        pady=5
    )


    # =================================================
    # BACK BUTTON
    # =================================================

    tk.Button(
        supplier_frame,
        text="← Dashboard",
        command=show_main_page,
        bg="#455c68",
        fg="white",
        font=("Arial", 11, "bold"),
        padx=15,
        pady=3
    ).pack(
        anchor="w",
        padx=20
    )


    # =================================================
    # FORM FRAME
    # =================================================

    form_frame = tk.Frame(
        supplier_frame,
        bg="white",
        bd=1,
        relief="solid"
    )

    form_frame.pack(
        fill="x",
        padx=20,
        pady=5
    )


    # =================================================
    # SUPPLIER ID
    # =================================================

    tk.Label(
        form_frame,
        text="Supplier ID",
        bg="white",
        font=("Arial", 11)
    ).grid(
        row=0,
        column=0,
        padx=10,
        pady=10
    )

    id_entry = tk.Entry(
        form_frame,
        width=25,
        font=("Arial", 11)
    )

    id_entry.grid(
        row=0,
        column=1,
        padx=10,
        pady=10
    )

    id_entry.config(
        state="readonly"
    )


    # =================================================
    # SUPPLIER NAME
    # =================================================

    tk.Label(
        form_frame,
        text="Supplier Name",
        bg="white",
        font=("Arial", 11)
    ).grid(
        row=1,
        column=0,
        padx=10,
        pady=10
    )

    name_entry = tk.Entry(
        form_frame,
        width=25,
        font=("Arial", 11)
    )

    name_entry.grid(
        row=1,
        column=1,
        padx=10,
        pady=10
    )


    # =================================================
    # EMAIL
    # =================================================

    tk.Label(
        form_frame,
        text="Email",
        bg="white",
        font=("Arial", 11)
    ).grid(
        row=0,
        column=2,
        padx=10,
        pady=10
    )

    email_entry = tk.Entry(
        form_frame,
        width=25,
        font=("Arial", 11)
    )

    email_entry.grid(
        row=0,
        column=3,
        padx=10,
        pady=10
    )


    # =================================================
    # PHONE
    # =================================================

    tk.Label(
        form_frame,
        text="Phone",
        bg="white",
        font=("Arial", 11)
    ).grid(
        row=1,
        column=2,
        padx=10,
        pady=10
    )

    phone_entry = tk.Entry(
        form_frame,
        width=25,
        font=("Arial", 11)
    )

    phone_entry.grid(
        row=1,
        column=3,
        padx=10,
        pady=10
    )


    # =================================================
    # GENDER
    # =================================================

    tk.Label(
        form_frame,
        text="Gender",
        bg="white",
        font=("Arial", 11)
    ).grid(
        row=0,
        column=4,
        padx=10,
        pady=10
    )

    gender_combo = ttk.Combobox(
        form_frame,
        values=[
            "Male",
            "Female",
            "Other"
        ],
        width=23,
        state="readonly"
    )

    gender_combo.grid(
        row=0,
        column=5,
        padx=10,
        pady=10
    )


    # =================================================
    # ADDRESS
    # =================================================

    tk.Label(
        form_frame,
        text="Address",
        bg="white",
        font=("Arial", 11)
    ).grid(
        row=1,
        column=4,
        padx=10,
        pady=10
    )

    address_entry = tk.Entry(
        form_frame,
        width=25,
        font=("Arial", 11)
    )

    address_entry.grid(
        row=1,
        column=5,
        padx=10,
        pady=10
    )


    # =================================================
    # TABLE AREA
    # =================================================

    table_frame = tk.Frame(
        supplier_frame,
        bg="#f2f2f2"
    )

    table_frame.pack(
        fill="both",
        expand=True,
        padx=20
    )


    # =================================================
    # SEARCH FRAME
    # =================================================

    search_frame = tk.Frame(
        table_frame,
        bg="#f2f2f2"
    )

    search_frame.pack(
        fill="x",
        pady=5
    )


    tk.Label(
        search_frame,
        text="Search Supplier:",
        bg="#f2f2f2",
        font=("Arial", 11, "bold")
    ).pack(
        side="left",
        padx=5
    )


    search_entry = tk.Entry(
        search_frame,
        width=35,
        font=("Arial", 11)
    )

    search_entry.pack(
        side="left",
        padx=5
    )


    # =================================================
    # TABLE
    # =================================================

    columns = (
        "ID",
        "Name",
        "Email",
        "Phone",
        "Gender",
        "Address"
    )


    supplier_table = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings"
    )


    supplier_table.heading(
        "ID",
        text="ID"
    )

    supplier_table.heading(
        "Name",
        text="Name"
    )

    supplier_table.heading(
        "Email",
        text="Email"
    )

    supplier_table.heading(
        "Phone",
        text="Phone"
    )

    supplier_table.heading(
        "Gender",
        text="Gender"
    )

    supplier_table.heading(
        "Address",
        text="Address"
    )


    supplier_table.column(
        "ID",
        width=70
    )

    supplier_table.column(
        "Name",
        width=160
    )

    supplier_table.column(
        "Email",
        width=200
    )

    supplier_table.column(
        "Phone",
        width=130
    )

    supplier_table.column(
        "Gender",
        width=100
    )

    supplier_table.column(
        "Address",
        width=220
    )


    # =================================================
    # SCROLLBARS
    # =================================================

    scroll_y = ttk.Scrollbar(
        table_frame,
        orient="vertical",
        command=supplier_table.yview
    )

    scroll_x = ttk.Scrollbar(
        table_frame,
        orient="horizontal",
        command=supplier_table.xview
    )


    supplier_table.configure(
        yscrollcommand=scroll_y.set,
        xscrollcommand=scroll_x.set
    )


    supplier_table.pack(
        side="left",
        fill="both",
        expand=True,
        pady=10
    )

    scroll_y.pack(
        side="right",
        fill="y"
    )

    scroll_x.pack(
        side="bottom",
        fill="x"
    )


    # =================================================
    # GET NEXT ID
    # =================================================

    def get_next_id():

        connection = connect_database()

        if connection is None:
            return

        try:

            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT COALESCE(MAX(id), 0) + 1
                FROM suppliers
                """
            )

            next_id = cursor.fetchone()[0]

            cursor.close()
            connection.close()


            id_entry.config(
                state="normal"
            )

            id_entry.delete(
                0,
                tk.END
            )

            id_entry.insert(
                0,
                str(next_id)
            )

            id_entry.config(
                state="readonly"
            )


        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )


    # =================================================
    # CLEAR FIELDS
    # =================================================

    def clear_fields():

        name_entry.delete(
            0,
            tk.END
        )

        email_entry.delete(
            0,
            tk.END
        )

        phone_entry.delete(
            0,
            tk.END
        )

        gender_combo.set("")

        address_entry.delete(
            0,
            tk.END
        )


        supplier_table.selection_remove(
            supplier_table.selection()
        )


        get_next_id()

        name_entry.focus()


    # =================================================
    # LOAD SUPPLIERS
    # =================================================

    def load_suppliers():

        for item in supplier_table.get_children():

            supplier_table.delete(item)


        connection = connect_database()

        if connection is None:
            return


        try:

            cursor = connection.cursor()


            cursor.execute(
                """
                SELECT
                    id,
                    name,
                    Email,
                    phone,
                    gender,
                    address
                FROM suppliers
                ORDER BY id DESC
                """
            )


            records = cursor.fetchall()


            for supplier in records:

                supplier_table.insert(
                    "",
                    tk.END,
                    values=supplier
                )


            cursor.close()
            connection.close()


            get_next_id()


        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )


    # =================================================
    # ADD SUPPLIER
    # =================================================

    def add_supplier():

        name = name_entry.get().strip()
        email = email_entry.get().strip()
        phone = phone_entry.get().strip()
        gender = gender_combo.get().strip()
        address = address_entry.get().strip()


        if not name:

            messagebox.showwarning(
                "Warning",
                "Please enter Supplier Name."
            )

            name_entry.focus()

            return


        if not email:

            messagebox.showwarning(
                "Warning",
                "Please enter Email."
            )

            email_entry.focus()

            return


        if not phone:

            messagebox.showwarning(
                "Warning",
                "Please enter Phone."
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
                INSERT INTO suppliers
                (
                    name,
                    Email,
                    phone,
                    gender,
                    address
                )
                VALUES
                (
                    %s,
                    %s,
                    %s,
                    %s,
                    %s
                )
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


            load_suppliers()

            clear_fields()


            messagebox.showinfo(
                "Success",
                "Supplier Added Successfully!"
            )


        except Exception as e:

            connection.rollback()
            connection.close()


            messagebox.showerror(
                "Database Error",
                str(e)
            )


    # =================================================
    # SELECT SUPPLIER
    # =================================================

    def select_supplier(event):

        selected = supplier_table.selection()

        if not selected:
            return


        values = supplier_table.item(
            selected[0],
            "values"
        )


        # ID
        id_entry.config(
            state="normal"
        )

        id_entry.delete(
            0,
            tk.END
        )

        id_entry.insert(
            0,
            values[0]
        )

        id_entry.config(
            state="readonly"
        )


        # Name
        name_entry.delete(
            0,
            tk.END
        )

        name_entry.insert(
            0,
            values[1]
        )


        # Email
        email_entry.delete(
            0,
            tk.END
        )

        email_entry.insert(
            0,
            values[2]
        )


        # Phone
        phone_entry.delete(
            0,
            tk.END
        )

        phone_entry.insert(
            0,
            values[3]
        )


        # Gender
        gender_combo.set(
            values[4]
        )


        # Address
        address_entry.delete(
            0,
            tk.END
        )

        address_entry.insert(
            0,
            values[5]
        )


    # =================================================
    # UPDATE SUPPLIER
    # =================================================

    def update_supplier():

        selected = supplier_table.selection()

        if not selected:

            messagebox.showwarning(
                "Warning",
                "Please select a supplier first."
            )

            return


        supplier_id = supplier_table.item(
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
                UPDATE suppliers
                SET
                    name = %s,
                    Email = %s,
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
                    supplier_id
                )
            )


            connection.commit()


            cursor.close()
            connection.close()


            load_suppliers()

            clear_fields()


            messagebox.showinfo(
                "Success",
                "Supplier Updated Successfully!"
            )


        except Exception as e:

            connection.rollback()
            connection.close()


            messagebox.showerror(
                "Database Error",
                str(e)
            )


    # =================================================
    # DELETE SUPPLIER
    # =================================================

    def delete_supplier():

        selected = supplier_table.selection()

        if not selected:

            messagebox.showwarning(
                "Warning",
                "Please select a supplier first."
            )

            return


        supplier_id = supplier_table.item(
            selected[0],
            "values"
        )[0]


        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this supplier?"
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
                DELETE FROM suppliers
                WHERE id = %s
                """,
                (supplier_id,)
            )


            connection.commit()


            cursor.close()
            connection.close()


            load_suppliers()

            clear_fields()


            messagebox.showinfo(
                "Success",
                "Supplier Deleted Successfully!"
            )


        except Exception as e:

            connection.rollback()
            connection.close()


            messagebox.showerror(
                "Database Error",
                str(e)
            )


    # =================================================
    # SEARCH SUPPLIER
    # =================================================

    def search_supplier():

        search_text = search_entry.get().strip()


        if search_text == "":

            load_suppliers()

            return


        value = "%" + search_text + "%"


        connection = connect_database()

        if connection is None:
            return


        try:

            cursor = connection.cursor()


            cursor.execute(
                """
                SELECT
                    id,
                    name,
                    Email,
                    phone,
                    gender,
                    address
                FROM suppliers
                WHERE
                    CAST(id AS CHAR) LIKE %s
                    OR name LIKE %s
                    OR Email LIKE %s
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


            for item in supplier_table.get_children():

                supplier_table.delete(item)


            for supplier in records:

                supplier_table.insert(
                    "",
                    tk.END,
                    values=supplier
                )


            cursor.close()
            connection.close()


            if not records:

                messagebox.showinfo(
                    "Search",
                    "Supplier not found."
                )


        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )


    # =================================================
    # SHOW ALL
    # =================================================

    def show_all_suppliers():

        search_entry.delete(
            0,
            tk.END
        )

        load_suppliers()


    # =================================================
    # SEARCH BUTTON
    # =================================================

    tk.Button(
        search_frame,
        text="Search",
        command=search_supplier,
        bg="#167b7b",
        fg="white",
        font=("Arial", 10, "bold"),
        padx=15,
        pady=5
    ).pack(
        side="left",
        padx=5
    )


    # =================================================
    # SHOW ALL BUTTON
    # =================================================

    tk.Button(
        search_frame,
        text="Show All",
        command=show_all_suppliers,
        bg="#455c68",
        fg="white",
        font=("Arial", 10, "bold"),
        padx=15,
        pady=5
    ).pack(
        side="left",
        padx=5
    )


    # =================================================
    # BUTTON FRAME
    # =================================================

    button_frame = tk.Frame(
        supplier_frame,
        bg="#f2f2f2"
    )

    button_frame.pack(
        pady=10
    )


    # =================================================
    # ADD BUTTON
    # =================================================

    tk.Button(
        button_frame,
        text="➕ Add Supplier",
        command=add_supplier,
        bg="#167b7b",
        fg="white",
        font=("Arial", 10, "bold"),
        padx=20,
        pady=8
    ).pack(
        side="left",
        padx=5
    )


    # =================================================
    # UPDATE BUTTON
    # =================================================

    tk.Button(
        button_frame,
        text="✏ Update Supplier",
        command=update_supplier,
        bg="#e67e22",
        fg="white",
        font=("Arial", 10, "bold"),
        padx=20,
        pady=8
    ).pack(
        side="left",
        padx=5
    )


    # =================================================
    # DELETE BUTTON
    # =================================================

    tk.Button(
        button_frame,
        text="🗑 Delete Supplier",
        command=delete_supplier,
        bg="#c0392b",
        fg="white",
        font=("Arial", 10, "bold"),
        padx=20,
        pady=8
    ).pack(
        side="left",
        padx=5
    )


    # =================================================
    # CLEAR BUTTON
    # =================================================

    tk.Button(
        button_frame,
        text="✖ Clear",
        command=clear_fields,
        bg="#777777",
        fg="white",
        font=("Arial", 10, "bold"),
        padx=20,
        pady=8
    ).pack(
        side="left",
        padx=5
    )


    # =================================================
    # TABLE SELECTION
    # =================================================

    supplier_table.bind(
        "<<TreeviewSelect>>",
        select_supplier
    )


    # =================================================
    # LOAD DATA
    # =================================================

    load_suppliers()