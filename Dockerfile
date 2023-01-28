FROM python:3.9-slim-buster

COPY ./app /opt/app
COPY requirements.txt /opt/requirements.txt
COPY model /opt/model

WORKDIR /opt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 4000

CMD ["python", "app/server.py"]
