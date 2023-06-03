При первом запуске:
1. Открываем первый терминал и переходим в папку GrammaRu

2. Создаем виртуальное окружение и устанавливаем необходимые библиотеки:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install psycopg2-binary

3. Создаем и запускаем БД:
docker-compose up

4. Выполняем пункт 1 для второго терминала и делаем миграции:
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

5. Запускаем приложение:
python manage.py runserver


При повторных запусках:
1. Открываем первый терминал и переходим в папку GrammaRu. Запускаем БД:
docker-compose up

2. Открываем второй терминал и переходим в папку GrammaRu. Запускаем приложение:
python manage.py runserver


При косяках с БД или новых добавлениях и правках в моделях:
1. Удаляем из папки migrations все файлы с миграциями

2. Открываем терминал и чистим docker:
docker container rm -f $(docker container ls -aq)
docker image prune -a
docker volume prune
docker network prune
