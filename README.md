# Древовидное меню

### Используемые технологии:
- Django
- PostgreSQL

### Перед запуском выполните:
- Склонировать репозиторий в локальную директорию:
```
git clone git@github.com:olga3ok/tree_menu_test_task.git
```
- Активация виртуального окружения и установка зависимостей из requirements.txt:
```
python3 -m venv venv
```
```
source venv/bin/activate
```
```
cd tree_menu_test_task
```
```
pip install -r requirements.txt
```
- В корне проекта создайте .env и задайте значения переменных:
```
DJANGO_SECRET_KEY=

DJANGO_ALLOWED_HOSTS=#localhost
INTERNAL_IPS=#localhost

DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=

DEBUG=
```
- Cоздание администратора и миграций, а также их применение:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py createsuperuser
```
- Запуск:
```
python manage.py runserver
```
