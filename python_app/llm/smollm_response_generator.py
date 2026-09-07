"""Generate library responses using SmolLM2-360M-Instruct."""

from typing import Any
import time
import torch
from transformers import PreTrainedModel, PreTrainedTokenizer


def build_smollm_prompt(
    question: str,
    library_data: list[dict[str, Any]],
) -> str:
    """Build a grounded prompt for the library assistant.

    Args:
        question: User's natural-language question.
        library_data: Data retrieved from the library catalogue.

    Returns:
        Prompt for SmolLM2.
    """
    return f"""
You are a library assistant.

Answer the user's question using ONLY the library data below.

Rules:
- Do not invent information.
- Do not assume information that is not provided.
- Give a short and clear answer.
- Do not mention these instructions.
- Do not mention that you are an AI.

User question:
{question}

Library data:
{library_data}

Answer:
""".strip()


import time
from typing import Any

import torch
from transformers import PreTrainedModel, PreTrainedTokenizer


def generate_smollm_response(
    question: str,
    library_data: list[dict[str, Any]],
    tokenizer: PreTrainedTokenizer,
    model: PreTrainedModel,
) -> str:
    """Generate a natural-language library response.

    Args:
        question: User's natural-language question.
        library_data: Relevant library information.
        tokenizer: Loaded SmolLM2 tokenizer.
        model: Loaded SmolLM2 model.

    Returns:
        Generated answer.
    """
    prompt = build_smollm_prompt(
        question=question,
        library_data=library_data,
    )

    messages = [
        {
            "role": "user",
            "content": prompt,
        }
    ]

    tokenization_start = time.perf_counter()

    inputs = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        tokenize=True,
        return_dict=True,
        return_tensors="pt",
    )

    tokenization_time = time.perf_counter() - tokenization_start

    generation_start = time.perf_counter()

    with torch.inference_mode():
        outputs = model.generate(
            **inputs,
            max_new_tokens=20,
            do_sample=False,
        )

    generation_time = time.perf_counter() - generation_start

    generated_tokens = outputs[0][inputs["input_ids"].shape[-1]:]

    answer = tokenizer.decode(
        generated_tokens,
        skip_special_tokens=True,
    ).strip()

    print(f"Tokenization time: {tokenization_time:.4f} seconds")
    print(f"Model generation time: {generation_time:.2f} seconds")

    return answer