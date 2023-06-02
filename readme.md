# Weather collector.
## Описание.
Каждый час собирает информацию о погоде для 50 крупнейших городов мира, после чего сохраняет значение в БД.  
Берём погоду здесь https://openweathermap.org/  
Города берём здесь http://api.geonames.org/  
(Проект будет немного допилен после ревью, но пока на изначально выбранном стеке.  
Сделано: прикручена база, ловим ошибки, логирование, секреты убраны, города тащим с geonames.)
## Технологии
- Python 3.11
- Django 4.2
- Requests
- Postgres
- Сelery
- Redis
- Docker
- Docker-compose
- Loguru
- Wait-for-it
## Установка
- Клонируйте репозиторий и перейти в него:
```
git clone git@github.com:dimabaril/DataFort_test.git
cd DataFort_test
```
- Создайте файл .env находящийся в директории вместе с файлом docker-compose.yaml  
и наполните его следующим образом (юзеров и пароли придумываем свои):
```
DJANGO_SECRET_KEY="django-super-secret-key"

OPENWEAWERMAP_API_KEY = "cc4a59be6e427ede277ae4d9ee4acde4"  # мой ключ

GEONAMES_USERNAME = "dimabaril" # мой, не злоупотреблять

DB_ENGINE=django.db.backends.postgresql  # указываем, что работаем с postgresql
DB_NAME=postgres  # имя базы данных
POSTGRES_USER=postgres  # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres  # пароль для подключения к БД (установите свой)
DB_HOST=db  # название сервиса (контейнера)
DB_PORT=5432  # порт для подключения к БД

SUPERUSER_USERNAME=admin  # для админки
SUPERUSER_EMAIL=admin@exemple.com
SUPERUSER_PASSWORD=admin  # для админки
```
- Докер у вас конечно есть. Запустите docker-compose:
### 1 Варинат для ленивых
```
docker-compose up
```
- Ждите.
```
...
```
### 2 Вариант
```
docker-compose -f docker-compose_2.yaml
```
- Далее все команды в контейнере
- Миграции
```
python manage.py migrate
```
- Юзер для админки
```
python manage.py createsuperuser
```
- Команда для сбора городов в базу с geonames
```
python3 manage.py collect_cities
```
- Далее надо задачи в разных терминалах пустить
- Celery Worker
```
celery -A weather_collector worker -l info
```
- Celery Beat
```
celery -A weather_collector beat -l info
```
- Тут надо немного подождать через минуту в базе появится погода.  
- Когда всё соберётся можно перейти по адресу:  
[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
```
либо то что вбивали на createsuperuser
username:admin  (SUPERUSER_USERNAME из файла .env)  
password:admin  (SUPERUSER_PASSWORD из файла .env)  
```
- Далее идём сюда, тут скоро появятся наши данные:  
[http://127.0.0.1:8000/admin/collector/weatherdata/](http://127.0.0.1:8000/admin/collector/weatherdata/)
## Комментари
- В settings для тестирования установлен интервал в 60 секунд:  
(можно поиграться с разными вариантами)
```
CELERY_BEAT_SCHEDULE = {
    "run_script_every_hour": {
        "task": "collector.tasks.collect_weather_periodically",
        # "schedule": 3600.0,  # Каждый час (в секундах)
        "schedule": timedelta(seconds=60),  # со старта и с промежутком
        # "schedule": crontab(minute=0, hour="*/1"),  # Каждый час
    },
}
```
- Есть ограничения, апишка отдаёт 1000 запросов в день(бесплатные).  
Нам надо 50 городов каждый час, соотв. 1200 запросов в день. Соотв. немного не вписываемся!
- Технологии выбраны путем гугления(опыта с celery нет). Сильного мнения по поводу правильности стека нет, наоборот много сомнений (нужен ли джанго).
- Структура БД... Пока так, можно было отделить city и timezone.
- Из интересных побочных данных я вижу только timezone, отсюда можно прогнозировать нагрузки, остальное (погодное) кмк не очень интересно.

З.Ы. В базе городов с geonames есть Dubai City который на openweathermap просто Dubai.
Там выпрыгивает exception в логах, пусть будет.

Если не заленюсь напишу тесты.
## Автор
Я
