FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV JAVA_HOME /usr/lib/jvm/default-java

RUN apt-get update && \
    apt-get install -y default-jdk-headless && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install uv

FROM base AS builder

COPY pyproject.toml .

RUN uv pip install --system --no-cache .

FROM base AS final

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

COPY src/ .

CMD ["python", "-m", "pulse_analytics.main"]
