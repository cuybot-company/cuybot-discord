FROM python:3.8-alpine

WORKDIR /app

RUN apk update && apk add build-base gcc npm

RUN npm i -g nodemon

COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["nodemon", "main.py"]
