# 🛒 E-Commerce REST API

A fully functional **E-Commerce REST API** built with **Python**, **Django**, and **Django REST Framework**.  
Supports JWT authentication, product management, order processing, reviews, and interactive API documentation via Swagger UI.

---

## 🔗 Live API Documentation

> Visit: `https://MoaazMuhammad.pythonanywhere.com/api/docs/`

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11 |
| Framework | Django 5.2 |
| API Layer | Django REST Framework |
| Authentication | JWT (SimpleJWT) |
| Filtering | django-filter |
| Documentation | drf-spectacular (Swagger UI) |
| Database | SQLite (development) |

---

## 📦 Features

- 🔐 **JWT Authentication** — Register, Login, Forgot/Reset Password
- 📦 **Product Management** — CRUD with category filtering and search
- ⭐ **Reviews & Ratings** — Authenticated users can review products
- 🛍️ **Order Management** — Create and track orders with status lifecycle (Processing → Shipped → Delivered)
- 💳 **Payment Modes** — COD / Card with payment status tracking (Paid / Unpaid)
- 📄 **Swagger Docs** — Full interactive API documentation

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/E-commerce-REST-API-with-Django-Framework-Python.git
cd E-commerce-REST-API-with-Django-Framework-Python/emarket
```

### 2. Install dependencies

```bash
pip install djangorestframework django-filter djangorestframework-simplejwt drf-spectacular django
```

### 3. Apply migrations

```bash
python manage.py migrate
```

### 4. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 5. Run the server

```bash
python manage.py runserver
```

### 6. Open Swagger UI

```
http://127.0.0.1:8000/api/docs/
```

---

## 📡 API Endpoints

### 🔐 Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/register/` | Register new user |
| POST | `/api/token/` | Login — returns JWT access & refresh token |
| GET | `/api/userinfo/` | Get current user info |
| PUT | `/api/userinfo/update/` | Update user profile |
| POST | `/api/forgot_password/` | Send password reset email |
| POST | `/api/reset_password/<token>` | Reset password using token |

### 📦 Products

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/products/` | List all products (with filtering) |
| GET | `/api/products/<id>/` | Get single product |
| POST | `/api/products/new` | Create product (auth required) |
| PUT | `/api/products/update/<id>/` | Update product |
| DELETE | `/api/products/delete/<id>/` | Delete product |

### ⭐ Reviews

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/<product_id>/reviews` | Add a review |
| DELETE | `/api/<product_id>/reviews/delete` | Delete a review |

### 🛍️ Orders

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/orders/new/` | Create new order |
| GET | `/api/orders/` | List all orders |
| GET | `/api/orders/<id>/` | Get single order |
| PUT | `/api/orders/<id>/process/` | Update order status |
| DELETE | `/api/orders/<id>/delete/` | Delete order |

---

## 🗂️ Project Structure

```
emarket/
├── account/          # User registration, auth, profile, password reset
├── product/          # Products, categories, reviews, filters
├── order/            # Orders, order items, payment & status tracking
├── utils/            # Custom error handlers (404, 500)
└── emarket/          # Project settings, root URLs
```

---

## 🔒 Authentication Guide

This API uses **Bearer JWT Tokens**.

1. Register via `POST /api/register/`
2. Login via `POST /api/token/` → copy the `access` token
3. In Swagger UI click **Authorize 🔒** → enter `Bearer <your_token>`
4. All protected endpoints are now accessible

---

## 📊 Data Models

### Product
- name, description, price, brand, category, ratings, stock

### Order
- shipping address (city, street, zip, country), total amount, payment mode (COD/Card), payment status (Paid/Unpaid), order status (Processing/Shipped/Delivered)

### Review
- product, user, rating (0–5), comment

---

## 👤 Author

**Muhammed Essa**  
[GitHub](https://github.com/muhammedessa) 

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
