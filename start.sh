#!/bin/sh
source /home/www/nx2/bin/activate
nohup /home/www/nx2/bin/gunicorn_django --workers=2 -b 0.0.0.0:9996 --timeout=300&
nohup  /usr/local/elasticsearch/elasticsearch-1.4.2/bin/elasticsearch &
