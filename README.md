# backend

### Бэкенд для НПА

### Стек:

- Django
- DRF
- Celery
- Postgresql
- Redis
- Swagger


### Запуск через docker

```shell
$ docker-compose up -d
```

### Установка исходного кода

```shell
$ createdb --username=postgres db
$ docker run -d --cap-add sys_resource --name rp redislabs/redis
$ python3 -m venv 
$ pip install -r requirements/local.txt
$ ./manage.py makemigrations && ./manage.py migrate
$ ./manage.py loaddata paragraphtypes.json
```

### Запуск исходного кода
```shell
$ ./manage.py runserver 0.0.0.0:8000
$ celery -A conf worker --loglevel=INFO
```
