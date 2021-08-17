Install
-------
conda create --name django-mozilla python=3
pip install django

Start Dev
---------
conda activate django-mozilla
python3 manage.py makemigrations && python3 manage.py migrate
python manage.py runserver 0.0.0.0:8000
