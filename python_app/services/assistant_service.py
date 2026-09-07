"""Business logic for the library conversational assistant."""

from typing import Any
import time
from python_app.llm.response_generator import generate_response
from python_app.llm.smollm_model import load_smollm_model
from python_app.llm.smollm_response_generator import generate_smollm_response
from python_app.services.search_service import search_catalogue


DEFAULT_TOP_K = 3

_tokenizer, _model = load_smollm_model()


def process_question(
    question: str,
    top_k: int = DEFAULT_TOP_K,
) -> dict[str, Any]:
    """Process a library question and generate a natural-language answer.

    Args:
        question: Natural-language question from the user.
        top_k: Maximum number of catalogue results to retrieve.

    Returns:
        Dictionary containing the question, library data, and answer.

    Raises:
        ValueError: If the question is invalid.
    """
    if not question or not question.strip():
        raise ValueError("Question cannot be empty.")

    if top_k <= 0:
        raise ValueError("top_k must be greater than zero.")

    cleaned_question = question.strip()

    search_start = time.perf_counter()

    results = search_catalogue(
        query=cleaned_question,
        top_k=top_k,
    )

    search_time = time.perf_counter() - search_start

    print(f"Search time: {search_time:.2f} seconds")

    if not results:
        return {
            "question": cleaned_question,
            "library_data": [],
            "answer": (
                "Sorry, I couldn't find a matching book "
                "in the library catalogue."
            ),
        }

    generation_start = time.perf_counter()

    answer = generate_smollm_response(
        question=cleaned_question,
        library_data=results,
        tokenizer=_tokenizer,
        model=_model,
    )

    generation_time = time.perf_counter() - generation_start

    print(f"LLM generation time: {generation_time:.2f} seconds")

    return {
        "question": cleaned_question,
        "library_data": results,
        "answer": answer,
    }