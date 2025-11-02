# Board — Простая доска объявлений
Board — это простой backend для доски объявлений с аутентификацией, CRUD для объявлений и пользователей, асинхронными задачами и CI/CD.

## Функционал
- Регистрация, аутентификация, управление пользователями через JWT

- Создание, редактирование, удаление и просмотр объявлений

- Разрешения: пользователи могут редактировать и удалять только свои объявления

- Асинхронные задачи на Celery с Redis брокером

- Планирование фоновых заданий через django-celery-beat

- Тесты с Pytest и автоматическая проверка качества кода

- CORS поддержка для фронтенда

## Технологии  

- Python 3.13, Django 5.1, Django REST Framework

- PostgreSQL 15

- Celery, Redis

- Docker, Docker Compose

- GitHub Actions для CI/CD

- Nginx для статических файлов и реверс-прокси

- Python-dotenv для управления переменными окружения

- Black, flake8, isort для качества кода

## API
API построен с использованием Django REST Framework и доступен по адресу /api/.

## Основные эндпоинты:

/api/users/ — управление пользователями (CRUD, регистрация, просмотр)

/api/ads/ — управление объявлениями

### JWT токены можно получить через стандартные эндпоинты аутентификации Simple JWT:

/api/token/ — получение access и refresh токенов

/api/token/refresh/ — обновление access токена

Требуется авторизация для создания, изменения и удаления ресурсов.

## Переменные окружения (.env)
Обязательные переменные:  

.env:  

SECRET_KEY=your_secret_key_here  
DEBUG=True  
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com  
  
POSTGRES_DB=board_db  
POSTGRES_USER=board_user  
POSTGRES_PASSWORD=board_password  
POSTGRES_HOST=db  
POSTGRES_PORT=5432  
  
REDIS_URL=redis://redis:6379/0  

CORS_ALLOWED_ORIGINS=http://localhost,http://127.0.0.1  
  
## Запуск и разработка

Клонируйте репозиторий и создайте .env файл с нужными значениями.

Убедитесь, что докер установлен.

1. Запустите контейнеры:

docker-compose up -d --build
2. Выполните миграции:

docker-compose exec backend python manage.py migrate
3.  Создайте суперпользователя:

docker-compose exec backend python manage.py createsuperuser
4. Доступ к приложению: http://localhost:8000/

## CI/CD
- CI запускается при пушах в ветки main и develop.

- Проверяется стиль кодирования (flake8), запускаются тесты (pytest).

- Сборка Docker образов backend и nginx.

- Деплой на удалённый сервер с помощью SSH и запуск Docker Compose.

- Для деплоя необходимо настроить GitHub Secrets:

SERVER_IP — IP сервера  

SERVER_USER — пользователь SSH  

SERVER_SSH_KEY — приватный SSH ключ  

DEPLOY_DIR — каталог на сервере для деплоя  

## Контакты
- Автор: mymillions@ya.ru
- Лицензия: MIT