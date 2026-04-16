# Official Airflow base image with Python 3.13
# This already includes Airflow installed and properly configured
FROM apache/airflow:3.2.0-python3.13

# Install Poetry (dependency manager)
# Version is pinned to ensure reproducibility across environments
ENV POETRY_VERSION=2.1.3 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

# Set working directory inside the container
WORKDIR /opt/airflow

# Copy dependency definition files into the container
# poetry.lock ensures all dependencies are installed with exact versions
COPY pyproject.toml poetry.lock /opt/airflow/

# Install Poetry and project dependencies
# --without dev → install only production dependencies
# --no-root → do not install the project itself as a package
# Dependencies are installed directly into the container environment
RUN pip install --no-cache-dir "poetry==$POETRY_VERSION" && \
    poetry install --no-root