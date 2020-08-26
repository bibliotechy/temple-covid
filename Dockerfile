FROM python:3.8-slim

COPY . /app
RUN cd /app && pip install pipenv && pipenv install --dev
WORKDIR /app

ENTRYPOINT [ "pipenv", "run", "python", "extractor.py" ]
