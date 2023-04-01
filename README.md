# central_trading_card-game_project
วิธีเปิด project <br /> 
ลง requirements <br /> 
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
run app
```
python manage.py runserver
```
