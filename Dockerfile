# Stage 1: Builder / Dependency Setup
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

# Install dependencies to user directory to keep runner stage clean
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 2: Runner
FROM python:3.11-slim AS runner

WORKDIR /app

# Install chromium and chromium-driver for running headless UI tests
RUN apt-get update && apt-get install -y --no-install-recommends \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Copy user-installed dependencies from builder stage
COPY --from=builder /root/.local /root/.local

# Adjust path to find global commands
ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

# Copy the rest of the application files
COPY . .

# Run both unit and UI tests using pytest
CMD ["pytest", "-v"]
