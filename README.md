Install
-------
    conda create --name django-mozilla python=3
    pip install django

Start Dev
---------
    conda activate django-mozilla
    python manage.py makemigrations && python manage.py migrate
    python manage.py runserver 0.0.0.0:8000
