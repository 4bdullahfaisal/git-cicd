# Flask CI/CD Demo

A small Flask web service used to demonstrate a complete GitLab CI/CD workflow. The project exposes a home page, a health check, and a pure Python function covered by automated tests.

## Features

- Flask application served by Gunicorn in production.
- `GET /` returns an environment-aware greeting.
- `GET /health` returns a JSON health response.
- Unit tests for the application and `add` function.
- Pylint static analysis.
- Multi-stage CI pipeline with lint, test, build, and deploy stages.
- Multi-stage Docker image based on Python 3.12.

## Task 3: Multi-Stage Automated CI/CD Deployment Pipeline

### Objective

Automate testing and integration whenever code is pushed to the remote GitLab repository. The pipeline validates the application, builds a deployable Docker image, and reports deployment status.

### Requirement Mapping

| Assignment requirement | Project implementation |
| --- | --- |
| Automated CI/CD workflow | `.gitlab-ci.yml` defines the complete pipeline. |
| Remote push execution | Lint and test run for push pipelines; build and deploy run for pushes to `main`. |
| Automated code checkout | GitLab Runner checks out the pushed commit before every job. |
| Static application linting | The `lint` job installs Pylint and runs `python -m pylint app.py`. |
| Unit-testing suite | The `unit_test` job runs Pytest and publishes `report.xml` as a JUnit artifact. |
| Build and integration | The `build_image` job builds the production Docker image and pushes it when registry credentials are available. |
| Deployment output status | The `deploy` job logs environment, commit, image, and pipeline URL. |
| Execution board visibility | GitLab Pipelines and job logs show each stage's status and output. |

The project uses GitLab CI as the automation platform and a GitLab Shell Runner. GitHub stores the project source for sharing, while GitLab executes the CI/CD pipeline defined in `.gitlab-ci.yml`.

## Project Structure

```text
.
├── app.py
├── Dockerfile
├── requirements.txt
├── tests/
│   └── test_app.py
└── .gitlab-ci.yml
```

## Requirements

- Python 3.12 or newer
- Docker Desktop for container use
- Git

Dependencies are pinned in `requirements.txt`: Flask, Gunicorn, Pytest, and Pylint.

## Run Locally with Python

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

On Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

The application listens on `http://localhost:4545` by default.

## Configuration

| Variable | Default | Purpose |
| --- | --- | --- |
| `APP_NAME` | `ProgreeApp` | Name shown on the home page |
| `APP_ENV` | `development` | Environment shown on the home page |
| `PORT` | `4545` | Development server port |

Example:

```bash
APP_NAME=Demo APP_ENV=staging PORT=5000 python app.py
```

## Tests and Lint

```bash
python -m pytest -v tests/
python -m pylint app.py
```

The expected result is three passing tests and a clean Pylint report.

## Run with Docker

```bash
docker build -t progreeapp:local .
docker run --rm --name progreeapp -p 4545:4545 progreeapp:local
```

Verify the service:

```bash
curl http://localhost:4545/health
```

Expected response:

```json
{"status":"ok"}
```

## CI/CD Pipeline

The `.gitlab-ci.yml` file defines four stages:

1. **Lint** installs dependencies and runs Pylint.
2. **Test** runs Pytest and stores a JUnit report.
3. **Build** builds the Docker image and pushes it when registry credentials are available.
4. **Deploy** records deployment status and is manual on `main`.

The pipeline is configured for a GitLab Shell runner. Python jobs create a temporary virtual environment. The build job downloads the Docker CLI and uses the runner's mounted Docker socket.

## Health Check

```http
GET /health
```

Successful response:

```json
{"status":"ok"}
```

## Development Workflow

```bash
git clone <repository-url>
cd task3
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -v tests/
python -m pylint app.py
```

Keep tests and lint passing before pushing changes. CI runs the same checks automatically.

## License

No license has been selected for this educational project yet.
