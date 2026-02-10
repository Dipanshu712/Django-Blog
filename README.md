

# 📝 Role-Based Blog Management System (Django)

A **professional Django web application** implementing a **role-based content management system (RBAC)** with custom dashboards, blogs, categories, users, comments, and search functionality.
Designed using real-world backend patterns used in production systems.

---
Live App - https://dipansu712.pythonanywhere.com/

## 🚀 Features

### 🔐 Authentication & Authorization

* Django authentication system
* Role-based access control (RBAC)
* Roles:

  * **Admin (Superuser)** – full system access
  * **Manager** – blogs, categories, users
  * **Editor** – blogs & categories

---

### 📊 Custom Dashboard

* Custom dashboard (not Django Admin)
* Role-based sidebar visibility
* Permission-aware UI rendering
* Statistics:

  * Total Blogs
  * Total Categories
  * Total Users (Admin & Manager)

---

### 📰 Blog Management

* Create, edit, delete blogs
* Blog status:

  * Draft
  * Published
* Featured blogs
* Image upload support
* Author & category assignment

---

### 🔍 Blog Search & Filtering

* Keyword-based blog search
* Search by:

  * Blog title
  * Content
  * Category
* Case-insensitive querying
* Integrated into blog listing UI
* Optimized using Django ORM filters

👉 This mimics **real CMS & admin panels**

---

### 🗂 Category Management

* Add, edit, delete categories
* Permission-protected CRUD operations
* Relational integrity with blogs

---

### 👥 User Management

* Add users from dashboard
* Assign roles (Manager / Editor)
* Delete users (except superuser)
* Role badges in UI

---

### 💬 Comments System

* Blog-linked comments
* User-linked comments
* Nested replies support
* Role-based deletion permissions
* Moderation-ready structure

---

## 🧠 Role Permissions Matrix

| Role    | Blogs | Categories | Search | Users |
| ------- | ----- | ---------- | ------ | ----- |
| Admin   | ✅     | ✅          | ✅      | ✅     |
| Manager | ✅     | ✅          | ✅      | ✅     |
| Editor  | ✅     | ✅          | ✅      | ❌     |

---

## 🛠 Tech Stack

* **Backend**: Django (Python)
* **Frontend**: HTML, CSS
* **Database**: SQLite (development)
* **Auth**: Django Auth + Groups
* **Search**: Django ORM filtering

---

## 📁 Project Structure

```
project/
│
├── dashboard/
│   ├── views.py
│   ├── urls.py
│   └── templates/dashboard/
│
├── blog/
│   ├── models.py
│   ├── views.py
│   └── templates/
│
├── templates/
│   └── base.html
│
├── static/
│
├── manage.py
└── README.md
```

---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/your-username/role-based-blog-django.git
cd role-based-blog-django
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 👥 Required Groups

Create these groups in Django Admin:

```
Manager
Editor
```

⚠️ Group names are **case-sensitive**

---

## 📈 Project Level

* **Complexity**: Intermediate → Advanced
* **Experience Equivalent**: ~2–2.5 years Django backend
* **Interview Ready**: ✅ Yes

---

## 🎯 What This Project Demonstrates

* Role-based access control (RBAC)
* Custom dashboard architecture
* Secure CRUD operations
* Search & filtering logic
* Permission debugging & enforcement
* Clean separation of concerns

---

## 🔮 Future Improvements

* AJAX-based search
* Pagination
* REST API (DRF)
* Deployment (Gunicorn + Nginx)
* Unit & permission tests

---

## 👨‍💻 Author

Dipanshu Mishra
Django Backend Developer


