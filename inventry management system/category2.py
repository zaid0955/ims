import tkinter as tk
from tkinter import ttk, messagebox

from database import (
    connect_database,
    create_database
)


# =====================================================
# CREATE DATABASE
# =====================================================

create_database()


# =====================================================
# CATEGORY FORM
# =====================================================

def category_form(parent, show_main_page):

    # =====================================================
    # CLEAR OLD PAGE
    # =====================================================

    for widget in parent.winfo_children():
        widget.destroy()

    # =====================================================
    # CREATE CATEGORY TABLE
    # =====================================================

    connection = connect_database()

    if connection is not None:

        try:

            cursor = connection.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS categories (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    description VARCHAR(255)
                )
            """)

            connection.commit()

            cursor.close()
            connection.close()

        except Exception as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )

            return

    # =====================================================
    # MAIN FRAME
    # =====================================================

    category_frame = tk.Frame(
        parent,
        bg="#f2f2f2"
    )

    category_frame.pack(
        fill="both",
        expand=True
    )

    # =====================================================
    # TITLE
    # =====================================================

    title_frame = tk.Frame(
        category_frame,
        bg="#15577f",
        height=45
    )

    title_frame.pack(
        fill="x"
    )

    title_frame.pack_propagate(False)

    tk.Label(
        title_frame,
        text="Manage Product Category",
        font=("Times New Roman", 20, "bold"),
        bg="#15577f",
        fg="white"
    ).pack(
        pady=7
    )

    # =====================================================
    # BACK BUTTON
    # =====================================================

    tk.Button(
        category_frame,
        text="← Dashboard",
        font=("Arial", 12),
        bg="#9f5a5a",
        fg="white",
        bd=0,
        command=show_main_page
    ).place(
        x=15,
        y=30
    )

    # =====================================================
    # FORM
    # =====================================================

    form_frame = tk.Frame(
        category_frame,
        bg="#f2f2f2"
    )

    form_frame.place(
        x=470,
        y=60
    )

    # =====================================================
    # CATEGORY ID
    # =====================================================

    tk.Label(
        form_frame,
        text="Category ID",
        font=("Times New Roman", 14),
        bg="#f2f2f2"
    ).grid(
        row=0,
        column=0,
        padx=10,
        pady=10,
        sticky="w"
    )

    category_id_entry = tk.Entry(
        form_frame,
        font=("Arial", 12),
        width=28,
        state="readonly"
    )

    category_id_entry.grid(
        row=0,
        column=1,
        padx=10,
        pady=10
    )

    # =====================================================
    # CATEGORY NAME
    # =====================================================

    tk.Label(
        form_frame,
        text="Category Name",
        font=("Times New Roman", 14),
        bg="#f2f2f2"
    ).grid(
        row=1,
        column=0,
        padx=10,
        pady=10,
        sticky="w"
    )

    category_name_entry = tk.Entry(
        form_frame,
        font=("Arial", 12),
        width=28
    )

    category_name_entry.grid(
        row=1,
        column=1,
        padx=10,
        pady=10
    )

    # =====================================================
    # DESCRIPTION
    # =====================================================

    tk.Label(
        form_frame,
        text="Description",
        font=("Times New Roman", 14),
        bg="#f2f2f2"
    ).grid(
        row=2,
        column=0,
        padx=10,
        pady=10,
        sticky="nw"
    )

    description_text = tk.Text(
        form_frame,
        font=("Arial", 12),
        width=28,
        height=4
    )

    description_text.grid(
        row=2,
        column=1,
        padx=10,
        pady=10
    )

    # =====================================================
    # TABLE
    # =====================================================

    table_frame = tk.Frame(
        category_frame,
        bg="#f2f2f2"
    )

    table_frame.place(
        x=470,
        y=315,
        width=500,
        height=250
    )

    # =====================================================
    # VERTICAL SCROLLBAR
    # =====================================================

    scroll_y = ttk.Scrollbar(
        table_frame,
        orient=tk.VERTICAL
    )

    # =====================================================
    # HORIZONTAL SCROLLBAR
    # =====================================================

    scroll_x = ttk.Scrollbar(
        table_frame,
        orient=tk.HORIZONTAL
    )

    # =====================================================
    # TREEVIEW
    # =====================================================

    category_table = ttk.Treeview(
        table_frame,
        columns=(
            "ID",
            "Name",
            "Description"
        ),
        show="headings",
        yscrollcommand=scroll_y.set,
        xscrollcommand=scroll_x.set
    )

    # =====================================================
    # SCROLLBAR COMMAND
    # =====================================================

    scroll_y.config(
        command=category_table.yview
    )

    scroll_x.config(
        command=category_table.xview
    )

    # =====================================================
    # TABLE HEADINGS
    # =====================================================

    category_table.heading(
        "ID",
        text="Category ID"
    )

    category_table.heading(
        "Name",
        text="Category Name"
    )

    category_table.heading(
        "Description",
        text="Description"
    )

    # =====================================================
    # TABLE COLUMNS
    # =====================================================

    category_table.column(
        "ID",
        width=90
    )

    category_table.column(
        "Name",
        width=150
    )

    category_table.column(
        "Description",
        width=250
    )

    # =====================================================
    # PACK TABLE
    # =====================================================

    category_table.pack(
        side=tk.TOP,
        fill=tk.BOTH,
        expand=True
    )

    scroll_y.pack(
        side=tk.RIGHT,
        fill=tk.Y
    )

    scroll_x.pack(
        side=tk.BOTTOM,
        fill=tk.X
    )

    # =====================================================
    # CLEAR FIELDS
    # =====================================================

    def clear_fields():

        category_id_entry.config(
            state="normal"
        )

        category_id_entry.delete(
            0,
            tk.END
        )

        category_id_entry.config(
            state="readonly"
        )

        category_name_entry.delete(
            0,
            tk.END
        )

        description_text.delete(
            "1.0",
            tk.END
        )

        category_table.selection_remove(
            category_table.selection()
        )

    # =====================================================
    # LOAD CATEGORIES
    # =====================================================

    def load_categories():

        # Clear table

        for item in category_table.get_children():

            category_table.delete(item)

        connection = connect_database()

        if connection is None:
            return

        try:

            cursor = connection.cursor()

            cursor.execute("""
                SELECT id, name, description
                FROM categories
                ORDER BY id DESC
            """)

            rows = cursor.fetchall()

            for row in rows:

                category_table.insert(
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
    # ADD CATEGORY
    # =====================================================

    def add_category():

        name = category_name_entry.get().strip()

        description = description_text.get(
            "1.0",
            tk.END
        ).strip()

        # Check name

        if name == "":

            messagebox.showwarning(
                "Warning",
                "Please enter Category Name"
            )

            return

        connection = connect_database()

        if connection is None:
            return

        try:

            cursor = connection.cursor()

            # Check duplicate category

            cursor.execute(
                """
                SELECT id
                FROM categories
                WHERE name=%s
                """,
                (name,)
            )

            existing = cursor.fetchone()

            if existing:

                messagebox.showwarning(
                    "Warning",
                    "This category already exists"
                )

                cursor.close()
                connection.close()

                return

            # Insert category

            cursor.execute(
                """
                INSERT INTO categories
                (name, description)
                VALUES (%s, %s)
                """,
                (
                    name,
                    description
                )
            )

            connection.commit()

            cursor.close()
            connection.close()

            load_categories()

            clear_fields()

            messagebox.showinfo(
                "Success",
                "Category Added Successfully"
            )

        except Exception as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )

    # =====================================================
    # SELECT CATEGORY
    # =====================================================

    def select_category(event):

        selected = category_table.focus()

        if not selected:
            return

        values = category_table.item(
            selected,
            "values"
        )

        clear_fields()

        # Category ID

        category_id_entry.config(
            state="normal"
        )

        category_id_entry.insert(
            0,
            values[0]
        )

        category_id_entry.config(
            state="readonly"
        )

        # Category Name

        category_name_entry.insert(
            0,
            values[1]
        )

        # Description

        description_text.insert(
            "1.0",
            values[2]
        )

    # =====================================================
    # DELETE CATEGORY
    # =====================================================

    def delete_category():

        selected = category_table.focus()

        if not selected:

            messagebox.showwarning(
                "Warning",
                "Please select a category first"
            )

            return

        values = category_table.item(
            selected,
            "values"
        )

        category_id = values[0]

        answer = messagebox.askyesno(
            "Delete Category",
            "Do you want to delete this category?"
        )

        if not answer:
            return

        connection = connect_database()

        if connection is None:
            return

        try:

            cursor = connection.cursor()

            cursor.execute(
                """
                DELETE FROM categories
                WHERE id=%s
                """,
                (category_id,)
            )

            connection.commit()

            cursor.close()
            connection.close()

            load_categories()

            clear_fields()

            messagebox.showinfo(
                "Success",
                "Category Deleted Successfully"
            )

        except Exception as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )

    # =====================================================
    # BUTTON FRAME
    # =====================================================

    button_frame = tk.Frame(
        form_frame,
        bg="#f2f2f2"
    )

    button_frame.grid(
        row=3,
        column=1,
        pady=10
    )

    # =====================================================
    # ADD BUTTON
    # =====================================================

    tk.Button(
        button_frame,
        text="Add",
        font=("Times New Roman", 13, "bold"),
        bg="#15577f",
        fg="white",
        width=10,
        command=add_category
    ).pack(
        side=tk.LEFT,
        padx=10
    )

    # =====================================================
    # DELETE BUTTON
    # =====================================================

    tk.Button(
        button_frame,
        text="Delete",
        font=("Times New Roman", 13, "bold"),
        bg="#15577f",
        fg="white",
        width=10,
        command=delete_category
    ).pack(
        side=tk.LEFT,
        padx=10
    )

    # =====================================================
    # CLEAR BUTTON
    # =====================================================

    tk.Button(
        button_frame,
        text="Clear",
        font=("Times New Roman", 13, "bold"),
        bg="#15577f",
        fg="white",
        width=10,
        command=clear_fields
    ).pack(
        side=tk.LEFT,
        padx=10
    )

    # =====================================================
    # TABLE SELECTION
    # =====================================================

    category_table.bind(
        "<ButtonRelease-1>",
        select_category
    )

    # =====================================================
    # LOAD DATABASE DATA
    # =====================================================

    load_categories()