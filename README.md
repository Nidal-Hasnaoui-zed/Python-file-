# 📚 Simple Library Management System (Console-Based)

Welcome to the **Library Management System**, a console-based Python application designed to help you practice **Object-Oriented Programming (OOP)** and **CRUD** operations using only in-memory storage (lists) — no database required.

## 🎯 Project Goal

This project helps you master core Python backend logic by building a mini-library system that manages **books** and **users**. It uses OOP principles, supports CRUD operations, and stores all data in lists for simplicity and clarity.

## 🛠️ Features

### 📚 Books Management
- **Create Book**: Add a new book with title, author, and quantity.
- **Read Books**: View a list of all available books.
- **Update Book**: Edit the title, author, or quantity of a book.
- **Delete Book**: Remove a book from the system.

### 👤 User (Borrower) Management
- **Create User**: Add a new library member with name and ID.
- **Borrow Book**: Reduce book quantity when a user borrows it, and log the borrowing user.
- **Return Book**: Increase book quantity and remove the user from the borrowed list.

## 💡 Technologies Used

- Python 3.x
- OOP (Classes, Methods)
- In-memory data storage using `list` and `dict`

## 📁 Project Structure

```bash
library_management/
├── main.py               # Entry point to run the system
├── book.py               # Book class definition and related methods
├── user.py               # User (borrower) class definition and methods
├── library.py            # Core logic to manage books and users
└── README.md             # Project documentation

