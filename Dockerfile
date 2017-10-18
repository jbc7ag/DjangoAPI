FROM python:3.6
COPY apiAyuda/requirements.txt /apiAyuda/requirements.txt
RUN pip install -r /apiAyuda/requirements.txt
WORKDIR /apiAyuda
COPY apiAyuda /apiAyuda
#CMD gunicorn --bind 0.0.0.0:8000 apiAyuda.wsgi:application
CMD  sh migraciones.sh