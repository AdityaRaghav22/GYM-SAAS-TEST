# Gym SaaS Application

## Overview
A gym management SaaS application built with Flask that allows gym owners to manage members, plans, memberships, and payments.

## Project Architecture
- **Framework**: Flask (Python 3.11)
- **Database**: PostgreSQL (Replit built-in) with SQLAlchemy ORM
- **Authentication**: JWT-based authentication with Flask-JWT-Extended (cookie-based)
- **Password Hashing**: Flask-Bcrypt
- **Migrations**: Flask-Migrate (Alembic)
- **Templates**: Jinja2 with Tailwind CSS (CDN)

## Project Structure
```
workspace/
├── gym_saas/
│   ├── app/
│   │   ├── __init__.py       # Flask app factory
│   │   ├── extensions.py     # SQLAlchemy, JWT, Bcrypt extensions
│   │   ├── models/           # Database models
│   │   │   ├── gym.py        # Gym model
│   │   │   ├── user.py       # User model (staff/owner)
│   │   │   ├── members.py    # Member model
│   │   │   ├── plan.py       # Subscription plans
│   │   │   ├── membership.py # Member subscriptions
│   │   │   └── payment.py    # Payment records
│   │   ├── routes/           # API endpoints & pages
│   │   │   ├── gym_auth.py   # Gym registration/login
│   │   │   ├── member.py     # Member CRUD
│   │   │   ├── plans.py      # Plan management
│   │   │   ├── membership.py # Membership management
│   │   │   ├── payment.py    # Payment tracking
│   │   │   ├── public.py     # Public landing page
│   │   │   ├── dashboard.py  # Dashboard
│   │   │   └── analytics.py  # Analytics
│   │   ├── services/         # Business logic
│   │   ├── templates/        # Jinja2 HTML templates
│   │   └── utils/            # Helper utilities
│   ├── migrations/           # Database migrations (Alembic)
│   ├── config.py             # Configuration settings
│   └── app.py                # Application entry point
├── wsgi.py                   # WSGI entry for production (gunicorn)
└── pyproject.toml            # Python dependencies
```

## Running the Application
- **Development**: Workflow "Start application" runs `python gym_saas/app.py` on port 5000
- **Production**: `gunicorn --bind 0.0.0.0:5000 wsgi:app`
- **PYTHONPATH**: Must include `/home/runner/workspace` so `gym_saas` package is importable
- **Migrations**: `FLASK_APP=wsgi.py python -m flask db upgrade --directory gym_saas/migrations`

## Environment Variables
- `DATABASE_URL` - PostgreSQL connection string (auto-configured by Replit)
- `SECRET_KEY` - Flask secret key
- `JWT_SECRET_KEY` - JWT authentication secret

## Recent Changes
- 2026-02-14: Initial Replit setup - configured PostgreSQL, ran migrations, set up workflow and deployment
