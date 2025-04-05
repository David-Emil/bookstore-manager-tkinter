# 📚 Book Store Management System (Python Tkinter)

A GUI-based Book Store Management System built with **Python Tkinter** and **SQLite3**, designed to streamline operations of a library or bookshop. It offers a centralized interface for managing customers, employees, and book inventory with user authentication and multi-frame navigation.

---

## ✨ Features

- 👤 **Login & Signup System**
  - Secure login with username/password
  - Registration form with validation

- 📚 **Book Inventory Management**
  - View and update book details (title, author, stock, price, etc.)
  - Instant book data fetch by title

- 👥 **Customer Management**
  - Add and manage customer info (name, contact, age, etc.)
  - Auto-save feature for new entries

- 🧑‍💼 **Employee Management**
  - View employee details in a structured table
  - Employee database (name, ID, salary, age)

- 💾 **Local Database (SQLite3)**
  - Three tables: Employees, Books, Customers
  - Real-time updates and persistent storage

- 🖼️ **Tkinter GUI**
  - Multi-frame navigation (Home, Books, Customers, Employees)
  - Clean, responsive layout

---

## 🛠️ Tech Stack

- Python 3.x
- Tkinter (GUI)
- SQLite3 (Database)

---

## 🚀 Getting Started

### 1. Clone the Repository

``bash
git clone https://github.com/yourusername/bookstore-manager-tkinter.git
cd bookstore-manager-tkinter
2. Install Python (if not installed)
Download Python from: https://www.python.org/downloads/

3. Run the Application
Make sure all .py files and the SQLite database file are in the same folder, then run:

bash
Copy
Edit
python main.py
Replace main.py with the actual main file name used to launch your GUI (like app.py or bookstore.py).

🧩 File Structure
bash
Copy
Edit
/bookstore-manager-tkinter/
│
├── main.py                  # Main GUI launcher
├── db/                      # SQLite DB file (or created on first run)
├── modules/                 # Separated frame logic (signup, login, customer, etc.)
├── assets/                  # Optional: logos, icons, etc.
└── README.md
🧪 Sample Users (Optional)
You can pre-insert users for testing:

Username	Password
admin	admin123
employee1	pass456
📈 Future Enhancements
Search/filter functionality for books/customers

PDF export of customer/employee reports

Integrated billing or checkout system

Switch to MySQL or PostgreSQL backend

🙌 Contributors
David Emil Sobhi (Leader)

📄 License
This project is developed for academic use. Feel free to fork and customize for learning or internal projects.

