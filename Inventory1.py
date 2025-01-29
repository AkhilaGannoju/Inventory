import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# Database setup
def init_db():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL CHECK(price >= 0),
            quantity INTEGER NOT NULL CHECK(quantity >= 0)
        )
    ''')
    conn.commit()
    conn.close()

# Add product function
def add_product():
    name = name_entry.get()
    category = category_entry.get()
    try:
        price = float(price_entry.get())
        quantity = int(quantity_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Price and Quantity must be numeric.")
        return
    
    if name and category:
        conn = sqlite3.connect("inventory.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (name, category, price, quantity) VALUES (?, ? , ? , ? )",
                       (name, category, price, quantity))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Product added successfully.")
        refresh_inventory()
    else:
        messagebox.showerror("Missing Information", "Please fill in all fields.")

# Update inventory view
def refresh_inventory():
    for row in inventory_tree.get_children():
        inventory_tree.delete(row)
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    for row in cursor.fetchall():
        inventory_tree.insert("", "end", values=row)
    conn.close()

# Delete selected product
def delete_product():
    selected_item = inventory_tree.selection()
    if selected_item:
        product_id = inventory_tree.item(selected_item[0])['values'][0]
        conn = sqlite3.connect("inventory.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Product deleted successfully.")
        refresh_inventory()
    else:
        messagebox.showerror("Error", "No product selected.")

# GUI setup
root = tk.Tk()
root.title("Inventory Management System")

# Input fields
tk.Label(root, text="Product Name:").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Category:").grid(row=1, column=0, padx=10, pady=5)
category_entry = tk.Entry(root)
category_entry.grid(row=1, column=1)

tk.Label(root, text="Price:").grid(row=2, column=0, padx=10, pady=5)
price_entry = tk.Entry(root)
price_entry.grid(row=2, column=1)

tk.Label(root, text="Quantity:").grid(row=3, column=0, padx=10, pady=5)
quantity_entry = tk.Entry(root)
quantity_entry.grid(row=3, column=1)

# Buttons
tk.Button(root, text="Add Product", command=add_product).grid(row=4, column=0, padx=10, pady=10)
tk.Button(root, text="Delete Selected", command=delete_product).grid(row=4, column=1, padx=10, pady=10)

# Inventory view
inventory_tree = ttk.Treeview(root, columns=("ID", "Name", "Category", "Price", "Quantity"), show="headings")
inventory_tree.heading("ID", text="ID")
inventory_tree.heading("Name", text="Name")
inventory_tree.heading("Category", text="Category")
inventory_tree.heading("Price", text="Price")
inventory_tree.heading("Quantity", text="Quantity")
inventory_tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

init_db()
refresh_inventory()

root.mainloop()
