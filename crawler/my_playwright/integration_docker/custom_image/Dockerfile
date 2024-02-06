FROM python:3.11.7-slim-bookworm as base

ARG DOCKER_IMAGE_NAME_TEMPLATE="self/playwright:python-bookworm"


RUN pip install playwright
RUN playwright install --with-deps chromium


FROM base as runtime-image

WORKDIR /my-project

COPY custom_script.py .
