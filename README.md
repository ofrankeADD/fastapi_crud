# FastAPI with CRUD routes

[![app CI on AWS ECR](https://github.com/ofrankeADD/fastapi_crud/actions/workflows/aws.yml/badge.svg)](https://github.com/ofrankeADD/fastapi_crud/actions/workflows/aws.yml)
[![pytest coverage](https://github.com/ofrankeADD/fastapi_crud/blob/main/src/coverage.svg)](https://github.com/ofrankeADD/fastapi_crud/blob/main/src/.coverage)

My current project developing a simple web API and deploying it automatically to a cloud container registry.

For the CI pipeline I am using Docker, Pytest, Github Actions and AWS ECR.

For the web API I am using FastAPI, Traefik, Postgres and SQLAlchemy.

The goal is to implement the standard CRUD routes as GET, POST, PUT and DELETE for a notes table.
