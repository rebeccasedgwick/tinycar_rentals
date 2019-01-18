# TinyCar Rentals
A small site to manage car rentals, using Django's admin site.

## To run:
_Note: requires pipenv to be pre-installed_

Clone the repo, launch a pipenv sub-shell and install dependencies:
```
~/$ cd tinycar_rentals/
~/tinycar_rentals$ pipenv shell
~/tinycar_rentals$ pipenv install
```

Create and run migrations:
```
~/tinycar_rentals$ cd tinycar/
~/tinycar_rentals/tinycar$ python3 manage.py makemigrations
~/tinycar_rentals/tinycar$ python3 manage.py migrate
```

Create a superuser, to access the admin site:
```
~/tinycar_rentals/tinycar$ python3 manage.py createsuperuser
```

You will be prompted to enter your admin credentials of choice.
Run the app:
```
~/tinycar_rentals/tinycar$ python3 manage.py runserver
```

Navigate to http://127.0.0.1:8000/admin  
Login using your superuser credentials.
