# ---------- STAGE 1: BUILDER ----------
FROM python:3.12-slim AS builder

WORKDIR /build

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ---------- STAGE 2: RUNTIME ----------

FROM python:3.12-slim AS runtime

RUN useradd --create-home --shell /bin/bash appuser

WORKDIR /app

COPY --from=builder /install /usr/local
COPY app.py .

ENV APP_NAME=ProgreeApp \
    APP_ENV=production \
    PORT=4545 \
    PYTHONUNBUFFERED=1

USER appuser

EXPOSE 4545

CMD ["gunicorn", "--bind", "0.0.0.0:4545", "app:app"]