import os
from flask import Flask

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "ProgreeApp")
APP_ENV = os.getenv("APP_ENV", "development")


@app.route("/")
def home():
    return f"Hello from {APP_NAME} running in {APP_ENV} mode!"


@app.route("/health")
def health():
    return {"status": "ok"}, 200


def add(a, b):
    """Tiny pure function so we have something to unit-test."""
    return a + b


if __name__ == "__main__":
    port = int(os.getenv("PORT", "4545"))
    app.run(host="0.0.0.0", port=port)
