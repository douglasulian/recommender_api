FROM tiangolo/uwsgi-nginx-flask:python3.6

COPY ./app /app
COPY ./requirements.txt /app

RUN  python3.6 -m pip install -r requirements.txt