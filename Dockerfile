FROM python:3

WORKDIR /usr/src/app

RUN pip install pandas tweepy 

COPY ./bot ./bot

WORKDIR /usr/src/app/bot

CMD ["python", "./main.py"]

