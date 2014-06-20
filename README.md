gsr14
=====

- Install virtual env: `sudo pip install virtualenv`
- Create venv: `mkdir venv; virtualenv venv --no-site-packages`
- Activate venv: `source venv/bin/activate` or on Windows: `venv\Scripts\activate.bat`
- When no longer needed, deactivate venv: `deactivate`
- Install requirements: `pip install -r requirements.txt`

Database commands:
- python manage.py syncdb
- python manage.py sql hack

Update database: 
-python manage.py sql hack

To reset hack database tables:
- python manage.py reset hack

Using admin to manually add data:
- python manage.py runserver
- go to 127. ... /admin
=====
