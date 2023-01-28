FROM python:3.9-slim-buster

COPY ./app /app

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 4000

CMD ["python", "server.py"]
