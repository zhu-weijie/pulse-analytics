FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install uv

FROM base AS builder

COPY pyproject.toml .

RUN uv pip install --system --no-cache .

FROM base AS final

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

COPY src/ .

CMD ["python", "-c", "print('Setup complete. Ready for next issue.')"]
