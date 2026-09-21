
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import pymysql

from database import connect_database
from employee import employee_form
from category2 import category_form
from product2 import product_form
from suppliers import supplier_form


# =========================
# Dashboard Counts
# =========================

def get_dashboard_counts():

    connection = connect_database()

    if connection is None:
        return 0, 0, 0, 0

    try:

        cursor = connection.cursor()

        # Total Employees
        cursor.execute("SELECT COUNT(*) FROM employees")
        total_employee = cursor.fetchone()[0]

        # Total Suppliers
        cursor.execute("SELECT COUNT(*) FROM suppliers")
        total_supplier = cursor.fetchone()[0]

        # Total Categories
        cursor.execute("SELECT COUNT(*) FROM categories")
        total_category = cursor.fetchone()[0]

        # Total Products
        cursor.execute("SELECT COUNT(*) FROM products")
        total_product = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        return total_employee, total_supplier, total_category, total_product

    except pymysql.Error as error:

        messagebox.showerror(
            "Database Error",
            str(error)
        )

        if connection:
            connection.close()

        return 0, 0, 0, 0


# =========================
# Main Window
# =========================

window = tk.Tk()

window.title("Inventory Management System")
window.geometry("1200x700")
window.state("zoomed")
window.configure(bg="#f2f2f2")


# =========================
# Message Function
# =========================

def show_message(name):
    messagebox.showinfo(
        "Information",
        f"{name} Page Opened"
    )


# =========================
# Logout Function
# =========================

def logout():

    result = messagebox.askyesno(
        "Logout",
        "Do you want to logout?"
    )

    if result:
        window.destroy()


# =========================
# Dashboard
# =========================

def show_dashboard():

    # Clear old page
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Get actual counts from MySQL
    total_employee, total_supplier, total_category, total_product = get_dashboard_counts()

    # Dashboard Frame
    dashboard_frame = tk.Frame(
        content_frame,
        bg="#bc8383"
    )
    dashboard_frame.pack(
        fill="both",
        expand=True
    )

    # =========================
    # Dashboard Title
    # =========================

    title_label = tk.Label(
        dashboard_frame,
        text="Dashboard",
        font=("Arial", 24, "bold"),
        bg="#5fbed8",
        fg="#101b4d"
    )
    title_label.pack(
        pady=(30, 20)
    )

    # =========================
    # Cards Frame
    # =========================

    cards_frame = tk.Frame(
        dashboard_frame,
        bg="#bc8383"
    )
    cards_frame.pack(
        pady=20
    )

    # =========================
    # Create Card Function
    # =========================

    def create_card(title, value, color):

        card = tk.Frame(
            cards_frame,
            bg=color,
            width=230,
            height=130
        )

        card.pack(
            side="left",
            padx=15
        )

        card.pack_propagate(False)

        title_label = tk.Label(
            card,
            text=title,
            font=("Arial", 16, "bold"),
            bg=color,
            fg="white"
        )

        title_label.pack(
            pady=(20, 5)
        )

        value_label = tk.Label(
            card,
            text=str(value),
            font=("Arial", 28, "bold"),
            bg=color,
            fg="white"
        )

        value_label.pack()


    # =========================
    # Dashboard Cards
    # =========================

    create_card(
        "Total Employee",
        total_employee,
        "#3498c5"
    )

    create_card(
        "Total Supplier",
        total_supplier,
        "#ff5a18"
    )

    create_card(
        "Total Category",
        total_category,
        "#197b7d"
    )

    create_card(
        "Total Product",
        total_product,
        "#607987"
    )

# =========================
# Header
# =========================

header_frame = tk.Frame(
    window,
    bg="#101b4d",
    height=70
)

header_frame.pack(
    fill="x"
)

header_frame.pack_propagate(False)


# Logo
logo_label = tk.Label(
    header_frame,
    text="🛒",
    font=("Arial", 30),
    bg="#101b4d",
    fg="white"
)

logo_label.pack(
    side="left",
    padx=(20, 10)
)


