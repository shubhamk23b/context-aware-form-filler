# 📝 Context Form Filler Agent

> An AI-powered document processing system that extracts information from unstructured PDF and image documents and converts it into structured, validated form data.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)

The system combines **OCR, PDF text extraction, LLM-based contextual understanding, structured output generation, and schema validation** to automate manual form-filling workflows.

---

## 📑 Table of Contents

- [Features](#-features)
- [Problem Statement](#-problem-statement)
- [System Architecture](#️-system-architecture)
- [Workflow](#-workflow)
- [AI Agent Architecture](#-ai-agent-architecture)
- [Tech Stack](#️-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [API Reference](#-api-reference)
- [Testing](#-testing)
- [Docker](#-docker)
- [Key Design Decisions](#-key-design-decisions)
- [Reliability](#-reliability)
- [Future Improvements](#-future-improvements)
- [Learning Outcomes](#-learning-outcomes)
- [Author](#-author)

---

## 🚀 Features

- 📄 PDF and image document processing
- 🔍 Automatic text extraction using **PyMuPDF**
- 👁️ OCR support using **Tesseract**
- 🤖 LLM-powered information extraction
- 🧠 Context-aware form filling
- ⚠️ Automatic missing-field detection
- 📦 Structured JSON output
- ✅ Schema-based validation with **Pydantic**
- 🌐 REST API using **FastAPI**
- 🗄️ SQLite database integration
- 🧩 Modular and scalable architecture

---

## 🎯 Problem Statement

Traditional document-based form filling requires users to manually read large documents and transfer relevant information into predefined forms. This process is:

- Time-consuming
- Repetitive
- Error-prone
- Difficult to scale
- Vulnerable to missing information

The Context Form Filler Agent automates this workflow by understanding document content and converting it into structured form data.

---

## 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │    User / Client    │
                    │   PDF / Image File  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       FastAPI       │
                    │      REST API       │
                    └──────────┬──────────┘
                               │
                               ▼
                 ┌───────────────────────────┐
                 │   Document Processing     │
                 └─────────────┬─────────────┘
                               │
                    ┌──────────┴──────────┐
                    │                     │
                    ▼                     ▼
             ┌─────────────┐       ┌─────────────┐
             │   PyMuPDF   │       │  Tesseract  │
             │ PDF Extract │       │     OCR     │
             └──────┬──────┘       └──────┬──────┘
                    │                     │
                    └──────────┬──────────┘
                               ▼
                     ┌──────────────────┐
                     │  Extracted Text  │
                     └────────┬─────────┘
                              │
                              ▼
                  ┌────────────────────────┐
                  │  Context Form Filler   │
                  │       AI Agent         │
                  │    LangChain + LLM     │
                  └────────────┬───────────┘
                               │
                    ┌──────────┴──────────┐
                    │                     │
                    ▼                     ▼
             ┌──────────────┐     ┌───────────────┐
             │    Field     │     │    Missing    │
             │  Extraction  │     │ Field Detect. │
             └──────┬───────┘     └───────┬───────┘
                    │                     │
                    └──────────┬──────────┘
                               ▼
                    ┌────────────────────┐
                    │ Schema Validation  │
                    └──────────┬─────────┘
                               │
                               ▼
                    ┌────────────────────┐
                    │  Structured JSON   │
                    │      Output        │
                    └──────────┬─────────┘
                               │
                               ▼
                    ┌────────────────────┐
                    │     SQLite DB      │
                    └────────────────────┘
```

---

## 🔄 Workflow

1. **Document Upload** — The user uploads a PDF or image through the FastAPI REST API.
2. **Document Processing** — The system picks the extraction method:
   - **PyMuPDF** → text-based (digital) PDFs
   - **Tesseract OCR** → scanned PDFs and images
3. **Text Extraction** — The document is converted into machine-readable text and normalized before being passed to the AI layer.
4. **Contextual Information Extraction** — The Context Form Filler Agent passes the text and the form schema to the LLM, which maps relevant information to predefined form fields.
5. **Missing Field Detection** — If a required field is not found, it is marked as missing instead of generating unsupported information.
6. **Structured Output** — Extracted information is converted into a predefined JSON structure:

   ```json
   {
     "policy_holder": "Rahul Sharma",
     "date_of_birth": "12 March 1999",
     "address": "Guwahati, Assam",
     "policy_number": null,
     "missing_fields": ["policy_number"]
   }
   ```

7. **Validation** — The generated JSON is validated against the expected schema before being returned to the client.
8. **Storage** — Extracted information and metadata can be stored in SQLite for further processing.

---

## 🧠 AI Agent Architecture

```text
                 Document Text
                      │
                      ▼
              ┌───────────────┐
              │   Prompt +    │
              │  Form Schema  │
              └───────┬───────┘
                      │
                      ▼
                ┌───────────┐
                │    LLM    │
                └─────┬─────┘
                      │
             Context Understanding
                      │
             ┌────────┴────────┐
             ▼                 ▼
       Field Extraction   Missing Fields
             │                 │
             └────────┬────────┘
                      ▼
                JSON Output
                      │
                      ▼
                Validation
```

The agent uses the expected form schema to guide the LLM and produce consistent structured output.

---

## 🛠️ Tech Stack

| Category             | Technology                   |
| -------------------- | ---------------------------- |
| Programming Language | Python                       |
| API Framework        | FastAPI                      |
| LLM Framework        | LangChain                    |
| LLM                  | LLM API / Hugging Face       |
| PDF Processing       | PyMuPDF                      |
| OCR                  | Tesseract                    |
| Database             | SQLite                       |
| API Architecture     | REST                         |
| Validation           | Pydantic / Schema Validation |
| Containerization     | Docker                       |
| Version Control      | Git & GitHub                 |

---

## 📁 Project Structure

```text
context-form-filler-agent/
│
├── app/
│   ├── main.py                    # FastAPI entry point
│   │
│   ├── routes/
│   │   ├── document_routes.py     # Document upload endpoints
│   │   └── form_routes.py         # Form-related endpoints
│   │
│   ├── agents/
│   │   └── form_filler_agent.py   # LangChain + LLM agent
│   │
│   ├── services/
│   │   ├── document_service.py    # Document handling & routing
│   │   ├── extraction_service.py  # PyMuPDF text extraction
│   │   └── ocr_service.py         # Tesseract OCR
│   │
│   ├── prompts/
│   │   └── form_prompts.py        # LLM prompt templates
│   │
│   ├── schemas/
│   │   └── form_schema.py        # Pydantic form schemas
│   │
│   ├── database/
│   │   ├── database.py            # DB connection/session
│   │   └── models.py              # SQLite models
│   │
│   └── utils/
│       └── helpers.py             # Shared helper functions
│
├── data/
│   ├── uploads/                   # Uploaded documents
│   └── processed/                 # Processed outputs
│
├── tests/
│
├── .env.example
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.10+
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed on your system
  - **Ubuntu/Debian:** `sudo apt install tesseract-ocr`
  - **macOS:** `brew install tesseract`
  - **Windows:** download the installer from the [UB Mannheim builds](https://github.com/UB-Mannheim/tesseract/wiki) and add it to your `PATH`
- An API key for your chosen LLM provider

### 1. Clone the Repository

```bash
git clone https://github.com/shubhamk23b/context-form-filler-agent.git
cd context-form-filler-agent
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
```

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy the example file and fill in your values:

```bash
cp .env.example .env
```

```env
LLM_API_KEY=your_api_key
DATABASE_URL=sqlite:///./app.db
```

> ⚠️ Never commit your `.env` file to GitHub.

### 5. Run the Application

```bash
uvicorn app.main:app --reload
```

| Resource                  | URL                         |
| ------------------------- | --------------------------- |
| API                       | http://localhost:8000       |
| Interactive API docs      | http://localhost:8000/docs  |

---

## 🔌 API Reference

### Upload Document

```http
POST /documents/upload
```

**Request** — `multipart/form-data`

| Field | Type | Description                      |
| ----- | ---- | -------------------------------- |
| file  | File | PDF or image document to process |

**Example (cURL)**

```bash
curl -X POST "http://localhost:8000/documents/upload" \
  -F "file=@document.pdf"
```

**Example Response**

```json
{
  "status": "success",
  "data": {
    "policy_holder": "Rahul Sharma",
    "date_of_birth": "12 March 1999",
    "address": "Guwahati, Assam"
  },
  "missing_fields": ["policy_number"]
}
```

---

## 🧪 Testing

Run the test suite:

```bash
pytest
```

The test suite can cover:

- PDF text extraction
- OCR processing
- Form field extraction
- Missing field detection
- JSON validation
- API endpoints

---

## 🐳 Docker

Build the image:

```bash
docker build -t context-form-filler-agent .
```

Run the container (passing your environment variables):

```bash
docker run -p 8000:8000 --env-file .env context-form-filler-agent
```

---

## 💡 Key Design Decisions

| Choice             | Why                                                                                       |
| ------------------ | ----------------------------------------------------------------------------------------- |
| **PyMuPDF**        | Fast extraction of text from digital PDF documents.                                       |
| **Tesseract OCR**  | Fallback for scanned documents and images where PDF extraction is not enough.             |
| **LLM**            | Contextual, semantic extraction instead of relying only on keyword matching.              |
| **LangChain**      | Structures the LLM workflow and manages prompts and extraction logic.                     |
| **FastAPI**        | Exposes the document-processing pipeline through clean, documented REST APIs.            |
| **Structured JSON**| Predictable output that other applications or services can easily consume.               |

---

## 🔒 Reliability

The system is designed to minimize incorrect data generation by:

- Using predefined form fields
- Detecting missing information
- Validating structured outputs
- Separating document extraction from AI processing
- Avoiding unsupported assumptions

For production deployment, additional human verification and confidence scoring can be introduced.

---

## 🚀 Future Improvements

- [ ] Field-level confidence scores
- [ ] Human-in-the-loop verification
- [ ] Advanced document classification
- [ ] RAG-based policy information retrieval
- [ ] Vector database integration
- [ ] Multi-document processing
- [ ] Table extraction
- [ ] Source/reference tracking for extracted fields
- [ ] LLM evaluation pipeline
- [ ] Monitoring and observability
- [ ] AWS deployment
- [ ] Asynchronous document processing
- [ ] Role-based access control

---

## 📚 Learning Outcomes

This project demonstrates practical experience with:

- Generative AI and LLM integration
- AI agents and prompt engineering
- LangChain
- OCR and PDF processing
- Structured information extraction
- FastAPI and REST API development
- Pydantic / schema validation
- Database integration
- Modular backend architecture
- Docker

---

## 👨‍💻 Author

**Shubham Kanojiya**
AI/ML & Backend Developer

GitHub: [@shubhamk23b](https://github.com/shubhamk23b)

---

## ⭐ Project Summary

**Context Form Filler Agent** is an AI-powered document intelligence system that automatically converts unstructured PDF/image documents into structured form data using **OCR, PDF extraction, LLM-based contextual understanding, and schema validation**, exposed through a modular **FastAPI backend**.

If you find this project useful, consider giving it a ⭐ on GitHub!
