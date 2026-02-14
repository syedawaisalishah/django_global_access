# 📦 django-global-access

Make your Django development server accessible from anywhere with zero configuration.

`django-global-access` automatically configures your Django project to allow external access by handling `ALLOWED_HOSTS` and simplifying global exposure during development.

---

## 🚀 Why This Package?

By default, Django runs on:

```
http://127.0.0.1:8000
```

Which is only accessible locally.

To access from another device (same network or public IP), you normally need:

```bash
python manage.py runserver 0.0.0.0:8000
```

And update:

```python
ALLOWED_HOSTS = ['*']
```

Many beginners forget this step.

This package solves that automatically.

---

## ✨ Features

* ✅ Automatically sets `ALLOWED_HOSTS = ['*']` if empty
* ✅ Allows external access without manual configuration
* ✅ Simple installation
* ✅ Lightweight
* ✅ Works with Django 3.2+

---

## 📥 Installation

```bash
pip install django-global-access
```

---

## ⚙️ Setup

### 1️⃣ Add to `INSTALLED_APPS`

```python
INSTALLED_APPS = [
    ...
    'django_global_access',
]
```

---

### 2️⃣ Add Middleware

```python
MIDDLEWARE = [
    ...
    'django_global_access.middleware.GlobalAccessMiddleware',
]
```

---

## ▶️ Usage

Run your Django server globally:

```bash
python manage.py runserver 0.0.0.0:8000
```

Now your app will be accessible via:

```
http://YOUR_LOCAL_IP:8000
```

Example:

```
http://192.168.1.10:8000
```

---

## 🌍 Access From Public Internet

To access from anywhere in the world:

1. Open port 8000 on your router
2. Use your public IP
3. Ensure firewall allows the port

You can get your public IP from:

```
https://api.ipify.org
```

Then access:

```
http://YOUR_PUBLIC_IP:8000
```

⚠️ **Warning:** This is intended for development use only.

---

## 🛡 Production Deployment (Recommended)

For production environments, do NOT use `runserver`.

Instead use:

* Gunicorn
* Nginx
* Docker
* Cloud VM services such as:

  * Amazon Web Services
  * Microsoft Azure
  * Google Cloud Platform

---

## 🧪 Example Project Structure

```
myproject/
│
├── manage.py
├── myproject/
│   ├── settings.py
│
└── django_global_access/
```

---

## 🔥 Advanced Usage (Optional Command)

If installed with management command support:

```bash
python manage.py expose
```

This will automatically run:

```bash
runserver 0.0.0.0:8000
```

---

## 🧠 How It Works

The middleware checks:

```python
if not settings.ALLOWED_HOSTS:
    settings.ALLOWED_HOSTS = ['*']
```

It modifies settings at runtime to prevent host restriction errors.

---

## ⚠️ Security Notice

This package is designed for:

* Development
* Testing
* Internal network demos

It is NOT recommended for production use without proper security configuration.

---

## 📄 License

MIT License

---

## 👨‍💻 Author

Syed Awais Ali Shah

