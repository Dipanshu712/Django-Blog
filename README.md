
# 📝 Role-Based Blog Management System (Django + DRF)

A **production-style Django web application** implementing a **Role-Based Access Control (RBAC)** system with custom dashboards, blogs, categories, users, comments, search, and **REST APIs using Django REST Framework (DRF)**.
Designed using **real-world backend patterns** commonly used in scalable content management systems.

**Live App:** [https://dipansu712.pythonanywhere.com/](https://dipansu712.pythonanywhere.com/)

---

## 🚀 Key Features

### 🔐 Authentication & Authorization

* Secure user authentication using Django Auth
* **Role-Based Access Control (RBAC)** using Django Groups
* Supported roles:

  * **Admin (Superuser)** – full system access
  * **Manager** – manage blogs, categories, users
  * **Editor** – manage own blogs & categories
* Permission checks enforced at both **UI and backend levels**

---

### 📊 Custom Admin Dashboard

* Custom dashboard (not Django Admin)
* Role-based sidebar visibility
* Permission-aware UI rendering
* Real-time statistics:

  * Total Blogs
  * Total Categories
  * Total Users (Admin & Manager only)

---

### 📰 Blog Management

* Create, edit, delete blogs (CRUD)
* Blog workflow:

  * Draft
  * Published
* Featured blogs support
* Image upload handling
* Author & category assignment
* Status-based content visibility

---

### 🔍 Search & Filtering

* Keyword-based blog search
* Search across:

  * Blog title
  * Content
  * Category
* Case-insensitive querying
* Integrated into listing UI
* Optimized using **Django ORM filters & querysets**
  👉 Mimics **real CMS & admin panel search functionality**

---

### 🗂 Category Management

* Permission-protected CRUD for categories
* Relational integrity with blogs
* Role-based access enforcement

---

### 👥 User Management

* Create users from dashboard
* Assign roles (Manager / Editor)
* Delete users (except superuser)
* Role badges for clarity in UI
* RBAC enforced at API and view level

---

### 💬 Comments System

* Blog-linked comments
* User-linked comments
* Nested replies (parent-child structure)
* Role-based deletion permissions
* Moderation-ready comment workflow

---

### 🔌 REST APIs (Django REST Framework)

* Designed **RESTful APIs** for:

  * Blogs
  * Categories
  * Comments
  * Authentication (login/register)
* Token-based authentication for API access
* API-first backend architecture (frontend-agnostic)
* APIs tested using **Postman/Thunder Client**
* Backend is **Flutter / React ready**

---

## 🧠 Role Permissions Matrix

| Role    | Blogs | Categories | Search | Users |
| ------- | ----- | ---------- | ------ | ----- |
| Admin   | ✅     | ✅          | ✅      | ✅     |
| Manager | ✅     | ✅          | ✅      | ✅     |
| Editor  | ✅     | ✅          | ✅      | ❌     |

---

## 🛠 Tech Stack

* **Backend:** Django, Django REST Framework (DRF)
* **Frontend:** HTML, CSS
* **Database:** SQLite (development)
* **Auth:** Django Auth + Groups
* **Search:** Django ORM filtering
* **Tools:** Git, GitHub, Postman

---

## 📁 Project Structure

```bash
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
│   ├── api_views.py
│   ├── serializers.py
│   └── templates/
│
├── templates/
│   └── base.html
│
├── static/
├── manage.py
└── README.md
```

---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/your-username/role-based-blog-django.git
cd role-based-blog-django
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 👥 Required Groups

Create the following groups in Django Admin:

```text
Manager  
Editor  
```

⚠️ Group names are **case-sensitive**

---

## 📈 Project Level

* **Complexity:** Intermediate → Advanced
* **Experience Equivalent:** ~1.5–2 years Django backend exposure
* **Interview Ready:** ✅ Yes
* **Production Patterns Used:** RBAC, API-first design, modular apps

---

## 🎯 What This Project Demonstrates

* Role-Based Access Control (RBAC)
* Secure authentication & authorization
* REST API design with DRF
* Custom dashboard architecture
* Search & filtering logic
* Permission enforcement & debugging
* Clean separation of concerns (HTML views vs APIs)

---

## 🔮 Future Enhancements

* Pagination & caching
* AJAX-based live search
* JWT authentication
* Redis caching
* Dockerization
* Unit tests & permission tests
* Production deployment (Gunicorn + Nginx + AWS)

---

## 👨‍💻 Author

**Dipanshu Mishra**
Python Backend Developer | Django & DRF
GitHub: [https://github.com/Dipanshu712](https://github.com/Dipanshu712)

---


