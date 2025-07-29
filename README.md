# 🧑‍💻 Full Stack Developer Portfolio – Built with Django

A personal developer portfolio website built using **Django**, where you can showcase your work, highlight your skills, and manage everything from an admin dashboard. Designed to be professional, customizable, and fully functional for real-world use.

---
## 🚀 Features

- 🎯 Fully responsive design
- 🗂 Add/edit/delete your projects from the Django Admin
- 📁 Upload project images and links (GitHub, live demo)
- 🧠 Skills section with rating bars
- 🧾 Resume/CV section
- 📇 Contact form (basic)
- 🔍 Clean UI with Bootstrap
- 💾 SQLite or PostgreSQL database support

---

## 🛠 Tech Stack

| Tech               | Description                     |
|--------------------|---------------------------------|
| 🐍 Django           | Backend Framework               |
| 🧰 HTML, CSS, JS    | Frontend                        |
| 🎨 Bootstrap        | Styling & Layout                |
| ☁️ Cloudinary       | Image Hosting                   |
| 📦 SQLite / Postgres | Database                        |
| ⚙️ Django Admin     | Admin management of content     |
| 🚀 Render / Railway | Deployment                      |

---

## 📥 Installation Instructions

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/portfolio-django.git

# 2. Create a virtual environment
python -m venv env

# 3. Activate the virtual environment
# Windows:
env\Scripts\activate
# macOS/Linux:
source env/bin/activate

# 4. Install required packages
pip install -r requirements.txt

# 5. Run migrations
python manage.py migrate

# 6. Create superuser for admin access
python manage.py createsuperuser

# 7. Run the development server
python manage.py runserver
