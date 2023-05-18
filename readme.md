# Weather collector.
## Описание.
Каждый час собирает информацию о погоде для 50 крупнейших городов мира, после чего сохраняет значение в БД.  
Берём погоду здесь https://openweathermap.org/
(Проект будет немного допилен после ревью, но пока на изначально выбранном стеке.  
Пока сделано: прикручена база, ловим ошибки, логирование, секреты убраны.)
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
```
docker-compose up
```
- Ждите.
```
...
```
- Когда всё соберётся можно перейти по адресу:  
[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
```
username:admin  (SUPERUSER_USERNAME из файла .env)  
password:admin  (SUPERUSER_PASSWORD из файла .env)  
```
- Далее идём сюда, тут скоро появятся наши данные:  
[http://127.0.0.1:8000/admin/collector/weatherdata/](http://127.0.0.1:8000/admin/collector/weatherdata/)
## Комментари
- В settings для тестирования установлен интервал в 60 секунд:
```
CELERY_BEAT_SCHEDULE = {
    "run_script_every_hour": {
        "task": "collector.tasks.collect_weather_periodically",
        # "schedule": 3600.0,  # Каждый час (в секундах)
        "schedule": 60.0,  # Каждые ... сек (для тестов)
    },
}
```
- Есть ограничения, апишка отдаёт 1000 запросов в день(бесплатные).  
Нам надо 50 городов каждый час, соотв. 1200 запросов в день. Соотв. немного не вписываемся!
- Технологии выбраны путем гугления(опыта с celery нет). Сильного мнения по поводу правильности стека нет, наоборот много сомнений (нужен ли джанго).
- Структура БД... Пока так, можно было отделить city и timezone.
- Из интересных побочных данных я вижу только timezone, отсюда можно прогнозировать нагрузки, остальное (погодное) кмк не очень интересно.
## Автор
Я
