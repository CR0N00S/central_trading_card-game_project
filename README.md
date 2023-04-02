# central_trading_card-game_project
how to open this project <br /> 
install requirements <br /> 
```
virtualenv env
.\env\Scripts\activate
pip install -r requirements.txt
```
set database
```
python manage.py makemigrations
python manage.py migrate
```
run the app
```
python manage.py runserver
```
web app will be in http://127.0.0.1:8000/ <br /> 
admin stie is http://127.0.0.1:8000/admin

create superuser for admin site 
```
python manage.py createsuperuser
```
