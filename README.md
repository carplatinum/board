# Board - Backend доска объявлений
Простой backend для доски объявлений, реализованный на  
Django 5, Django REST Framework с JWT авторизацией, Celery, Redis, PostgreSQL, Docker и развертыванием в Yandex Cloud.

# Технологии  
- Python 3.13, Django 5.x

- PostgreSQL, PgAdmin 4

- Django REST Framework + djangorestframework-simplejwt (JWT)

- Celery с Redis брокером

- Docker, Docker Compose

- GitHub Actions для CI/CD

- CORS support

# Структура проекта  
- apps/users — управление пользователями

- apps/ads — объявления

- board/ — конфигурация Django проекта и celery.py

- docker-compose.yml — для локального запуска и разработки

- CI/CD workflow в .github/workflows/ci-cd.yml

# Установка и запуск
1. Клонирование и установка зависимостей

git clone <репозиторий>
cd board
poetry install
2. Создание и настройка .env файла
Создайте .env в корне проекта со следующими переменными:

SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

POSTGRES_DB=board_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=db
POSTGRES_PORT=5432

REDIS_URL=redis://redis:6379/0

CORS_ALLOWED_ORIGINS=http://localhost,http://127.0.0.1
3. Запуск базы данных и Redis через Docker Compose

- docker-compose up -d db redis
- Или используйте PgAdmin для управления базой.

4. Примените миграции

- docker-compose exec backend python manage.py migrate
5. Запуск сервера разработки

- docker-compose exec backend python manage.py runserver 0.0.0.0:8000
6. Запуск Celery воркера и Celery beat

- docker-compose exec celery celery -A config worker -l info
- docker-compose exec celery-beat celery -A config beat -l info --scheduler django_celery_beat.schedulers.DatabaseScheduler
- Docker локально и деплой
- Для локальной разработки и деплоя используется docker-compose.yml и Dockerfile.

## Для сборки и запуска локально:

- docker-compose up --build
- В контейнере backend установлен Gunicorn в качестве WSGI-сервера.

- Файлы с миграциями и статикой монтируются через тома для удобства разработки.

# CI/CD
Интеграция настроена с GitHub Actions.

Автоматическая сборка, тестирование и деплой контейнеров в Yandex Cloud VM.

Можно использовать GitHub Secrets для безопасного хранения переменных окружения.

# Контакты  
- Автор: mymillions@ya.ru 
- Лицензия: MIT