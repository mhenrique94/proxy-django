# PROXY DJANGO
___

PT: Esse projeto foi desenvolvido com o intuito de praticar desenvolvimento back-end por meio da criação de uma API, do serviço para manipulação local de lotes de texto, deploy (colocar no ar) no render.com, da implementação de modelo e manipulação de banco de dados e, futuramente, o consumo desses dados por meio de um projeto paralelo de front-end (página da web).

EN: This project was developed aiming the practice of back-end development through an API design, a service to manipulate local text chuncks, the deploy on render.com, through the implementation and manupalation of database model, and furthermore, the data consumption through a paralel front-end project (web-page).

PT: Para a versão web com a lista de proxy, visite:
EN: For a proxylist web version, visit:

https://proxy-django.onrender.com

___
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

ps.: a different list an be build on each run

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



At the root folder of the project, run on terminal:
```
pip install -r requirements.txt
./manage.py makemigrations
./manage.py migrate
./manage.py runserver
```
:)