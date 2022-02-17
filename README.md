# FastAPI with CRUD routes

[![app CI on AWS ECR](https://github.com/ofrankeADD/fastapi_crud/actions/workflows/aws.yml/badge.svg)](https://github.com/ofrankeADD/fastapi_crud/actions/workflows/aws.yml)
[![pytest coverage](https://github.com/ofrankeADD/fastapi_crud/blob/main/src/coverage.svg)](https://github.com/ofrankeADD/fastapi_crud/blob/main/src/.coverage)

Please note: This repository has public access in order to show the process and status of my web API project and should by no means be mistaken for a fully polished software product.


- My current project developing a simple web API and deploying it automatically to a cloud container registry.

- For the CI pipeline I am using Docker, Pytest, Github Actions and AWS ECR.

- For the backend I am using FastAPI, Traefik, Postgres and SQLAlchemy.

- The app has implemented the standard CRUD routes GET, POST, PUT and DELETE for a notes table.

- Currently under development: frontend with Vue.js and axios


## Building and running the Docker container:

Currently in development mode:

`docker-compose -f docker-compose.dev.yaml up -d --build`
 
API Routes:
 
`http://localhost:8432/notes/{id}/`
 
`http://localhost:8432/items/{id}/`
 
`http://localhost:8432/items/{id}?q={text}`
 
Swagger UI:
 
`http://localhost:8432/docs`
 
Frontend entrypoint:
 
`http://localhost:8080/`

## Unittests:

`docker-compose -f docker-compose.dev.yml exec -T backend pytest .`
