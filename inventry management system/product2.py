import tkinter as tk
from tkinter import ttk, messagebox
from database import (
    connect_database,
    create_database,
    create_product_table
)
# =====================================================
# CREATE DATABASE AND TABLE
# =====================================================
create_database()
create_product_table()
def product_form(parent, show_main_page):
    # =====================================================
    # CLEAR OLD PAGE
    # =====================================================
    for widget in parent.winfo_children():
        widget.destroy()
    # =====================================================
    # MAIN FRAME
    # =====================================================
    product_frame = tk.Frame(
        parent,
        bg="#f2f2f2"
    )
    product_frame.pack(
        fill="both",
        expand=True
    )
    # =====================================================
    # BACK BUTTON
    # =====================================================
    tk.Button(
        product_frame,
        text="← Dashboard",
        font=("Arial", 13),
        bg="#f2f2f2",
        bd=0,
        command=show_main_page
    ).place(
        x=10,
        y=5
    )
    # =====================================================
    # LEFT FORM
    # =====================================================
    form_frame = tk.Frame(
        product_frame,
        bg="#f2f2f2",
        bd=2,
        relief="solid"
    )
    form_frame.place(
        x=10,
        y=50,
        width=380,
        height=425
    )
    # =====================================================
    # TITLE
    # =====================================================
    title_frame = tk.Frame(
        form_frame,
        bg="#15577f",
        height=45
    )
    title_frame.pack(
        fill="x"
    )
    title_frame.pack_propagate(False)
    tk.Label(
        title_frame,
        text="Manage Product Details",
        font=("Times New Roman", 20, "bold"),
        bg="#15577f",
        fg="white"
    ).pack(
        pady=7
    )
    # =====================================================
    # FORM
    # =====================================================
    fields_frame = tk.Frame(
        form_frame,
        bg="#f2f2f2"
    )
    fields_frame.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=10
    )
    # =====================================================
    # CATEGORY
    # =====================================================
    tk.Label(
        fields_frame,
        text="Category",
        font=("Times New Roman", 15),
        bg="#f2f2f2"
    ).grid(
        row=0,
        column=0,
        sticky="w",
        pady=8
    )
    category_combo = ttk.Combobox(
        fields_frame,
        font=("Arial", 12),
        state="readonly",
        width=18
    )
    category_combo.set("Select")
    category_combo.grid(
        row=0,
        column=1,
        padx=15,
        pady=8
    )
    # =====================================================
    # SUPPLIER
    # =====================================================
    tk.Label(
        fields_frame,
        text="Supplier",
        font=("Times New Roman", 15),
        bg="#f2f2f2"
    ).grid(
        row=1,
        column=0,
        sticky="w",
        pady=8
    )
    supplier_combo = ttk.Combobox(
        fields_frame,
        font=("Arial", 12),
        state="readonly",
        width=18
    )
    supplier_combo.set("Select")
    supplier_combo.grid(
        row=1,
        column=1,
        padx=15,
        pady=8
    )
    # =====================================================
    # NAME
    # =====================================================
    tk.Label(
        fields_frame,
        text="Name",
        font=("Times New Roman", 15),
        bg="#f2f2f2"
    ).grid(
        row=2,
        column=0,
        sticky="w",
        pady=8
    )
    name_entry = tk.Entry(
        fields_frame,
        font=("Arial", 12),
        width=20
    )
    name_entry.grid(
        row=2,
        column=1,
        padx=15,
        pady=8
    )
    # =====================================================
    # PRICE
    # =====================================================
    tk.Label(
        fields_frame,
        text="Price",
        font=("Times New Roman", 15),
        bg="#f2f2f2"
    ).grid(
        row=3,
        column=0,
        sticky="w",
        pady=8
    )
    price_entry = tk.Entry(
        fields_frame,
        font=("Arial", 12),
        width=20
    )
    price_entry.grid(
        row=3,
        column=1,
        padx=15,
        pady=8
    )
    # =====================================================
    # QUANTITY
    # =====================================================
    tk.Label(
        fields_frame,
        text="Quantity",
        font=("Times New Roman", 15),
        bg="#f2f2f2"
    ).grid(
        row=4,
        column=0,
        sticky="w",
        pady=8
    )
    quantity_entry = tk.Entry(
        fields_frame,
        font=("Arial", 12),
        width=20
    )
    quantity_entry.grid(
        row=4,
        column=1,
        padx=15,
        pady=8
    )
    # =====================================================
    # STATUS
    # =====================================================
    tk.Label(
        fields_frame,
        text="Status",
        font=("Times New Roman", 15),
        bg="#f2f2f2"
    ).grid(
        row=5,
        column=0,
        sticky="w",
        pady=8
    )
    status_combo = ttk.Combobox(
        fields_frame,
        values=[
            "Available",
            "Out of Stock",
            "Low Stock"
        ],
        font=("Arial", 12),
        state="readonly",
        width=18
    )
    status_combo.set("Select")
    status_combo.grid(
        row=5,
        column=1,
        padx=15,
        pady=8
    )
    # =====================================================
    # RIGHT SIDE
    # =====================================================
    table_area = tk.Frame(
        product_frame,
        bg="#f2f2f2"
    )
    table_area.place(
        x=405,
        y=50,
        relwidth=1,
        width=-420,
        height=425
    )
    # =====================================================
    # SEARCH
    # =====================================================

    search_frame = tk.LabelFrame(
        table_area,
        text="Search Products",
        font=("Times New Roman", 14, "bold"),
        bg="#f2f2f2",
        bd=2
    )

    search_frame.pack(
        fill="x",
        pady=(0, 10)
    )

    tk.Label(
        search_frame,
        text="Search By",
        font=("Arial", 11),
        bg="#f2f2f2"
    ).pack(
        side="left",
        padx=8,
        pady=8
    )

    search_combo = ttk.Combobox(
        search_frame,
        values=[
            "ID",
            "Category",
            "Supplier",
            "Name",
            "Price"
        ],
        state="readonly",
        width=15
    )

    search_combo.set("Name")

    search_combo.pack(
        side="left",
        padx=5
    )

    search_entry = tk.Entry(
        search_frame,
        font=("Arial", 11),
        width=18
    )

    search_entry.pack(
        side="left",
        padx=5
    )

    # =====================================================
    # TABLE
    # =====================================================

    table_frame = tk.Frame(
        table_area,
        bg="#f2f2f2"
    )

    table_frame.pack(
        fill="both",
        expand=True
    )

    scroll_y = ttk.Scrollbar(
        table_frame,
        orient="vertical"
    )

    scroll_x = ttk.Scrollbar(
        table_frame,
        orient="horizontal"
    )

    product_table = ttk.Treeview(
        table_frame,
        columns=(
            "ID",
            "Category",
            "Supplier",
            "Name",
            "Price",
            "Quantity",
            "Status"
        ),
        show="headings",
        yscrollcommand=scroll_y.set,
        xscrollcommand=scroll_x.set
    )

    scroll_y.config(
        command=product_table.yview
    )

    scroll_x.config(
        command=product_table.xview
    )

    # Headings

    product_table.heading(
        "ID",
        text="ID"
    )

    product_table.heading(
        "Category",
        text="Category"
    )

    product_table.heading(
        "Supplier",
        text="Supplier"
    )

    product_table.heading(
        "Name",
        text="Name"
    )

    product_table.heading(
        "Price",
        text="Price"
    )

    product_table.heading(
        "Quantity",
        text="Quantity"
    )

    product_table.heading(
        "Status",
        text="Status"
    )

    # Columns

    product_table.column(
        "ID",
        width=50
    )

    product_table.column(
        "Category",
        width=150
    )

    product_table.column(
        "Supplier",
        width=130
    )

    product_table.column(
        "Name",
        width=120
    )

    product_table.column(
        "Price",
        width=80
    )

    product_table.column(
        "Quantity",
        width=80
    )

    product_table.column(
        "Status",
        width=110
    )

    product_table.pack(
        side="left",
        fill="both",
        expand=True
    )

    scroll_y.pack(
        side="right",
        fill="y"
    )

    scroll_x.pack(
        side="bottom",
        fill="x"
    )

    # =====================================================
    # LOAD CATEGORIES
    # =====================================================

    def load_categories():

        connection = connect_database()

        if connection is None:
            return

        try:

            cursor = connection.cursor()

            cursor.execute(
                "SELECT name FROM categories ORDER BY name"
            )

            rows = cursor.fetchall()

            category_combo["values"] = [
                row[0] for row in rows
            ]

            cursor.close()
            connection.close()

        except Exception as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )

    # =====================================================
    # LOAD SUPPLIERS
    # =====================================================

    def load_suppliers():

        connection = connect_database()

        if connection is None:
            return

        try:

            cursor = connection.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS suppliers (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL
                )
            """)

            connection.commit()

            cursor.execute(
                "SELECT name FROM suppliers ORDER BY name"
            )

            rows = cursor.fetchall()

            supplier_combo["values"] = [
                row[0] for row in rows
            ]

            cursor.close()
            connection.close()

        except Exception as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )

    # =====================================================
    # LOAD PRODUCTS
    # =====================================================

    def load_products():

        for item in product_table.get_children():
            product_table.delete(item)

        connection = connect_database()

        if connection is None:
            return

        try:

            cursor = connection.cursor()

            cursor.execute("""
                SELECT id, category, supplier, name,
                       price, quantity, status
                FROM products
                ORDER BY id DESC
            """)

            rows = cursor.fetchall()

            for row in rows:

                product_table.insert(
                    "",
                    tk.END,
                    values=row
                )

            cursor.close()
            connection.close()

        except Exception as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )

    # =====================================================
    # CLEAR
    # =====================================================

    def clear_fields():

        category_combo.set("Select")
        supplier_combo.set("Select")

        name_entry.delete(
            0,
            tk.END
        )

        price_entry.delete(
            0,
            tk.END
        )

        quantity_entry.delete(
            0,
            tk.END
        )

        status_combo.set("Select")

        product_table.selection_remove(
            product_table.selection()
        )

    # =====================================================
    # SAVE
    # =====================================================

    def save_product():

        category = category_combo.get()
        supplier = supplier_combo.get()
        name = name_entry.get().strip()
        price = price_entry.get().strip()
        quantity = quantity_entry.get().strip()
        status = status_combo.get()

        if category == "Select":
            messagebox.showwarning(
                "Warning",
                "Please select Category"
            )
            return

        if supplier == "Select":
            messagebox.showwarning(
                "Warning",
                "Please select Supplier"
            )
            return

        if name == "":
            messagebox.showwarning(
                "Warning",
                "Please enter Product Name"
            )
            return

        if price == "" or quantity == "":
            messagebox.showwarning(
                "Warning",
                "Please enter Price and Quantity"
            )
            return

        if status == "Select":
            messagebox.showwarning(
                "Warning",
                "Please select Status"
            )
            return

        try:

            price = float(price)
            quantity = int(quantity)

        except ValueError:

            messagebox.showerror(
                "Error",
                "Price must be a number and Quantity must be an integer"
            )
            return

        connection = connect_database()

        if connection is None:
            return

        try:

            cursor = connection.cursor()

            cursor.execute("""
                INSERT INTO products
                (category, supplier, name, price, quantity, status)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                category,
                supplier,
                name,
                price,
                quantity,
                status
            ))

            connection.commit()

            cursor.close()
            connection.close()

            load_products()
            clear_fields()

            messagebox.showinfo(
                "Success",
                "Product Saved Successfully"
            )

        except Exception as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )

    # =====================================================
    # SELECT PRODUCT
    # =====================================================

    def select_product(event):

        selected = product_table.focus()

        if not selected:
            return

        values = product_table.item(
            selected,
            "values"
        )

        category_combo.set(values[1])
        supplier_combo.set(values[2])

        name_entry.delete(
            0,
            tk.END
        )

        name_entry.insert(
            0,
            values[3]
        )

        price_entry.delete(
            0,
            tk.END
        )

        price_entry.insert(
            0,
            values[4]
        )

        quantity_entry.delete(
            0,
            tk.END
        )

        quantity_entry.insert(
            0,
            values[5]
        )

        status_combo.set(values[6])

    # =====================================================
    # UPDATE
    # =====================================================

    def update_product():

        selected = product_table.focus()

        if not selected:

            messagebox.showwarning(
                "Warning",
                "Please select a product first"
            )

            return

        values = product_table.item(
            selected,
            "values"
        )

        product_id = values[0]

        category = category_combo.get()
        supplier = supplier_combo.get()
        name = name_entry.get().strip()
        price = price_entry.get().strip()
        quantity = quantity_entry.get().strip()
        status = status_combo.get()

        if category == "Select" or supplier == "Select":

            messagebox.showwarning(
                "Warning",
                "Please select Category and Supplier"
            )

            return

        if name == "" or price == "" or quantity == "":

            messagebox.showwarning(
                "Warning",
                "Please fill all fields"
            )

            return

        try:

            price = float(price)
            quantity = int(quantity)

        except ValueError:

            messagebox.showerror(
                "Error",
                "Invalid Price or Quantity"
            )

            return

        if status == "Select":

            messagebox.showwarning(
                "Warning",
                "Please select Status"
            )

            return

        connection = connect_database()

        if connection is None:
            return

        try:

            cursor = connection.cursor()

            cursor.execute("""
                UPDATE products
                SET category=%s,
                    supplier=%s,
                    name=%s,
                    price=%s,
                    quantity=%s,
                    status=%s
                WHERE id=%s
            """, (
                category,
                supplier,
                name,
                price,
                quantity,
                status,
                product_id
            ))

            connection.commit()

            cursor.close()
            connection.close()

            load_products()
            clear_fields()

            messagebox.showinfo(
                "Success",
                "Product Updated Successfully"
            )

        except Exception as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )

    # =====================================================
    # DELETE
    # =====================================================

    def delete_product():

        selected = product_table.focus()

        if not selected:

            messagebox.showwarning(
                "Warning",
                "Please select a product first"
            )

            return

        values = product_table.item(
            selected,
            "values"
        )

        product_id = values[0]

        answer = messagebox.askyesno(
            "Delete Product",
            "Do you want to delete this product?"
        )

        if not answer:
            return

        connection = connect_database()

        if connection is None:
            return

        try:

            cursor = connection.cursor()

            cursor.execute(
                "DELETE FROM products WHERE id=%s",
                (product_id,)
            )

            connection.commit()

            cursor.close()
            connection.close()

            load_products()
            clear_fields()

            messagebox.showinfo(
                "Success",
                "Product Deleted Successfully"
            )

        except Exception as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )

    # =====================================================
    # SEARCH
    # =====================================================

    def search_product():

        search_value = search_entry.get().strip()

        if search_value == "":
            messagebox.showwarning(
                "Warning",
                "Please enter search value"
            )
            return

        search_by = search_combo.get()

        column = "name"

        if search_by == "ID":
            column = "id"

        elif search_by == "Category":
            column = "category"

        elif search_by == "Supplier":
            column = "supplier"

        elif search_by == "Name":
            column = "name"

        elif search_by == "Price":
            column = "price"

        connection = connect_database()

        if connection is None:
            return

        try:

            cursor = connection.cursor()

            if search_by == "ID":

                query = f"""
                    SELECT id, category, supplier, name,
                           price, quantity, status
                    FROM products
                    WHERE id=%s
                    ORDER BY id DESC
                """

                cursor.execute(
                    query,
                    (search_value,)
                )

            else:

                query = f"""
                    SELECT id, category, supplier, name,
                           price, quantity, status
                    FROM products
                    WHERE {column} LIKE %s
                    ORDER BY id DESC
                """

                cursor.execute(
                    query,
                    ("%" + search_value + "%",)
                )

            rows = cursor.fetchall()

            for item in product_table.get_children():
                product_table.delete(item)

            for row in rows:

                product_table.insert(
                    "",
                    tk.END,
                    values=row
                )

            cursor.close()
            connection.close()

        except Exception as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )

    # =====================================================
    # SHOW ALL
    # =====================================================

    def show_all():

        search_entry.delete(
            0,
            tk.END
        )

        load_products()

    # =====================================================
    # SEARCH BUTTON
    # =====================================================

    tk.Button(
        search_frame,
        text="Search",
        font=("Times New Roman", 12, "bold"),
        bg="#15577f",
        fg="white",
        width=9,
        command=search_product
    ).pack(
        side="left",
        padx=5
    )

    # =====================================================
    # SHOW ALL BUTTON
    # =====================================================

    tk.Button(
        search_frame,
        text="Show All",
        font=("Times New Roman", 12, "bold"),
        bg="#15577f",
        fg="white",
        width=9,
        command=show_all
    ).pack(
        side="left",
        padx=5
    )

    # =====================================================
    # BUTTONS
    # =====================================================

    button_frame = tk.Frame(
        form_frame,
        bg="#f2f2f2"
    )

    button_frame.pack(
        side="bottom",
        pady=10
    )

    tk.Button(
        button_frame,
        text="Save",
        font=("Times New Roman", 13, "bold"),
        bg="#15577f",
        fg="white",
        width=8,
        command=save_product
    ).pack(
        side="left",
        padx=7
    )

    tk.Button(
        button_frame,
        text="Update",
        font=("Times New Roman", 13, "bold"),
        bg="#15577f",
        fg="white",
        width=8,
        command=update_product
    ).pack(
        side="left",
        padx=7
    )

    tk.Button(
        button_frame,
        text="Delete",
        font=("Times New Roman", 13, "bold"),
        bg="#15577f",
        fg="white",
        width=8,
        command=delete_product
    ).pack(
        side="left",
        padx=7
    )

    tk.Button(
        button_frame,
        text="Clear",
        font=("Times New Roman", 13, "bold"),
        bg="#15577f",
        fg="white",
        width=8,
        command=clear_fields
    ).pack(
        side="left",
        padx=7
    )
    # =====================================================
    # TABLE CLICK
    # =====================================================
    product_table.bind(
        "<ButtonRelease-1>",
        select_product
    )
    # =====================================================
    # LOAD DATA
    # =====================================================
    load_categories()
    load_suppliers()
    load_products()