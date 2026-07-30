# import os
# import time

# from dotenv import load_dotenv
# from google import genai
# from config import MODEL_NAME

# # Load environment variables
# load_dotenv()

# # Read API key
# api_key = os.getenv("GEMINI_API_KEY")

# if not api_key:
#     raise ValueError(
#         "GEMINI_API_KEY not found. Please add it to your .env file."
#     )

# # Create Gemini client
# client = genai.Client(api_key=api_key)

# MAX_RETRIES = 3
# RETRY_DELAY = 2  # seconds


# def generate_response(prompt: str, text: str) -> str:
#     """
#     Sends a request to Gemini and returns the generated text.
#     Retries automatically if a temporary error occurs.
#     """

#     full_prompt = f"""
# {prompt}

# Content:
# {text}
# """

#     for attempt in range(MAX_RETRIES):
#         try:
#             response = client.models.generate_content(
#                 model=MODEL_NAME,
#                 contents=full_prompt,
#             )

#             return response.text

#         except Exception as e:

#             print(
#                 f"Attempt {attempt + 1}/{MAX_RETRIES} failed: {e}"
#             )

#             if attempt == MAX_RETRIES - 1:
#                 raise RuntimeError(
#                     f"Error communicating with Gemini after {MAX_RETRIES} attempts: {e}"
#                 )

#             time.sleep(RETRY_DELAY)
import os
from typing import Optional, Type

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel
from langchain_core.runnables import Runnable

from config import MODEL_NAME

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found. Please add it to your .env file."
    )

llm = ChatGoogleGenerativeAI(
    model=MODEL_NAME,
    google_api_key=api_key,
    temperature=0.2,
)

PROMPT_TEMPLATE = PromptTemplate.from_template(
    """
{prompt}

Content:
{content}
"""
)


def generate_response(
    prompt: str,
    text: str,
    output_model: Optional[Type[BaseModel]] = None,
):
    """
    Sends a request using LangChain and returns either
    plain text or a structured Pydantic object.
    """

    full_prompt = PROMPT_TEMPLATE.format(
        prompt=prompt,
        content=text,
    )

    try:

        if output_model:

            chain: Runnable = (
                PROMPT_TEMPLATE
                | llm.with_structured_output(output_model)
            )

            return chain.invoke(
                {
                    "prompt": prompt,
                    "content": text,
                }
            )
        
        chain: Runnable = (
            PROMPT_TEMPLATE
            | llm
        )

        response = chain.invoke(
            {
                "prompt": prompt,
                "content": text,
            }
        )

        return response.content

    except Exception as e:
        raise RuntimeError(
            f"Error communicating with Gemini: {e}"
        ) from e