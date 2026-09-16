# Task 3 | Automated CI/CD Deployment Pipeline

A production-ready Flask service with automated linting, testing, Docker image builds, and deployment status reporting through GitLab CI/CD.

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.3-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Docker-ready-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![GitLab CI](https://img.shields.io/badge/GitLab_CI/CD-enabled-FC6D26?logo=gitlab&logoColor=white)](https://docs.gitlab.com/ee/ci/)
[![Tests](https://img.shields.io/badge/Tests-3_passing-2EA44F?logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Pylint](https://img.shields.io/badge/Pylint-10.00%2F10-2EA44F?logo=python&logoColor=white)](https://pylint.readthedocs.io/)

## What This Project Does

This project fulfills Task 3 by running an automated workflow whenever code is pushed to the remote repository. GitLab Runner checks out the code, analyzes it, tests it, builds a Docker image, and reports the deployment result in the GitLab pipeline dashboard.

The source is stored in GitHub for version control and sharing. GitLab CI executes the pipeline defined in `.gitlab-ci.yml`.

## Application Features

- Flask web application served by Gunicorn.
- Home page with configurable application name and environment.
- JSON health endpoint for monitoring.
- Unit tests for the application routes and `add` function.
- Production Docker image based on Python 3.12.

## Task 3 Requirements

### Automated remote workflow

Every push starts the lint and test jobs. Pushes to `main` also enable the Docker build and deployment stages.

### Automatic code checkout

GitLab Runner automatically checks out the commit that triggered the pipeline before executing each job.

### Static analysis

The `lint` job installs the project dependencies and runs:

```bash
python -m pylint app.py
```

### Unit testing

The `unit_test` job runs the Pytest suite and publishes `report.xml` as a JUnit test report:

```bash
python -m pytest -v tests/ --junitxml=report.xml
```

### Docker build and integration

The `build_image` job builds the production image. When GitLab registry credentials are available, it logs in and pushes the image using the commit SHA as its tag.

### Deployment status reporting

The manual `deploy` job prints the deployment environment, commit SHA, image name, and pipeline URL to the GitLab job log. These results are visible from the GitLab pipeline dashboard.

## Pipeline Stages

```text
Push to repository
       |
       v
    Lint  --->  Test  --->  Build image  --->  Deploy status
```

The pipeline is configured for a GitLab Shell Runner. Python jobs create a temporary virtual environment. The build job downloads the Docker CLI and uses the runner's mounted Docker socket.

## Project Structure

```text
.
├── app.py             Flask application
├── Dockerfile         Production container definition
├── requirements.txt   Pinned Python dependencies
├── tests/
│   └── test_app.py    Automated tests
├── .gitlab-ci.yml     GitLab CI/CD pipeline
├── .pylintrc          Pylint configuration
└── .dockerignore      Docker build exclusions
```

## Requirements

Install these tools before running the project locally:

- Python 3.12 or newer
- Docker Desktop
- Git

The project uses Flask, Gunicorn, Pytest, and Pylint. Exact versions are pinned in `requirements.txt`.

## Run Locally

### Linux or Git Bash

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

The development server runs at:

```text
http://localhost:4545
```

## Configuration

The application supports these environment variables:

- `APP_NAME` changes the name shown on the home page. Default: `ProgreeApp`.
- `APP_ENV` changes the displayed environment. Default: `development`.
- `PORT` changes the development server port. Default: `4545`.

Example:

```bash
APP_NAME=Task3 APP_ENV=staging PORT=5000 python app.py
```

## Run Tests and Lint

```bash
python -m pytest -v tests/
python -m pylint app.py
```

Expected result:

```text
3 passed
Your code has been rated at 10.00/10
```

## Run with Docker

Build the production image:

```bash
docker build -t progreeapp:local .
```

Start the container:

```bash
docker run --rm --name progreeapp -p 4545:4545 progreeapp:local
```

Test the health endpoint:

```bash
curl http://localhost:4545/health
```

Expected response:

```json
{"status":"ok"}
```

Open the application at:

```text
http://localhost:4545
```

## GitLab CI/CD Jobs

The pipeline file contains four jobs:

- `lint`: runs Pylint against `app.py`.
- `unit_test`: runs Pytest and stores the JUnit report.
- `build_image`: builds and optionally pushes the Docker image.
- `deploy`: manually prints the deployment status report.

To view results, open the GitLab project and select **Build > Pipelines**. Open a pipeline to see each job log and its status. Click the play button on `deploy` after the earlier stages pass.

## Health Endpoint

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
git add .
git commit -m "Describe your change"
git push
```

Keep tests and lint passing before pushing. The CI pipeline repeats these checks automatically.

## License

No license has been selected for this educational project yet.
