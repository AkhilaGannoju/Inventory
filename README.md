# Inventory

# InvTrack - Inventory Management System

## Overview
InvTrack is a Python-based Inventory Management System that allows users to efficiently manage store or warehouse inventory. It provides a user-friendly GUI built with Tkinter and an SQLite database for data storage.

## Features
- **Add Products**: Add new products with name, category, price, and quantity.
- **View Inventory**: Display all products in an interactive table.
- **Delete Products**: Remove selected products from the database.
- **Data Persistence**: Stores inventory data in an SQLite database.

## Technologies Used
- **Python** (for core functionality)
- **Tkinter** (for GUI)
- **SQLite** (for database management)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/InvTrack.git
   ```
2. Navigate to the project directory:
   ```sh
   cd InvTrack
   ```
3. Install required dependencies:
   ```sh
   pip install tk
   ```
4. Run the application:
   ```sh
   python invtrack.py
   ```

## Usage
- Open the application.
- Enter product details and click "Add Product" to add items to the inventory.
- Click on a product and press "Delete Selected" to remove it.
- View all inventory items in the displayed table.

## Database Structure
The application uses an SQLite database (`inventory.db`) with the following schema:
```sql
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL CHECK(price >= 0),
    quantity INTEGER NOT NULL CHECK(quantity >= 0)
);
```

## Future Enhancements
- Implement product editing functionality.
- Add search and filtering options.
- Generate sales and stock reports.

## License
This project is open-source and available under the [MIT License](LICENSE).

