# Multi-stage build for CEC Lang

# Stage 1: Build React frontend
FROM node:20-alpine AS frontend-builder
WORKDIR /app/frontend
COPY interfaces/react-frontend/package*.json ./
RUN npm install
COPY interfaces/react-frontend/ ./
RUN npm run build

# Stage 2: Python backend with built frontend
FROM python:3.11-slim
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir fastapi uvicorn python-multipart

# Copy application code
COPY core/ ./core/
COPY data/ ./data/
COPY api/ ./api/
COPY interfaces/ ./interfaces/

# Copy built frontend from Stage 1 (overwrites source with built files)
COPY --from=frontend-builder /app/frontend/dist ./interfaces/react-frontend/dist

# Expose port
EXPOSE 8080

# Set environment variables
ENV PORT=8080
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["python", "-m", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8080"]
