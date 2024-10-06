FROM python:3.12-slim

RUN apt-get update && apt-get install -y curl
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH "$PATH:/root/.local/bin"
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

ENV PYTHONPATH "$PYTHONPATH:/app/src"

COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-root

COPY . .

ENTRYPOINT ["python", "-u"]

CMD ["phase2.py"]
