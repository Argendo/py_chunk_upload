# Используйте официальный образ Python
FROM python:3.8-slim

# Установите необходимые зависимости
RUN pip install Flask Flask-Dropzone

# Создайте рабочую директорию в контейнере
WORKDIR /app

# Копируйте файлы приложения в контейнер
COPY app_chunked.py /app/app_chunked.py
COPY templates/index_chunked.html /app/templates/index_chunked.html

# Установите переменную окружения для Flask
ENV FLASK_APP=app_chunked.py

# Определите порт, на котором будет работать приложение
EXPOSE 5002

# Запустите приложение при старте контейнера
CMD ["flask", "run", "--host=0.0.0.0", "--port=5002"]

