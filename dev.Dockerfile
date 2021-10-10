FROM python:3.8-alpine

WORKDIR /app

RUN apk update && apk add build-base gcc

COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["python3", "main.py"]
