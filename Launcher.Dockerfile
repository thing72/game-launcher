from python:3.9

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

ENV PATH="~/.poetry/bin:${PATH}"

WORKDIR /app

COPY . /app

RUN ~/.poetry/bin/poetry install
