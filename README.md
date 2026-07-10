# Continuous Integration and Continuous Deployment Pipelines

This project implements a fully integrated Continuous Integration and Continuous Deployment (CI/CD) testing pipeline for i2i Academy. It features unit tests and automated headless Selenium UI tests running on a Python codebase, complete with a GitHub Actions workflow configuration and a multi-stage Docker environment.

## Purpose

The main objective of this repository is to demonstrate how to automate the validation of business logic and user interface functionality using pytest and Selenium in a headless browser environment. These tests run sequentially inside a GitHub Actions runner and are packaged into a multi-stage Docker container to ensure environment consistency between local development and production.

## Directory Structure

```text
.
├── .github/
│   └── workflows/
│       └── ci-cd.yml      # GitHub Actions CI/CD pipeline configuration
├── tests/
│   ├── test_logic.py      # pytest unit test for tax_calculator
│   └── test_ui.py         # Selenium headless UI test
├── .gitignore             # Git ignore definitions (excluding SOLUTION.md and screenshots)
├── Dockerfile             # Multi-stage Docker build configuration
├── README.md              # Project documentation (English)
├── requirements.txt       # Python project dependencies
├── SOLUTION.md            # Internship report (Turkish, git-ignored)
└── tax_calculator.py      # SOLID-compliant telecom tax calculator module
```

## Prerequisite Setup

To run this project locally, ensure you have the following prerequisites installed:
- Python 3.8 or higher
- Google Chrome browser (for local UI testing)
- Docker Desktop (optional, for containerized testing)

Follow these steps to configure your environment:
1. Clone the repository to your local machine.
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Local Run Commands

Once the prerequisites are installed and the virtual environment is active, execute the testing suite using pytest:

- **Run all tests (Unit + UI)**:
  ```bash
  pytest
  ```

- **Run only unit tests**:
  ```bash
  pytest tests/test_logic.py
  ```

- **Run only UI tests**:
  ```bash
  pytest tests/test_ui.py
  ```

## Docker Execution Instructions

The project features a multi-stage Dockerfile that compiles dependencies in the builder stage and sets up a headless Chromium/ChromeDriver environment in the runner stage.

1. **Build the Docker Image**:
   ```bash
   docker build -t i2i-cicd-pipeline .
   ```

2. **Run the Docker Container**:
   ```bash
   docker run --rm i2i-cicd-pipeline
   ```
