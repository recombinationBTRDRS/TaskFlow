# TaskFlow 🚀

Асинхронна система управління завданнями з real-time оновленнями та детальною аналітикою.

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Vue.js](https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vue.js&logoColor=4FC08D)](https://vuejs.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://postgresql.org/)
[![WebSocket](https://img.shields.io/badge/WebSocket-010101?style=for-the-badge&logo=socket.io&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)

## ✨ Особливості

- 🔄 Асинхронний backend з FastAPI та async SQLAlchemy
- ⚡ Real-time оновлення через WebSockets
- 📊 Інтерактивні графіки з Chart.js
- 🎯 Персональний task tracker з детальною аналітикою
- 🐳 Docker deployment готовий до продакшена
- 🎨 Сучасний Vue.js 3 фронтенд з TypeScript
- 🛠️ Pinia для управління станом
- 🎛️ Vite для швидкої розробки

## 🏗️ Архітектура

```
TaskFlow/
├── frontend/          # Vue.js 3 + TypeScript + Vite
├── backend/           # FastAPI + SQLAlchemy + AsyncPG
├── docker-compose.yml # Оркестрація контейнерів
└── README.md
```

## 🚀 Швидкий старт з Docker

### Вимоги

- Docker 20.10+
- Docker Compose 2.0+

### Запуск усього стеку одразу

```bash
# Клонування репозиторію
git clone https://github.com/your-username/taskflow.git
cd taskflow

# Запуск всіх сервісів (база даних + бекенд + фронтенд)
docker-compose up -d

# Перевірка статусу
docker-compose ps
```

Після запуску доступно:

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **PostgreSQL**: localhost:5432

### Управління сервісами

```bash
# Запуск окремих сервісів
docker-compose up db -d          # Тільки база даних
docker-compose up backend -d     # База + бекенд
docker-compose up frontend -d    # Весь стек

# Перегляд логів
docker-compose logs -f           # Всі сервіси
docker-compose logs -f frontend  # Тільки фронтенд
docker-compose logs -f backend   # Тільки бекенд

# Зупинка
docker-compose down              # Зупинити всі сервіси
docker-compose down -v           # Зупинити + видалити volumes
```

## 🛠️ Розробка (без Docker)

### Backend

```bash
cd backend

# Створення віртуального середовища
python -m venv venv
source venv/bin/activate  # Linux/macOS
# або
venv\Scripts\activate     # Windows

# Встановлення залежностей
pip install -r requirements.txt

# Запуск PostgreSQL (потрібен Docker)
docker-compose up db -d

# Міграції
alembic upgrade head

# Запуск сервера
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend

```bash
cd frontend

# Встановлення залежностей
npm install

# Розробка (з hot reload)
npm run dev

# Збірка для продакшена
npm run build

# Перевірка типів
npm run type-check

# Лінтинг
npm run lint
```

## 🔧 Конфігурація

### Змінні середовища

Створіть `.env` файл в корені проекту:

```env
# Database
DATABASE_URL=postgresql+asyncpg://taskflow:password@localhost:5432/taskflow_db
DB_HOST=localhost
DB_PORT=5432
DB_NAME=taskflow_db
DB_USER=taskflow
DB_PASSWORD=password

# Backend
BACKEND_HOST=0.0.0.0
BACKEND_PORT=8000
DEBUG=true

# Frontend (для Docker)
VITE_API_BASE_URL=http://localhost:8000/api
VITE_WS_URL=ws://localhost:8000/ws
```

### Порти та сервіси

| Сервіс     | Порт | Опис                         |
| ---------- | ---- | ---------------------------- |
| Frontend   | 3000 | Vue.js додаток               |
| Backend    | 8000 | FastAPI REST API + WebSocket |
| PostgreSQL | 5432 | База даних                   |

## 📁 Структура проекту

```
taskflow/
├── frontend/                    # Vue.js фронтенд
│   ├── src/
│   │   ├── views/              # Vue компоненти сторінок
│   │   ├── stores/             # Pinia stores
│   │   ├── services/           # API клієнти
│   │   ├── types/              # TypeScript типи
│   │   ├── composables/        # Vue композиція API
│   │   └── router/             # Vue Router
│   ├── Dockerfile              # Docker образ фронтенду
│   ├── nginx.conf              # Nginx конфігурація
│   ├── package.json
│   ├── vite.config.ts
│   └── tailwind.config.js
├── backend/                     # FastAPI бекенд
│   ├── app/
│   │   ├── models/             # SQLAlchemy моделі
│   │   ├── routes/             # FastAPI роути
│   │   ├── services/           # Бізнес логіка
│   │   └── main.py             # Головний файл
│   ├── Dockerfile
│   ├── requirements.txt
│   └── alembic/                # Міграції БД
├── docker-compose.yml          # Оркестрація Docker
└── README.md
```

## 🔄 Workflow розробки

1. **Локальна розробка**:

   ```bash
   # Запускаємо БД в Docker
   docker-compose up db -d

   # Backend локально
   cd backend && uvicorn app.main:app --reload

   # Frontend локально
   cd frontend && npm run dev
   ```

2. **Тестування в Docker**:

   ```bash
   docker-compose up --build
   ```

3. **Продакшен**:
   ```bash
   docker-compose -f docker-compose.prod.yml up -d
   ```

## 🧪 Тестування

```bash
# Backend тести
cd backend
pytest

# Frontend тести
cd frontend
npm run test

# E2E тести
npm run test:ui
```

## 📊 Технології

### Frontend

- **Vue.js 3** - прогресивний JavaScript фреймворк
- **TypeScript** - типізація для JavaScript
- **Vite** - швидкий build tool
- **Pinia** - управління станом
- **Vue Router** - маршрутизація
- **Tailwind CSS** - utility-first CSS
- **Chart.js** - графіки та візуалізація
- **Axios** - HTTP клієнт

### Backend

- **FastAPI** - швидкий веб-фреймворк для API
- **SQLAlchemy** - ORM з async підтримкою
- **AsyncPG** - асинхронний PostgreSQL драйвер
- **Alembic** - міграції бази даних
- **WebSockets** - real-time комунікація
- **Pydantic** - валідація даних

### DevOps

- **Docker** - контейнеризація
- **Nginx** - веб-сервер для фронтенду
- **PostgreSQL** - реляційна база даних

## 🔍 API Documentation

Після запуску бекенду, API документація доступна за адресою:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🤝 Внесок у проект

1. Fork репозиторій
2. Створіть feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit зміни (`git commit -m 'Add some AmazingFeature'`)
4. Push в branch (`git push origin feature/AmazingFeature`)
5. Відкрийте Pull Request

## 📝 Ліцензія

Цей проект ліцензований під MIT License.

## 🆘 Допомога

Якщо виникли проблеми:

1. Перевірте чи запущені всі сервіси: `docker-compose ps`
2. Подивіться логи: `docker-compose logs -f [service_name]`
3. Перестворіть контейнери: `docker-compose down && docker-compose up --build`

### Часті проблеми

**Порт зайнятий**:

```bash
# Знайти процес що використовує порт
lsof -i :3000
# Зупинити процес
kill -9 <PID>
```

**Проблеми з node_modules**:

```bash
# Очистити кеш
docker-compose down
docker system prune -f
docker-compose up --build
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
