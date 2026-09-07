"""Test SmolLM2-360M-Instruct local inference."""

import time

import torch

from python_app.llm.smollm_model import load_smollm_model


def main() -> None:
    """Load SmolLM2 and measure response-generation time."""
    start_time = time.perf_counter()

    tokenizer, model = load_smollm_model()

    model_load_time = time.perf_counter() - start_time

    question = "Where is the German book?"

    library_data = """
Book: German Language
Author: John Smith
Branch: Pune
Shelf: A-12
Status: AVAILABLE
"""

    messages = [
        {
            "role": "user",
            "content": f"""
You are a library assistant.

Answer using ONLY the library data provided.

User question:
{question}

Library data:
{library_data}

Give a short and natural answer.
Do not invent information.
""",
        }
    ]

    inputs = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        tokenize=True,
        return_dict=True,
        return_tensors="pt",
    )

    start_time = time.perf_counter()

    with torch.inference_mode():
        outputs = model.generate(
            **inputs,
            max_new_tokens=30,
            do_sample=False,
        )

    generation_time = time.perf_counter() - start_time

    generated_tokens = outputs[0][inputs["input_ids"].shape[-1]:]

    answer = tokenizer.decode(
        generated_tokens,
        skip_special_tokens=True,
    ).strip()

    print(f"\nModel loading time: {model_load_time:.2f} seconds")
    print(f"Generation time: {generation_time:.2f} seconds")
    print("\nAnswer:")
    print(answer)


if __name__ == "__main__":
    main()