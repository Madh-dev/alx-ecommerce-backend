# 📦 E-Commerce Backend — Django, PostgreSQL & JWT

A production-ready **e-commerce backend** built to simulate real-world development. This project focuses on **scalability**, **security**, **database performance**, and **clean API design**, following the structure and expectations described in the concept document.

---

## 📘 Table of Contents

* [Project Overview](#project-overview)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Database Schema](#database-schema)
* [API Documentation](#api-documentation)
* [Authentication (JWT Flow)](#authentication-jwt-flow)
* [Endpoints Overview](#endpoints-overview)
* [Setup Instructions](#setup-instructions)
* [Environment Variables](#environment-variables)
* [Git Commit Workflow](#git-commit-workflow)
* [Evaluation Criteria](#evaluation-criteria)
* [Future Improvements](#future-improvements)

---

## 🔍 Project Overview

This project implements a backend system for an **e-commerce product catalog**, enabling:

* Management of **products**, **categories**, and **users**
* Secure **JWT authentication**
* Advanced **filtering**, **sorting**, and **pagination**
* Fully documented **API endpoints**
* A high-performance **PostgreSQL** database with indexing

This backend mirrors what is done in real company systems, making it ideal for portfolio and learning.

---

## 🚀 Features

### **1. CRUD Operations**

* Products
* Categories
* User accounts

### **2. Advanced API Functionality**

* Filter products by category, name, price
* Sort products by price or creation date
* Paginated product listing
* Keyword-based search

### **3. Security**

* JWT authentication (access + refresh token)
* Secure password hashing
* Rate-limit-ready structure

### **4. Developer Experience**

* Auto-generated Swagger documentation
* Meaningful error messages
* Clean modular architecture
* DRF Viewsets for maintainability

### **5. Performance Optimizations**

* Indexes on frequently queried fields
* Proper use of `select_related()` and `prefetch_related()`
* Optimized query structure

---

## 🛠 Technologies Used

| Layer           | Technology      |
| --------------- | --------------- |
| Backend         | Django, DRF     |
| Database        | PostgreSQL      |
| Authentication  | JWT (SimpleJWT) |
| Documentation   | Swagger / Redoc |
| Version Control | Git + GitHub    |

---

## 🧱 Database Schema

### **Tables**

* `User`
* `Category`
* `Product`

### **Relationships**

```
Category (1) ─── (∞) Product
```

### **Indexes**

| Column        | Reason                |
| ------------- | --------------------- |
| `price`       | Sorting               |
| `category_id` | Filtering             |
| `created_at`  | Ordering & pagination |
| `slug`        | Fast lookups          |

---

## 📚 API Documentation

Once the server is running, visit:

### **Swagger UI**

```
/swagger/
```

### **Redoc**

```
/redoc/
```

These interactive pages include:

* All API endpoints
* Query params (filter, sort, paginate)
* Response examples
* Authentication test tools

---

## 🔐 Authentication (JWT Flow)

1. User logs in
2. Server responds with:

   * `access_token`
   * `refresh_token`
3. Access token used for authorized requests
4. Refresh token obtains new access token when expired

---

## 🌐 Endpoints Overview

### **Auth**

| Method | Endpoint              | Description          |
| ------ | --------------------- | -------------------- |
| POST   | `/api/token/`         | Login + get tokens   |
| POST   | `/api/token/refresh/` | Refresh access token |

### **Categories**

| Method | Endpoint               | Description     |
| ------ | ---------------------- | --------------- |
| GET    | `/api/categories/`     | List categories |
| POST   | `/api/categories/`     | Create category |
| PUT    | `/api/categories/:id/` | Update category |
| DELETE | `/api/categories/:id/` | Delete category |

### **Products**

| Method | Endpoint             | Description                          |
| ------ | -------------------- | ------------------------------------ |
| GET    | `/api/products/`     | List products with filtering/sorting |
| POST   | `/api/products/`     | Create product                       |
| GET    | `/api/products/:id/` | Retrieve product                     |
| PUT    | `/api/products/:id/` | Update product                       |
| DELETE | `/api/products/:id/` | Delete product                       |

### **Query Examples**

Filter by category:

```
/api/products/?category=shoes
```

Sort by price (descending):

```
/api/products/?ordering=-price
```

Paginate:

```
/api/products/?page=2&page_size=10
```

Keyword search:

```
/api/products/?search=bag
```

---

## 🛠 Setup Instructions

### **1. Clone Repository**

```bash
git clone <your-repo-url>
cd ecommerce-backend
```

### **2. Create Virtual Environment**

```bash
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
```

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4. Configure PostgreSQL**

Create database:

```sql
CREATE DATABASE ecommerce_db;
```

### **5. Apply Migrations**

```bash
python manage.py migrate
```

### **6. Run Server**

```bash
python manage.py runserver
```

---

## 🔧 Environment Variables

Create a `.env` file:

```
SECRET_KEY=your_secret_here
DEBUG=True
DB_NAME=ecommerce_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

---

## 🧭 Git Commit Workflow

Follow this structured commit format:

```
feat: set up Django project with PostgreSQL
feat: implement user authentication with JWT
feat: add product APIs with filtering and pagination
feat: integrate Swagger documentation for API endpoints
perf: optimize database queries with indexing
docs: add API usage instructions in Swagger
refactor: improve serializer validation
fix: resolve pagination bug in product list
```

This shows:

* Progress tracking
* Clean version control
* Professional engineering practices

---

## 📝 Evaluation Criteria (Matches Concept Document)

### **1. Functionality**

✔ Complete CRUD
✔ Filters, sorting, pagination
✔ Authentication

### **2. Code Quality**

✔ Clean folder structure
✔ Well-documented functions
✔ Database indexing

### **3. User Experience**

✔ Beautiful API documentation
✔ Clear error messages

### **4. Version Control**

✔ Frequent commits
✔ Proper commit messages

---

## 🚀 Future Improvements

* Add cart & order system
* Implement user roles (admin, staff, customer)
* Add product reviews and ratings
* Add caching layer (Redis)
* Add Celery for background tasks

