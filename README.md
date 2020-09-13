# template

## database setup (with default values)
```
$ sudo -u postgres psql
postgres=# create database template_db;
postgres=# create user template_admin with encrypted password '$templatepass$';
postgres=# grant all privileges on database template_db to template_admin;
postgres=# \q
```

### if you want to run tests
```
$ sudo -u postgres psql
postgres=# ALTER USER template_admin CREATEDB;
postgres=# \q
$ python manage.py migrate
```

## initial setup
This script setups everything you need for the project (pipenv, yarn and django)
```
$ ./quickstart.sh
```

### activate pipenv enviroment
```
$ pipenv shell
```

### install new libraries in pipenv
```
$ pipenv install docxtpl
```

## yarn
If you change something in vue you must rebuild the html with this command
```
$ yarn build
```

### run django
```
$ python manage.py migrate
$ python manage.py runserver
```
