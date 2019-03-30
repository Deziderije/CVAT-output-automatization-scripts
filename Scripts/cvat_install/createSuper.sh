#! /bin /bash

sudo docker exec -it cvat bash -ic '/usr/bin/python3 ~/manage.py createsuperuser'
