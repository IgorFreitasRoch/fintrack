# FinTrack 💰

A personal finance management app built as a full stack learning project.
The goal is to track income, expenses, and monitor balance in a simple and secure way.

---

## Tech Stack

**Backend**
- Python 3.x
- FastAPI
- SQLAlchemy (ORM)
- Pydantic (validation)
- bcrypt (password hashing)
- JWT (authentication)

**Frontend**
- Semantic HTML5
- SCSS (compiled to CSS)
- ITCSS methodology (layered architecture)
- BEM naming convention (Block, Element, Modifier)
- Custom CSS framework (no external dependencies)
- Vanilla JavaScript

**Database**
- SQLite (local development)
- PostgreSQL (production)

**Documentation**
- Swagger UI — available at `/docs` when backend is running

---

## CSS Architecture

This project uses ITCSS + BEM to organize styles:

```
css/
├── 1-settings/   → design tokens and variables
├── 2-tools/      → mixins and SCSS functions
├── 3-generic/    → reset and normalize
├── 4-elements/   → base HTML elements, no classes
├── 5-objects/    → layout and structure
├── 6-components/ → buttons, cards, forms
└── 7-utilities/  → helper and utility classes
```

BEM naming:
- `.card`           → Block
- `.card__title`    → Element
- `.card--featured` → Modifier

---

## Folder Structure

```
fintrack/
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   ├── models/
│   │   └── services/
│   ├── tests/
│   ├── requirements.txt
│   └── main.py
├── frontend/
│   ├── assets/
│   │   ├── css/
│   │   └── js/
│   └── index.html
├── database/
│   └── migrations/
├── .env.example
├── .gitignore
└── README.md
```

---

## Features

- [ ] User authentication (register and login)
- [ ] Password hashing with bcrypt
- [ ] JWT authorization
- [ ] Expense and income tracking
- [ ] Recurring expenses with cron job
- [ ] Dashboard with current balance
- [ ] Automatic API documentation

---

## Getting Started

### Prerequisites
- Python 3.10+
- Node.js

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend

Open `frontend/index.html` directly in the browser.

### SCSS Compilation

```bash
sass --watch frontend/assets/css/main.scss:frontend/assets/css/main.css
```

---

## Environment Variables

Copy `.env.example`, rename it to `.env` and fill in your values:

```bash
cp .env.example .env
```

---

## API Documentation

With the backend running, visit:
```
http://localhost:8000/docs
```

---

## Author

Built with curiosity and coffee by Igor.