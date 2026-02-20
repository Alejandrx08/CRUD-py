![Animation](https://github.com/user-attachments/assets/17b59f0d-1c93-4c15-a1b6-b6a311b21ecf)

# CRUD-Py

![Python](https://img.shields.io/badge/Python-3.x-blue)
![SQLite](https://img.shields.io/badge/SQLite-Database-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![Security](https://img.shields.io/badge/Auth-bcrypt-orange)

A modular CRUD (Create, Read, Update, Delete) system built with **Python + SQLite**, featuring secure authentication using **bcrypt hashing** and role-based access control.

This project demonstrates backend fundamentals including database management, authentication, security practices, and modular architecture.

---

## Key Features

* User registration
* Login authentication system
* Secure password hashing (bcrypt)
* Role-based access (admin / user)
* User activation / deactivation
* Full CRUD operations
* Modular project structure
* Database seeding for testing

---

## Tech Stack

* Python 3.x
* SQLite3
* bcrypt
* Virtualenv
* Git / GitHub

---

## Project Structure

```
CRUD/
│
├── src/
│   └── crud_py/
│       ├── __init__.py
│       ├── app.py          # Main CLI application
│       ├── db.py           # Database connection & initialization
│       ├── security.py     # Password hashing & verification
│       ├── seed.py         # Generate sample users
│       └── users_repo.py   # CRUD operations
│
├── schema/                 # SQL schema
├── app.db                  # SQLite database
├── requirements.txt        # Dependencies
├── run.py                  # Entry point
└── .gitignore
```

---

## Database Schema

```
CREATE TABLE IF NOT EXISTS usuarios(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT NOT NULL,
  apellido TEXT NOT NULL,
  correo TEXT NOT NULL UNIQUE,
  password TEXT NOT NULL,
  rango TEXT NOT NULL,
  tipo TEXT,
  activo INTEGER NOT NULL DEFAULT 1
);
```

---

## Installation

Clone the repository:

```
git clone https://github.com/Alejandrx08/CRUD-py.git
cd CRUD
```

Create a virtual environment (recommended):

```
python -m venv .venv
```

Activate the environment (Windows):

```
.venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the project:

```
python run.py
```

---

## Seeding Sample Data

Generate test users with different roles and hashed passwords:

```
python -m src.crud_py.seed
```

---

## Roles

**Admin**

* List users
* Update users
* Delete users
* Full system control

**User**

* Limited access

---

## Security

* Passwords are hashed using bcrypt
* No plaintext password storage
* Basic role-based authorization
* Input validation on login

---

## Future Roadmap

* Web version (Flask / FastAPI)
* REST API
* Audit logs
* Docker support

---

## Learning Goals

This project was built to practice:

* CRUD design patterns
* Authentication systems
* Password security (hashing)
* Database modeling
* Modular architecture
* Error handling
* Role-based authorization

---

## Author

Alejandro Ibarra
Systems Engineering Student

Focused on backend development, security, and system architecture.