# Title
title_label = tk.Label(
    header_frame,
    text="Inventory Management System",
    font=("Arial", 22, "bold"),
    bg="#101b4d",
    fg="white"
)

title_label.pack(
    side="left"
)


# Logout Button
logout_button = tk.Button(
    header_frame,
    text="Logout",
    font=("Arial", 11, "bold"),
    bg="#e74c3c",
    fg="white",
    width=10,
    cursor="hand2",
    command=logout
)

logout_button.pack(
    side="right",
    padx=20
)


# =========================
# Information Bar
# =========================

info_frame = tk.Frame(
    window,
    bg="#455c68",
    height=45
)

info_frame.pack(
    fill="x"
)

info_frame.pack_propagate(False)


# Welcome Text
welcome_label = tk.Label(
    info_frame,
    text="Welcome to Inventory Management System",
    font=("Arial", 11, "bold"),
    bg="#455c68",
    fg="white"
)

welcome_label.pack(
    side="left",
    padx=20
)


# Date Label
date_label = tk.Label(
    info_frame,
    text=datetime.now().strftime("%d-%m-%Y"),
    font=("Arial", 11),
    bg="#455c68",
    fg="white"
)

date_label.pack(
    side="right",
    padx=20
)


# Time Label
time_label = tk.Label(
    info_frame,
    font=("Arial", 11),
    bg="#455c68",
    fg="white"
)

time_label.pack(
    side="right",
    padx=10
)


# =========================
# Update Time
# =========================

def update_time():

    current_time = datetime.now().strftime("%I:%M:%S %p")

    time_label.config(
        text=current_time
    )

    window.after(
        1000,
        update_time
    )


update_time()


# =========================
# Main Body
# =========================

body_frame = tk.Frame(
    window,
    bg="#f2f2f2"
)

body_frame.pack(
    fill="both",
    expand=True
)


# =========================
# Left Menu
# =========================

menu_frame = tk.Frame(
    body_frame,
    bg="#eeeeee",
    width=200
)

menu_frame.pack(
    side="left",
    fill="y"
)

menu_frame.pack_propagate(False)


# Menu Title
menu_title = tk.Label(
    menu_frame,
    text="MENU",
    font=("Arial", 16, "bold"),
    bg="#dc4848",
    fg="#101b4d"
)

menu_title.pack(
    pady=(25, 15)
)

# =========================
# Menu Button Function
# =========================

def create_menu_button(text, command):

    button = tk.Button(
        menu_frame,
        text=text,
        font=("Arial", 11, "bold"),
        bg="#ffffff",
        fg="#101b4d",
        relief="flat",
        cursor="hand2",
        anchor="w",
        padx=20,
        height=2,
        command=command
    )

    button.pack(
        fill="x",
        padx=10,
        pady=4
    )

    return button


# =========================
# Menu Buttons
# =========================

create_menu_button(
    "Employee",
    lambda: employee_form(
        content_frame,
        show_dashboard
    )
)

create_menu_button(
    "Supplier",
    lambda: supplier_form(
        content_frame,
        show_dashboard
    )
)

create_menu_button(
    "Category",
    lambda: category_form(
        content_frame,
        show_dashboard
    )
)

create_menu_button(
    "Products",
    lambda: product_form(
        content_frame,
        show_dashboard
    )
)


create_menu_button(
    "Exit",
    logout
)


# =========================
# Content Frame
# =========================

content_frame = tk.Frame(
    body_frame,
    bg="#bc8383"
)

content_frame.pack(
    side="left",
    fill="both",
    expand=True
)


# =========================
# Footer
# =========================

footer_frame = tk.Frame(
    window,
    bg="#101b4d",
    height=35
)

footer_frame.pack(
    fill="x"
)

footer_frame.pack_propagate(False)


footer_label = tk.Label(
    footer_frame,
    text="IMS-Inventory Management System | Developed By zaid rasool",
    font=("Arial", 10),
    bg="#101b4d",
    fg="white"
)

footer_label.pack(
    pady=8
)


# =========================
# Show Dashboard
# =========================

show_dashboard()


# =========================
# Run Application
# =========================

window.mainloop()
