FROM python:3.9-alpine

WORKDIR /code/src/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /code/src/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/src/requirements.txt

#RUN set -eux \
#    && apk add --no-cache --virtual .build-deps build-base \
#        libressl-dev libffi-dev gcc musl-dev python3-dev \
#    && pip install --upgrade pip setuptools wheel \
#    && pip install -r /code/src/app/requirements.txt \
#    && rm -rf /root/.cache/pip

COPY . /code/src/

CMD ["coverage", "run", "-m", "pytest"]
CMD ["coverage-badge", "-f", "-o", "/code/src/coverage.svg"]

#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8432", "--proxy-headers", "--ssl-keyfile", "./key.pem", "--ssl-certfile", "./cert.pem", "--reload"]

CMD ["gunicorn", "app.main:app", "--bind", "0.0.0.0:8432", "--reload", "--workers", "2", "--worker-class", "uvicorn.workers.UvicornWorker"]

