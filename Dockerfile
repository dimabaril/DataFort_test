FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

COPY weather_collector/ .

RUN python manage.py migrate

# Создание суперпользователя
RUN echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell

# CMD ["python3", "manage.py", "runserver", "0:8000"]

CMD ["bash"]