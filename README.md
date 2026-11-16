# IT Architect Assistant

A RAG (retrieval-augmented generation) assistant for IT architects, built on Google Cloud.
It answers questions about your organisation's architecture principles and reviews design
documents against them, citing the passages it relied on.

```
Google Drive referential ──► RAG Engine corpus ──► retrieval ──► Gemini ──► answer with citations
```

## Project description

The project has two stages, each in its own notebook.

| Stage | Notebook | What it does |
|---|---|---|
| 1. Retrieval | `rag_retrieval_setup.ipynb` | Imports the referential from Google Drive, cuts it into chunks, embeds them and builds a searchable corpus on Vertex AI RAG Engine. Tests retrieval with sample questions and saves the corpus reference to `corpus_info.json`. |
| 2. Chatbot | `rag_chatbot.ipynb` | Connects a Gemini model to the corpus. Answers questions with `[S1]`-style citations, remembers the conversation, accepts attached files, and reviews a design document decision by decision (verdicts: COMPLIANT, NON-COMPLIANT, NOT COVERED). |

### Files

| File | Purpose |
|---|---|
| `config.example.py` | Template for the retrieval settings (project, region, Drive IDs, chunking). |
| `chatbot_config.example.py` | Template for the chatbot settings (model, temperature, top K, attachments, review). |
| `test_queries.py` | Questions used to check retrieval in stage 1. Edit freely. |
| `system_prompt.md` | The chatbot's role and rules. Edit this file, not the code. |
| `config.py`, `chatbot_config.py` | Your local copies of the templates. Git-ignored. |
| `corpus_info.json` | Written by stage 1, read by stage 2. Git-ignored. |

## Prerequisites

- Python 3.12 and [`uv`](https://docs.astral.sh/uv/)
- The [`gcloud` CLI](https://cloud.google.com/sdk/docs/install)
- A GCP project with billing enabled and the **Vertex AI User** role (`roles/aiplatform.user`).
  Enabling the API also needs *Service Usage Admin* or Owner.
- Edit rights on the Google Drive folder that holds the referential (you must share it with a service account)

## Setup

1. **Create the environment and install dependencies**

   ```bash
   uv sync
   ```

   The notebooks install the Google SDKs (`google-cloud-agentplatform`, `google-cloud-storage`)
   in their Step 0 cell. Use the project's `.venv` as the notebook kernel.

2. **Create your local config files**

   ```bash
   cp config.example.py config.py
   cp chatbot_config.example.py chatbot_config.py
   ```

3. **Edit `config.py`**: set `PROJECT_ID`, and put your Drive folder ID in `DRIVE_FOLDER_IDS`
   (the last part of `https://drive.google.com/drive/folders/<FOLDER_ID>`).
   Choose `text-multilingual-embedding-002` for `EMBEDDING_MODEL` if your documents are in French or mixed languages.
   The embedding model cannot be changed after the corpus is created.

4. **Authenticate with Google Cloud**

   ```bash
   gcloud auth login
   gcloud auth application-default login
   gcloud config set project YOUR_PROJECT_ID
   ```

5. **Run the retrieval notebook** (`rag_retrieval_setup.ipynb`) top to bottom.
   In Step 5 it prints a service account address: share your Drive folder with it as **Viewer**.
   If the import reports 0 files, this share is missing.

6. **Run the chatbot notebook** (`rag_chatbot.ipynb`) top to bottom.
   It reads `corpus_info.json` from stage 1.

## Everyday use

- **Add or update documents:** put them in the Drive folder, then re-run Step 6 (import), Step 7 (check) and Step 9 (test) of the retrieval notebook. Unchanged files are skipped.
- **Change test questions:** edit `test_queries.py`, then re-run Step 1 and Step 9.
- **Change the chatbot's behaviour:** edit `chatbot_config.py` or `system_prompt.md`, then re-run Step 1 and the steps that follow.
- **Change chunk size or embedding model:** set a new `CORPUS_DISPLAY_NAME` so a new corpus is created, then re-import.
- **Delete the corpus** (it costs money while it exists): set `ALLOW_DELETE_CORPUS = True` in `config.py` and run the clean-up cell. Your Drive files are never touched.

## Notes

- Notebook outputs are cleared before committing, since they can contain account and project details. Clear them again before you push.
- `config.py`, `chatbot_config.py`, `corpus_info.json`, `design_review.csv` and `chat_transcript.json` are git-ignored on purpose.
