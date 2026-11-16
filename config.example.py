"""
Configuration constants for the IT Architect Assistant retrieval system.

Copy this file to `config.py`, then edit it. `config.py` is the ONLY file you need to edit. The notebook `rag_retrieval_setup.ipynb`
reads every setting from here. Values marked "TODO" must be changed before the
first run.
"""

# ---------------------------------------------------------------------------
# 1. Google Cloud project
# ---------------------------------------------------------------------------
# TODO: the ID (not the display name) of your GCP project.
PROJECT_ID = "your-gcp-project-id"

# Region where the corpus (the index) is stored and queried.
# europe-west4 (Netherlands) and europe-west3 (Frankfurt) are the two European
# regions where RAG Engine is generally available.
LOCATION = "europe-west4"

# APIs the notebook enables on the project.
REQUIRED_APIS = [
    "aiplatform.googleapis.com",
]

# ---------------------------------------------------------------------------
# 2. Corpus (the searchable index of the referential)
# ---------------------------------------------------------------------------
# The notebook reuses an existing corpus with this exact display name instead
# of creating a duplicate, so keep it stable.
CORPUS_DISPLAY_NAME = "it-architecture-referential"
CORPUS_DESCRIPTION = (
    "Referential of IT architecture design principles and recommendations, "
    "used to review design documents."
)

# Embedding model that turns each chunk of text into a vector.
# It CANNOT be changed after the corpus is created (you would have to delete
# the corpus and re-import everything).
#   - text-embedding-005              : default, best for English documents
#   - text-multilingual-embedding-002 : choose this if the referential is in
#                                       French or mixes several languages
EMBEDDING_MODEL = "publishers/google/models/text-embedding-005"

# ---------------------------------------------------------------------------
# 3. Source: Google Drive
# ---------------------------------------------------------------------------
# The ID is the last part of the Drive URL:
#   https://drive.google.com/drive/folders/<FOLDER_ID>
#   https://docs.google.com/document/d/<FILE_ID>/edit
# TODO: put at least one folder ID or file ID.
DRIVE_FOLDER_IDS = [
    "your-drive-folder-id",
]
DRIVE_FILE_IDS = [
    # "an-individual-file-id",
]

# ---------------------------------------------------------------------------
# 4. Chunking (how documents are cut into pieces before indexing)
# ---------------------------------------------------------------------------
# Sizes are in tokens (1 token is roughly 3/4 of an English word).
# Smaller chunks = more precise matches; larger chunks = more context per match.
CHUNK_SIZE = 512
CHUNK_OVERLAP = 100

# Throttle for embedding calls during import. Lower it if you hit quota errors.
MAX_EMBEDDING_REQUESTS_PER_MIN = 1000

# ---------------------------------------------------------------------------
# 5. Retrieval
# ---------------------------------------------------------------------------
# Number of chunks returned for each question.
TOP_K = 5

# Maximum vector distance for a chunk to be returned (smaller = stricter).
# Set to None to disable the filter and always get TOP_K results, which is
# useful while you are still calibrating.
VECTOR_DISTANCE_THRESHOLD = None

# ---------------------------------------------------------------------------
# 6. Outputs and safety
# ---------------------------------------------------------------------------
# File where the notebook saves the corpus resource name, so the chatbot
# (next stage of the project) can find the index without recreating it.
CORPUS_INFO_FILE = "corpus_info.json"

# Safety lock for the clean-up cell at the end of the notebook.
# The corpus is only deleted when this is True.
ALLOW_DELETE_CORPUS = False
