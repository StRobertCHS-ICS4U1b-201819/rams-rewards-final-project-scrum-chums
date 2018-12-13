# Setup workspace from scratch
Create a **blank** workspace, then enter the following commands into the terminal.
```sh
$ sudo python -m pip install --upgrade pip setuptools
$ sudo apt-get install python3.6
$ sudo pip install pipenv
```

### Create virtual environment
```sh
$ pipenv --python 3.6
```
This will create a Pipfile which can be edited (advanced)

### Install django
```sh
$ pipenv install django
```
This will add `django` to the `Pipfile`.

### Enter into the virtual Environment
```sh
pipenv shell
```
This will log you in to the Python virtual environment with django installed. 
This **must** be done to work with the correct version of Python with the correct version of Django installed. 
To exit, enter `exit` into the terminal.

At this point, you can start the [Django tutorial](https://docs.djangoproject.com/en/2.1/intro/tutorial01/).

# **ERROR:** Running server
You need to go into your project's `settings.py` file and change the following line:
```python
ALLOWED_HOSTS = []
```
to..
```python
ALLOWED_HOSTS = ["*"]
```

---
---


# Common commands

### Create a project
Replace `projectname` with the name of your project. i.e., `django-admin startproject tutorial`.
```sh
$ pipenv shell
$ django-admin startproject projectname
$ cd projectname
$ python manage.py startapp appname
```

### Run Django server on c9.io
```sh
$ python manage.py runserver $IP:$PORT
```

### Make migrations
When you edit a model, you must make migrations and migrate (to update the database structure).
```sh
$ python manage.py makemigrations
$ python manage.py migrate
```