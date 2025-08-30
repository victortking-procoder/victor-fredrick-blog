# 📌 My Portfolio & Blog Backend

A **Django REST Framework (DRF)** powered backend for managing **portfolio projects, blog posts, and contact messages**. Built as a graduation project with clean REST APIs, token authentication, and deployed on **Render**.

---

## 🚀 Features

### Portfolio API

* List all projects
* Retrieve project details
* Admin-authenticated: create, update, delete

### Blog API

* List posts with pagination, search, filtering by tags/categories
* Retrieve post details
* Admin-authenticated: create, update, delete
* Markdown rendering (`content_html`)

### Contact API

* Public: submit a message
* Admin: view, mark as read, or delete messages

### Authentication

* Token-based authentication
* Login & logout endpoints
* Admin-only access for protected routes

---

## 🛠️ Tech Stack

* **Backend**: Django + Django REST Framework
* **Database**: PostgreSQL (Render free tier Postgres)
* **Auth**: DRF Token Authentication
* **Static**: WhiteNoise for static file serving
* **Email**: SMTP (Zoho Mail)
* **Deployment**: Render (Web Service + Postgres DB)

---

## 📂 Project Structure

```
victor_fredrick/
├── blog/         # Blog app
├── portfolio/    # Portfolio app
├── contact/      # Contact form app
├── users/        # Authentication
├── config/       # Django project settings
├── manage.py
├── build.sh      # Render build script
├── render.yaml   # Render deployment config
└── requirements.txt
```

---

## 🔑 API Endpoints

### Auth

* `POST /api/auth/login/` → Get token
* `POST /api/auth/logout/` → Invalidate token

### Portfolio

* `GET /api/portfolio/projects/`
* `GET /api/portfolio/projects/<slug>/`
* `POST /api/portfolio/projects/` (admin)
* `PUT/PATCH/DELETE /api/portfolio/projects/<slug>/` (admin)

### Blog

* `GET /api/blog/posts/?search=django`
* `GET /api/blog/posts/<slug>/`
* `POST /api/blog/posts/` (admin)
* `PUT/PATCH/DELETE /api/blog/posts/<slug>/` (admin)
* `GET /api/blog/categories/`
* `GET /api/blog/tags/`

### Contact

* `POST /api/contact/contact/` (public)
* `GET /api/contact/messages/` (admin)
* `GET /api/contact/messages/<id>/` (admin)
* `PATCH /api/contact/messages/<id>/` (mark as read, admin)
* `DELETE /api/contact/messages/<id>/` (admin)

✍️ Developed as a backend graduation project — built with ❤️ using Django & DRF, deployed on **Render**