# Stage 1: Build
FROM python:3.10.10-slim-bullseye AS builder

ENV APP_NAME=ordermanager-api
ARG PROJECT_DIR=/app/backend
WORKDIR ${PROJECT_DIR}
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV TZ America/Sao_Paulo
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONFAULTHANDLER=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y build-essential libpq-dev

# Cria o ambiente virtual
RUN python -m venv venv

# Ativa o ambiente virtual
ENV PATH=${PROJECT_DIR}/venv/bin:$PATH

COPY requirements.txt ${PROJECT_DIR}/requirements.txt
RUN pip install -r ${PROJECT_DIR}/requirements.txt

# Stage 2: Run
FROM python:3.10.10-slim-bullseye

ENV APP_NAME=ordermanager-api
ARG PROJECT_DIR=/app/backend
WORKDIR ${PROJECT_DIR}
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV TZ America/Sao_Paulo
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONFAULTHANDLER=1
ENV PYTHONUNBUFFERED=1

# Copia o ambiente virtual do builder
COPY --from=builder ${PROJECT_DIR}/venv ${PROJECT_DIR}/venv

# Ativa o ambiente virtual
ENV PATH=${PROJECT_DIR}/venv/bin:$PATH

# Copia apenas o código fonte da aplicação
COPY ./backend ${PROJECT_DIR}

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
