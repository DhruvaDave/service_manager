This repo will work in django version 1.8 or 1.9

This is demo microservice app which is help you to understand microservice concept.

After downloading this repo run this commands: 

python manage.py makemigrations
python manage.py migrate

python manage.py syncdb

python manage.py runcluster 

The first time you do this, you won’t see any services registerd.

Click on the “Admin” link, log in and register services by clicking on “Services” in the Microservices admin. Click “Add service” to add each new service in your app.

Runcluster will run all the services which are added in microservice table at a same time.


For any application that needs to find services in the cluster, add this to the settings.py file:

import requests

SERVICES = requests.get('http://127.0.0.1:8000/services/').json()

Do not add this line first .. first add all services and check them running on different port. :)

Referances :
https://microservicesdocumentation.readthedocs.io/en/latest/contributing/python.html
https://pypi.org/project/django-microservices/