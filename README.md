# TaskFlow 🚀

Асинхронний task management система з real-time оновленнями та детальною аналітикою.

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://reactjs.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://postgresql.org/)
[![WebSocket](https://img.shields.io/badge/WebSocket-010101?style=for-the-badge&logo=socket.io&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)

## ✨ Особливості

- 🔄 **Асинхронний backend** з FastAPI та async SQLAlchemy
- ⚡ **Real-time оновлення** через WebSockets
- 📊 **Інтерактивні графіки** з Chart.js
- 🎯 **Персональний task tracker** з детальною аналітикою
- 🐳 **Docker deployment** готовий до продакшена

## 🚀 Швидкий старт

### Вимоги

- Python 3.10+
- Node.js 18+
- Docker & Docker Compose

### Запуск

```bash
# Клонування
git clone https://github.com/recombinationBTRDRS/taskflow.git
cd taskflow

# База даних
docker-compose up db -d

# Backend
cd backend
pip install -r requirements.txt
alembic upgrade head
python -m uvicorn app.main:app --reload

# Frontend
cd ../frontend
npm install
npm start
```

🎯 **План реалізації**

### Фаза 1: Backend Foundation (Тиждень 1)

**Setup проекту**  
• [] Створити FastAPI app з базовою структурою  
• [ ] Налаштувати async PostgreSQL підключення  
• [ ] Створити базові моделі (Category, Subcategory, Tag, Task)  
• [ ] Налаштувати Alembic для міграцій  
• [ ] Створити з PostgreSQL

**Database Models**  
• Category (id, name, color, created_at)  
• Subcategory (id, name, category_id, created_at)  
• Tag (id, name, color, created_at)  
• Task (id, title, description, category_id, subcategory_id, start_time, end_time, duration, created_at)  
• TaskTag (task_id, tag_id) — many-to-many

---

### Фаза 2: Core API (Тиждень 1–2)

**CRUD API Endpoints**  
• [ ] CRUD для категорій  
• [ ] CRUD для підкатегорій  
• [ ] CRUD для тегів  
• [ ] CRUD для завдань  
• [ ] Async сервіси для бізнес-логіки

**Task Management Logic**  
• [ ] Автоматичний розрахунок  
• [ ] Валідація перекриваючихся завдань  
• [ ] Bulk operations (start/stop multiple tasks)

---

### Фаза 3: Analytics & WebSocket (Тиждень 2)

**Analytics API**  
• [ ] Статистика за день  
• [ ] Статистика за тиждень  
• [ ] Розподіл по категоріях  
• [ ] Фільтрація по даті, категорії, тегу

**WebSocket Implementation**  
• [ ] WebSocket endpoint для real-time оновлень  
• [ ] Connection manager для broadcast повідомлень  
• [ ] Events: task_started, task_stopped, task_updated

---

### Фаза 4: Frontend Foundation (Тиждень 2–3)

**React Setup**  
• [ ] Create React App + Tailwind CSS  
• [ ] Axios клієнт для API запитів  
• [ ] React Router для навігації  
• [ ] Context/Provider для глобального стану

**Core Components**  
• [ ] Layout з навігацією  
• [ ] WebSocket provider для real-time updates  
• [ ] Loading states та error handling

---

### Фаза 5: Main Features (Тиждень 3–4)

**Dashboard**  
• [ ] Список сьогоднішніх завдань  
• [ ] Timer widget для активних завдань  
• [ ] Quick stats (загальний час, кількість завдань)

**Task Management**  
• [ ] Task форма (створення/редагування)  
• [ ] Task cards з action buttons  
• [ ] Фільтри по категорії/тегу/даті

**Category Management**  
• [ ] Category/Subcategory manager  
• [ ] Drag & drop для зміни порядку  
• [ ] Color picker для категорій

---

### Фаза 6: Analytics & Polish (Тиждень 4–5)

**Analytics Dashboard**  
• [ ] Chart.js інтеграція  
• [ ] Time breakdown charts  
• [ ] Category distribution pie charts  
• [ ] Date range picker

**UX Improvements**  
• [ ] Keyboard shortcuts  
• [ ] Auto-save drafts  
• [ ] Toast notifications  
• [ ] Dark/light theme

---

### Фаза 7: Testing & Deployment (Тиждень 5–6)

**Testing**  
• [ ] Backend: тести для API  
• [ ] Frontend: React Testing Library  
• [ ] Integration тести для WebSocket

**DevOps**  
• [ ] Docker multi-stage builds  
• [ ] GitHub Actions CI/CD  
• [ ] Production  
• [ ] Environment variables management
