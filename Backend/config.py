import os

from dotenv import load_dotenv

load_dotenv()


# ==========================
# Gemini Configuration
# ==========================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

MODEL_NAME = "gemini-2.5-flash"

# TEMPERATURE = 0.2


# ==========================
# Review Thresholds
# ==========================

AUTO_APPROVE_THRESHOLD = 0.30

REVISION_THRESHOLD = 0.70


# ==========================
# Application
# ==========================

APP_NAME = "Intelligent Content Review & Moderation Workflow"

APP_VERSION = "1.0.0"