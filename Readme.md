# Проект Atomic Habits

Atomic Habits - это веб-приложение для отслеживания и управления своими привычками.

## Технологии:

* python 3.11
* django 4.2.7
* djangorestframework 3.14.0
* django-celery-beat 2.5.0 
* django-cors-headers 4.3.1
* celery 5.3.5
* PostgreSQL
* psycopg2-binary 2.9.9
* pillow 10.1.0
* redis 5.0.1
* Docker 24.0.6

## Установка:

Для установки и запуска проекта выполните следующие шаги:

1. Склонируйте репозиторий проекта на свой локальный компьютер git clone _https://github.com/SheenShaman/habit_traker_
2. Создайте виртуальное окружение **python3 -m venv venv**
3. Активируйте виртуальное окружение **venv\Scripts\activate**
4. Установите зависимости **pip install -r requirements.txt**
5. Примените миграции **python manage.py migrate**
6. Запустите сервер разработки Django **python manage.py runserver**
7. Откройте приложение в вашем веб-браузере по адресу http://127.0.0.1:8000/

##### В проекте используется Docker Compose

Для запуска приложения необходимо выполнить следующие команды: 
* **docker-compose build** - сборка образа
* **docker-compose up** - запуск контейнера 

##### Если БД не создана, то необходимо будет ее создать, но перед этим убедиться, что у вас запущен контейнер. 

Команда для создания БД: 
* **docker-compose exec db psql -U postgres**
###### Автор проекта:

https://github.com/SheenShaman