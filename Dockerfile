FROM python:3-alpine

RUN apk add --no-cache python3-dev libstdc++ g++
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

COPY *.py /app/
COPY requirements.txt /app/
COPY .env.dist /app/.env

RUN mkdir /app/data

WORKDIR /app
RUN pip install -r requirements.txt
RUN apk del python3-dev libstdc++ g++

CMD python sheila.py