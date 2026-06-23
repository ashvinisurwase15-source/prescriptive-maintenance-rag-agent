# Prescriptive Maintenance RAG Agent

## Project Overview

Prescriptive Maintenance RAG Agent is an AI-powered maintenance assistant that analyzes machinery manuals and alert data to provide maintenance recommendations. The system uses Retrieval-Augmented Generation (RAG) with ChromaDB and Gemini LLM to retrieve relevant maintenance information and generate intelligent recommendations.

---

## Technologies Used

* Python
* FastAPI
* ChromaDB
* LangChain
* Hugging Face Embeddings
* Google Gemini 2.5 Flash
* Uvicorn
* python-dotenv

---

## Features Implemented

### RAG Pipeline

* Document Loading
* Document Chunking
* Embedding Generation
* ChromaDB Vector Storage
* Semantic Search
* Document Retrieval

### AI Features

* Gemini LLM Integration
* Context-Aware Maintenance Recommendations

### Maintenance Analytics

* Health Score Calculation
* Failure Risk Prediction
* Priority Classification
* Severity Classification

### Backend Features

* FastAPI REST API
* Swagger UI Testing
* JSON Response Generation

---

## Project Structure

app/
├── api/
├── models/
├── rag/
│ ├── loader.py
│ ├── chunker.py
│ ├── retriever.py
│ └── vector_store.py
├── services/
│ ├── health_score.py
│ ├── failure_risk.py
│ ├── priority_classifier.py
│ ├── severity_classifier.py
│ └── llm_recommendation.py

---

## System Workflow

1. User submits a maintenance query.
2. ChromaDB retrieves relevant document chunks.
3. Retrieved context is passed to Gemini.
4. Gemini generates maintenance recommendations.
5. Additional analytics are generated:

   * Health Score
   * Failure Risk
   * Priority Level
   * Severity Level
6. Results are returned through FastAPI.

---

## API Endpoint

### POST /query

Sample Request:

{
"query": "high machine temperature"
}

Sample Response:

{
"query": "high machine temperature",
"health": {
"health_score": 80,
"status": "Healthy"
},
"failure_risk": {
"risk_score": 40,
"risk_level": "Medium"
},
"priority": {
"priority_score": 30,
"priority_level": "Medium"
},
"severity": {
"severity_score": 25,
"severity_level": "Medium"
},
"recommendation": "AI-generated maintenance recommendation"
}

---

## Current Progress

Completed Modules:

* Project Setup
* GitHub Repository Setup
* FastAPI Configuration
* Document Loader
* Document Chunking
* ChromaDB Integration
* Semantic Search
* Retrieval Pipeline
* Health Score Module
* Failure Risk Module
* Priority Classification Module
* Severity Classification Module
* Gemini Recommendation Engine
* API Testing using Swagger UI

---

## Author

Ashvini Surwase

AI Internship Project – Prescriptive Maintenance RAG Agent
