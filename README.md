# 🏢 FIFTH Property Management System (PMS)

This is a backend API built with **Django** and **MySQL** for managing properties, contacts (landlords and tenants), and leases. It includes structured REST endpoints, a dashboard summary view, and auto-generated API documentation.

---

## 🚀 Features

- Create and manage **landlords**, **tenants**, **units**, and **leases**
- Dashboard analytics for total units, rent income, and ownership breakdown
- API filtering, nested serializers, and linked relationships
- Auto-generated Swagger documentation
- Postman collection for quick testing
- Test data seeding command

---

## 🧱 Tech Stack

- **Backend**: Python, Django, Django REST Framework
- **Database**: MySQL
- **API Docs**: Swagger (via `drf-yasg`)
- **Dev Tools**: Postman, Git, `.env` configuration

---

## ⚙️ Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/pms-backend.git
cd pms-backend
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment
```bash
DB_NAME=pms_db
DB_USER=root
DB_PASSWORD=yourpassword
DB_HOST=127.0.0.1
DB_PORT=3306
SECRET_KEY=your-secret-key
DEBUG=True
```

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (optional)
```bash
python manage.py createsuperuser
```

### 7. Seed Test Data
```bash
python manage.py seed_test_data
```

### 8. Start the Server
```bash
python manage.py runserver
```

---

## 📬 API Endpoints

### Contacts

| Method | Endpoint              | Description                          |
|--------|-----------------------|--------------------------------------|
| GET    | `/contacts/`          | List all contacts                    |
| GET    | `/contacts/?type=landlord` | Filter contacts by type          |
| POST   | `/contacts/`          | Create landlord or tenant            |
| PUT    | `/contacts/<id>/`     | Update contact                       |
| DELETE | `/contacts/<id>/`     | Delete contact                       |

### 🏢 Units

| Method | Endpoint              | Description                          |
|--------|-----------------------|--------------------------------------|
| GET    | `/units/`             | List all units                       |
| POST   | `/units/`             | Add new unit (linked to landlord)    |
| PUT    | `/units/<id>/`        | Update unit                          |
| DELETE | `/units/<id>/`        | Delete unit                          |

### 📄 Leases

| Method | Endpoint              | Description                          |
|--------|-----------------------|--------------------------------------|
| GET    | `/leases/`            | List all leases                      |
| POST   | `/leases/`            | Create a lease with unit + contacts  |
| PUT    | `/leases/<id>/`       | Update lease                         |
| DELETE | `/leases/<id>/`       | Delete lease                         |

### 📊 Dashboard & Index

| Method | Endpoint              | Description                          |
|--------|-----------------------|--------------------------------------|
| GET    | `/dashboard/`         | View total units, rent summary, etc. |
| GET    | `/index/`             | View linked lease-tenant-landlord    |

---

## 📚 API Documentation

* **Swagger UI**: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

---

## 🗺️ ERD Diagram

This is the visual representation of the data model:

![ERD Diagram](docs/erd.png)
