FROM python:3.9-slim-buster

ARG USERNAME=python
ARG UID=1000
ARG GID=1000

RUN groupadd -g "${GID}" ${USERNAME} \
    && useradd --create-home --no-log-init -u "${UID}" -g "${GID}" ${USERNAME}

# USER ${USERNAME}

RUN mkdir /application
WORKDIR /application

ENV POETRY_VIRTUALENVS_CREATE=FALSE
RUN pip install poetry
COPY pyproject.toml poetry.lock /application/
RUN poetry install --no-root --without dev

COPY . /application/
RUN poetry install

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/application
EXPOSE 8000
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "application.asgi:app"]