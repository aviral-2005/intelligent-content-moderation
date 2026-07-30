
from llm.client import generate_response
from llm.prompt.content_analyzer import CONTENT_ANALYZER_PROMPT
from llm.validator import (
    validate_response,
    REQUIRED_CONTENT_FIELDS,
)
from models.ai_models import ContentAnalysis


def analyze_content(content: str) -> ContentAnalysis:

    # AI Analysis
    ai_analysis = generate_response(
        CONTENT_ANALYZER_PROMPT,
        content,
        output_model=ContentAnalysis,
    )

    # Convert Pydantic model to dictionary
    analysis = ai_analysis.model_dump()

    # Add Python-generated metadata
    analysis["original_content"] = content
    analysis["word_count"] = len(content.split())
    analysis["character_count"] = len(content)

    # Validate final response
    analysis = validate_response(
        analysis,
        REQUIRED_CONTENT_FIELDS,
    )

    return ContentAnalysis(**analysis)