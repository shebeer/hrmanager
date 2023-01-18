# HR Manager backend application
## Setup
The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/gocardless/sample-django-app.git
$ cd hrmanager
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv env
$ source env/bin/activate
```
Once `pip` has finished downloading the dependencies,
Create and migrate database:
```sh
(env)$ python manage.py migrate
```
Create super user:
```sh
(env)$ python manage.py createsuperuser
```
Run application
```sh
(env)$ python manage.py runserver
```
## API Documentation
Authentication
```sh
POST /api-token-auth/
payload:
{
    "username":"username",
    "password":"password"
}
Response:
{
    "token": "212f871600467069f064096"
}
```

