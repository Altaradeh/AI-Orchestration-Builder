# Ember AI – Worksheet Generator (MVP)

This repository contains a minimal MVP for a **privacy-first AI worksheet generator**.
It is backend-only and designed for local execution and review.

---

## Requirements

- Python 3.10+
- Git
- Poetry

---

## Installation


1. Install dependencies

    poetry install

2. Set environment variables

Create a `.env` file in the project root:

    OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
    OPENAI_MODEL=gpt-4o-mini

(Optional – only if you want to test opt-in persistence)

    SUPABASE_URL=https://xxxx.supabase.co
    SUPABASE_SERVICE_ROLE_KEY=xxxxxxxxxxxxxxxx

---

## Running the Project

Run the local test script:

    poetry run python src/run_local.py

This will:
- Run a single worksheet-generation workflow
- Print a schema-validated JSON output OR a structured refusal
- Optionally save the result if opt-in persistence is enabled

---

