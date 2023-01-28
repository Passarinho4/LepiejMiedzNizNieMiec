FROM python:3.9-slim-buster

RUN pip install --upgrade pip --no-cache-dir
COPY requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt --no-cache-dir

COPY ./app /opt/app

COPY model /opt/model

WORKDIR /opt

EXPOSE 4000

CMD ["python", "app/server.py"]
