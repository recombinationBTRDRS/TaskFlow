# TaskFlow

TaskFlow is a Django-based task management and time-tracking application. It enables you to define your own categories, subcategories, and tags, log start/end times or durations for each task, and get simple analytics on how you spend your day or week.

---

## Features

- User authentication (single user by default, extensible to multiple users)
- Customizable categories and subcategories with recommended defaults
- Tagging system for flexible filtering
- Task logging with:
  - Start time
  - End time **or** duration
  - Automatic calculation of end time or duration
- Dashboard showing today’s tasks in chronological order
- CRUD operations for categories, subcategories, tags, and tasks
- Basic analytics:
  - Total time per category over a selected period (day, week)
  - Filtering by date range, category, or tag
  - Data presented in tables and simple charts (Chart.js)

---

## Tech Stack

- Python 3.10+
- Django 4.x
- PostgreSQL 14
- Django REST Framework
- Chart.js for front-end charts
- Docker & Docker Compose
- GitHub Actions for CI/CD

---

## Prerequisites

- Python 3.10+
- pip
- Docker & Docker Compose (optional, for containerized setup)
- PostgreSQL (or use Dockerized DB)

---

## Installation

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/taskflow.git
   cd taskflow
   ```
