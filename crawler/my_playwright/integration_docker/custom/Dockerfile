FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

WORKDIR /my-project

RUN virtualenv venv && \
    . venv/bin/activate && \
    python -m pip install playwright


COPY custom_script.py .