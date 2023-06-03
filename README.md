При первом запуске:
1. Переходим в папку GrammaRu

2. Создаем виртуальное окружение и устанавливаем необходимые библиотеки:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install psycopg2-binary

3. Создаем и запускаем БД:
docker-compose up

4. Открываем еще один терминал, выполняем пункт 1 и делаем миграции:
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

5. Запускаем приложение:
python manage.py runserver


При повторных запусках:
1. Переходим в папку GrammaRu и открываем первый терминал. Запускаем БД:
docker-compose run

2. Переходим в папку GrammaRu и открываем второй терминал. Запускаем приложение:
python manage.py runserver
