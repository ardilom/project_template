#!/bin/bash

engine=`python -c"from backend.settings.dev import DATABASES; print(DATABASES['default']['ENGINE'])"`
debug=`python -c"from backend.settings.dev import DEBUG; print(DEBUG)"`
dbname=`python -c"from backend.settings.dev import DATABASES; print(DATABASES['default']['NAME'])"`

if [ $debug = "True" ] ; then
echo "----------------------drop-database------------------------------"
    if [ $engine == "django.db.backends.sqlite3" ]; then
        if [ -f $dbname ] ; then
            echo "SQLITE: deleting $dbname"
            rm $dbname
        fi
    else
        dbuser=`python -c"from backend.settings.dev import DATABASES; print(DATABASES['default']['USER'])"`
        dbpass=`python -c"from backend.settings.dev import DATABASES; print(DATABASES['default']['PASSWORD'])"`
        if [ $engine == "django.db.backends.mysql" ]; then
            echo "drop database $dbname" | mysql --user=$dbuser --password=$dbpass
            echo "create database $dbname" | mysql --user=$dbuser --password=$dbpass
        else
            dropdb $dbname
            createdb $dbname
        fi
    fi
    python manage.py migrate
fi

echo "Yarn build"
yarn build
