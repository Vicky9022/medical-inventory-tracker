# Medical Inventory Tracker

**One‑line:** A small web app to manage medical store inventory — FastAPI backend (Tortoise ORM + PostgreSQL) with a simple static HTML/CSS frontend.

---

## What this repo contains (quick)

* `backend/` – Python FastAPI application (uses Tortoise ORM, Pydantic models). Entry: `backend/main.py`.
* `frontend/` – Static HTML/CSS (simple client views under `frontend/Mini Project - Copy/`).

I inspected the uploaded code and verified the backend expects a PostgreSQL database named `medical_inventory_tracker` (see `backend/database.py`).

---

## Tech stack

* **Backend:** Python 3.x, FastAPI, Uvicorn, Tortoise ORM, Pydantic (pydantic-settings). Database: PostgreSQL (async driver `asyncpg`).
* **Frontend:** Plain HTML/CSS/vanilla JS (static files).

---

## Project structure

```
medical-inventory-tracker/
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── config.py
│   ├── core/models/
│   ├── core/schemas/
│   └── routers/
├── frontend/
│   └── Mini Project - Copy/
│       ├── index.html
│       ├── customer.html
│       ├── *.css
│       └── ...
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## Quickstart (local)

> These steps assume you have Python 3.9+ and PostgreSQL installed.

### 1) Clone repo & enter folder

```bash
git clone https://github.com/your-username/medical-inventory-tracker.git
cd medical-inventory-tracker
```

### 2) Python virtual environment & dependencies

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

pip install --upgrade pip
pip install -r requirements.txt
```

### 3) Configure environment variables

Copy `.env.example` → `.env` and update values:

```ini
# backend/.env.example
DB_USER=your_db_user
DB_PASSWORD=your_db_password
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
EXPIRE_AFTER_DAYS=1
```

⚠️ **Never commit `.env` to GitHub**.

### 4) Create database (Postgres)

```sql
-- login to postgres shell (psql)
CREATE DATABASE medical_inventory_tracker;
CREATE USER myuser WITH PASSWORD 'mypassword';
GRANT ALL PRIVILEGES ON DATABASE medical_inventory_tracker TO myuser;
```

### 5) Run the backend

```bash
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Open [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger UI.

### 6) Open the frontend

Static HTML — open in browser or serve locally:

```bash
cd frontend
python -m http.server 5500
# open http://localhost:5500/Mini%20Project%20-%20Copy/index.html
```

---

## Backend endpoints (examples)

* `GET /` — returns `{ "message": "Hello world!" }`
* `POST /medicine` — create a medicine entry
* `PUT /medicine` — update medicine quantity
* `GET /medicine?name=<name>` — search medicine by name
* `POST /store/signup` — register a new store
* `POST /store/verify` — verify store owner
* `GET /store/medicine?store_id=<id>` — fetch store medicines

---

## Files added for production readiness

### `requirements.txt`

```
fastapi
uvicorn
tortoise-orm
pydantic
pydantic-settings
python-dotenv
asyncpg
starlette
```

### `.gitignore`

```
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.venv/
venv/

# Node
node_modules/

# Env
*.env
backend/.env
frontend/.env

# Editor/OS
.vscode/
.idea/
.DS_Store
Thumbs.db
```

### `.env.example`

```
DB_USER=postgres
DB_PASSWORD=changeme
SECRET_KEY=changeme
ALGORITHM=HS256
EXPIRE_AFTER_DAYS=1
```

---

## Security notes

* Rotate DB password & secret key if you ever committed `.env`.
* Never push `.env` or other secrets.

---

## License

MIT (recommended). Add a LICENSE file.

---

*End of README — ready to push & use*
