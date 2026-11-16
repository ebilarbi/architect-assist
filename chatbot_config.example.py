"""
Configuration of the IT Architect Assistant chatbot.

Copy this file to `chatbot_config.py`, then edit that copy to change how the chatbot behaves. The notebook
`rag_chatbot.ipynb` reads every setting from here. The chatbot's personality
and rules are in a separate text file, `system_prompt.md`.
"""

# ---------------------------------------------------------------------------
# 1. Link to the retrieval system (built by rag_retrieval_setup.ipynb)
# ---------------------------------------------------------------------------
# File written by the last step of the retrieval notebook. It contains the
# project ID, the region and the resource name of the corpus. Copy it next to
# this notebook, or give its path here.
CORPUS_INFO_FILE = "corpus_info.json"

# ---------------------------------------------------------------------------
# 2. Language model (LLM)
# ---------------------------------------------------------------------------
# Gemini model that writes the answers. Step 3 of the notebook lists the models
# your project can use if this one is not available.
MODEL_NAME = "gemini-3.5-flash"

# Where the model runs. This can differ from the region of the corpus.
#   "eu"     : processed within the European Union (recommended)
#   "global" : best availability, no guarantee on where data is processed
#   or a single region where the model is offered, e.g. "europe-west3"
MODEL_LOCATION = "eu"

# 0.0 = factual and repeatable, 1.0 = more varied. Keep it low for reviews.
TEMPERATURE = 0.2

# Upper limit on the length of one answer (in tokens, about 3/4 of a word each).
MAX_OUTPUT_TOKENS = 8192

# ---------------------------------------------------------------------------
# 3. System prompt
# ---------------------------------------------------------------------------
# Text file holding the chatbot's role and rules. Edit that file, not the code.
SYSTEM_PROMPT_FILE = "system_prompt.md"

# Values inserted into the system prompt wherever {assistant_name},
# {organisation} and {answer_language} appear.
ASSISTANT_NAME = "Archi"
ORGANISATION = "the Architecture team"
ANSWER_LANGUAGE = "the language of the user's last message"

# ---------------------------------------------------------------------------
# 4. Retrieval (what the chatbot looks up before answering)
# ---------------------------------------------------------------------------
# Number of passages of the referential given to the model for each question.
TOP_K = 6

# Maximum vector distance for a passage to be used (smaller = stricter).
# None = no filter. Use the value you calibrated in the retrieval notebook.
VECTOR_DISTANCE_THRESHOLD = None

# Passages longer than this are cut, to keep the prompt small.
MAX_PASSAGE_CHARS = 2500

# In a conversation, a follow-up such as "and for internal APIs?" is not a good
# search query on its own. When True, the model first rewrites it into a
# complete question using the conversation so far. Costs one extra short call.
REWRITE_FOLLOW_UP_QUESTIONS = True

# Number of past exchanges (question + answer) kept in the conversation memory.
MAX_HISTORY_TURNS = 10

# Show the table of sources under each answer.
SHOW_SOURCES = True

# ---------------------------------------------------------------------------
# 5. Attached files (documents added to the conversation)
# ---------------------------------------------------------------------------
# Files attached automatically when the notebook reaches step 9.
# Supported: .docx, .pdf, .txt, .md, .csv, .json, .yaml, .png, .jpg, .webp
# Example: ATTACHMENTS = ["designs/DP-003_Serverless_Music_Analytics_Pipeline.docx"]
ATTACHMENTS = []

# Question asked in step 9 once the files above are attached.
ATTACHMENT_TEST_QUESTION = (
    "Summarise the attached design in five lines, then list the three points "
    "that most need checking against our principles."
)

# Limits. Attached files are sent to the model again at every question for as
# long as they stay attached, so large files make each question slower and
# more expensive.
MAX_ATTACHMENTS = 5
MAX_ATTACHMENT_MB = 15
MAX_ATTACHMENT_CHARS = 300_000   # for text and Word files

# When True and files are attached, the search query sent to the referential
# is written by the model with the files in view. Costs one extra call that
# includes the files. Set to False to search with the question alone.
USE_ATTACHMENTS_FOR_SEARCH = True

# ---------------------------------------------------------------------------
# 6. Design document review
# ---------------------------------------------------------------------------
# Path of a design document to review in step 10 (.docx, .pdf, .txt or .md).
# Leave empty to skip that step.
REVIEW_DOCUMENT_PATH = ""

# Upper limit on the number of design decisions analysed in one document.
# Each decision costs one retrieval and one model call.
MAX_DECISIONS = 25

# Passages retrieved for each design decision.
REVIEW_TOP_K = 4

# The only verdicts the chatbot may give. Keep "NOT COVERED": without it the
# model stretches an unrelated principle to fit.
VERDICTS = ["COMPLIANT", "NON-COMPLIANT", "NOT COVERED"]

# Where the review table is saved.
REVIEW_OUTPUT_FILE = "design_review.csv"

# ---------------------------------------------------------------------------
# 7. Tests and outputs
# ---------------------------------------------------------------------------
# Questions used by the notebook to check the chatbot. The second one is a
# follow-up on purpose, to test the conversation memory.
# TODO: replace with questions that match your referential.
TEST_QUESTIONS = [
    "What are our principles for exposing an API to the internet?",
    "And for APIs that are only used internally?",
]

# File where step 12 saves the conversation.
TRANSCRIPT_FILE = "chat_transcript.json"
