import time

from python_app.llm.local_model import load_local_model
from python_app.llm.response_generator import generate_response


def main() -> None:
    """Measure local Qwen response-generation performance."""

    start_time = time.perf_counter()

    tokenizer, model = load_local_model()

    model_load_time = time.perf_counter() - start_time

    question = "Where is the Harry Potter book?"

    library_data = [
        {
            "book_name": "Harry Potter",
            "author_name": "J. K. Rowling",
            "branch_name": "Pune",
            "shelf": "A-12",
            "book_status": "AVAILABLE",
        }
    ]

    start_time = time.perf_counter()

    answer = generate_response(
        question,
        library_data,
        tokenizer,
        model,
    )

    generation_time = time.perf_counter() - start_time

    print(f"\nModel loading time: {model_load_time:.2f} seconds")
    print(f"Generation time: {generation_time:.2f} seconds")

    print("\nAnswer:")
    print(answer)


if __name__ == "__main__":
    main()