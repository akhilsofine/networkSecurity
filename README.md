# Network Security

A phishing detection project built for network security classification using machine learning and a FastAPI prediction service. The project includes data ingestion, validation, transformation, model training, and API-based predictions.

## Project Overview

This solution is designed to:
- ingest network/security data from MongoDB
- validate incoming data quality and schema compliance
- transform data into training-ready feature sets
- train and evaluate classification models
- deploy a lightweight prediction API

## Tech Stack

- Python 3.11+
- FastAPI
- scikit-learn
- pandas
- NumPy
- MLflow
- MongoDB
- Docker

## Repository Structure

- `networksecurity/` — core implementation for the data pipeline and model logic
- `app.py` — FastAPI application for training and prediction endpoints
- `main.py` — training pipeline entrypoint
- `setup.py` — package configuration for installation
- `requirements.txt` — project dependencies
- `Dockerfile` — container build configuration
- `data_schema/` — schema definitions and configuration files
- `templates/` — HTML templates for API responses

## Local Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate      # Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   ```bash
   export MONGODB_URL_KEY="your_mongodb_connection_string"
   ```

4. Run the API locally:
   ```bash
   python app.py
   ```

5. Train the model:
   ```bash
   python main.py
   ```

## API Endpoints

- `GET /` — redirects to FastAPI docs
- `GET /train` — triggers the training pipeline
- `POST /predict` — uploads a CSV file and returns the prediction result table

## Docker

Build the container:
```bash
docker build -t networksecurity .
```

Run the container:
```bash
docker run -p 8000:8000 --env MONGODB_URL_KEY="your_mongodb_connection_string" networksecurity
```

## Notes

This repository is organized for clean production-style deployment, with separate focuses for infrastructure, application logic, and deployment workflows.

