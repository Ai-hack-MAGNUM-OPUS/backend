FROM python:3.10-alpine

# Set environment variables
ENV PYTHONUNBUFFERED 1

COPY ./requirements/base.txt .
COPY ./requirements/production.txt .
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /production.txt
RUN apk del .tmp-build-deps


RUN mkdir /app
COPY ./app /app
WORKDIR /app