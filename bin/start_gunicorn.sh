#!/bin/bash
source /home/user/Usluga_podiezdov/venv/bin/activate
exec gunicorn -c "/home/user/Usluga_podiezdov/conf/gunicorn_conf.py" podiezd.wsgi
