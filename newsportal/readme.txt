admin
admin1234


py -m venv venv (python3 -m venv venv)
venv/scripts/activate (source venv/bin/activate)
cd newsportal
pip install django
pip install django-filter
pip install django-allauth
py manage.py makemigrations
py manage.py migrate
py manage.py runserver