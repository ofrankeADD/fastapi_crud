FROM python:3.9-alpine

WORKDIR /code/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /code/src/app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/src/app/requirements.txt

#RUN set -eux \
#    && apk add --no-cache --virtual .build-deps build-base \
#        libressl-dev libffi-dev gcc musl-dev python3-dev \
#    && pip install --upgrade pip setuptools wheel \
#    && pip install -r /code/src/app/requirements.txt \
#    && rm -rf /root/.cache/pip

COPY . /code/src/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8432", "--proxy-headers", "--ssl-keyfile", "./key.pem", "--ssl-certfile", "./cert.pem", "--reload"]

