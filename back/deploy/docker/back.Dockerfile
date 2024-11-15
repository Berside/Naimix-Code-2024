FROM python:3.12


WORKDIR /app

ENV PYTHONUNBUFFERED=1
# ENV PYTHONPATH="${PYTHONPATH}:/app"


COPY api/. /app/

RUN ls .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 7200

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:7000
