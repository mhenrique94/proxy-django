# PROXY DJANGO

### how to get a proxy list locally:

at the same folder as main.py, type on a terminal:
```
python3 main.py
```
the output will be a txt file with a bunch of proxies on the following format:
`type://ip:port`

like:
<br>HTTPS://50.174.7.156:80
<br>SOCKS5://104.17.248.164:80
<br>HTTP://190.217.101.77:999


enjoy!


### for devs:
this will be an endpoint!
<br>as soon as i get the work started, new information will be added here.
This project runs on django 4.2, python3, postgresql and everything else that can be found in requirements.txt

Be aware the a basic setup is needed:
- setup the database, including user and roles;
- a virtual environment
- the .env with the keys.
<br>Hope it helps:
https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-20-04



1. at the root folder of the project, run on terminal:
```
pip install -r requirements.txt
./manage.py makemigrations
./manage.py migrate
./manage.py runserver
```
:)