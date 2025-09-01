# Простіший і надійніший варіант
FROM node:18-alpine AS build

WORKDIR /app

# Копіюємо package файли
COPY package*.json ./

# Встановлюємо залежності
RUN npm clean-install

# Копіюємо код
COPY . .

# Очищуємо кеш і проблемні файли
RUN rm -rf dist .vite node_modules/.cache || true && \
    find . -name "*.vue.js" -delete || true && \
    find . -name "*.vue.d.ts" -delete || true

# Збираємо проект
RUN npm run build

# Production stage
FROM nginx:alpine AS production

# Копіюємо зібрані файли
COPY --from=build /app/dist /usr/share/nginx/html

# Копіюємо nginx конфіг
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 3000

CMD ["nginx", "-g", "daemon off;"]