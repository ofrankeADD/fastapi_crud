FROM python:3.9-alpine

WORKDIR /code/src/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /code/src/requirements.txt

RUN pip install -r /code/src/requirements.txt

COPY . /code/src/
#COPY ../tests/ /code/src/tests/

#CMD sh -c 'while !</dev/tcp/db/5432; do sleep 1; done; gunicorn app.main:app --bind 0.0.0.0:8432 --reload --workers 2 --worker-class uvicorn.workers.UvicornWorker'

CMD ["gunicorn", "app.main:app", "--bind", "0.0.0.0:8432", "--reload", "--workers", "2", "--worker-class", "uvicorn.workers.UvicornWorker"]

