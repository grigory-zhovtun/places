# Places (Django)

Открыть проект локально: после запуска перейдите на http://127.0.0.1:8000/

Небольшое Django‑приложение для отображения интересных мест на карте. Проект использует Leaflet, статические JSON‑данные и/или данные из БД. Есть админка для управления местами и фотографиями.

---

## Features

- Интерактивная карта с метками и боковой панелью  
- Загрузка и отображение фотографий мест (медиа)  
- Админ‑панель Django: управление местами и изображениями  
- Поддержка визуального редактора описаний (`django-tinymce`)  
- Сортировка изображений в админке (`django-admin-sortable2`)  
- Раздача статики и медиа в dev‑режиме  

---

## Prerequisites

- Python 3.10+  
- Установленный `pip`  
- Файл `requirements.txt` с зависимостями (в репозитории)  

---

## Installation and Setup

1. Клонируйте репозиторий  
   ```bash
   git clone <your-repository-url>
   cd <project-folder>
   ```

2. (Опционально) создайте и активируйте виртуальное окружение  
   ```bash
   python -m venv venv
   # Linux/macOS
   source venv/bin/activate
   # Windows
   venv\Scripts\activate
   ```

3. Установите зависимости  
   ```bash
   pip install -r requirements.txt
   ```

4. Создайте файл `.env` в корне проекта со значениями переменных окружения  
   ```env
   SECRET_KEY=your-secret-key
   DEBUG=True
   ALLOWED_HOSTS=127.0.0.1,localhost
   ```

5. Выполните миграции и (при необходимости) создайте суперпользователя  
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. Запустите сервер разработки  
   ```bash
   python manage.py runserver
   ```

7. Откройте в браузере http://127.0.0.1:8000/  
   Админ‑панель: http://127.0.0.1:8000/admin/

---

## Environment Variables

- `SECRET_KEY` — секретный ключ Django (обязателен)  
- `DEBUG` — режим отладки (`True`/`False`, по умолчанию `False`)  
- `ALLOWED_HOSTS` — список хостов, разделённых запятой (например, `127.0.0.1,localhost`)  

---
