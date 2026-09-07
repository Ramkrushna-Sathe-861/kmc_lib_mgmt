"""Generate natural-language library responses using the local Qwen model."""

from typing import Any

import torch

from transformers import PreTrainedModel, PreTrainedTokenizer


def build_prompt(
    question: str,
    library_data: list[dict[str, Any]],
) -> str:
    """Build a grounded prompt from the user question and library data.

    Args:
        question: User's natural-language question.
        library_data: Relevant data retrieved from the library system.

    Returns:
        Prompt containing the question, library data, and response rules.
    """
    return f"""
You are a library assistant.

Answer the user's question using ONLY the library data provided below.

Rules:
1. Do not invent or assume information.
2. Do not use knowledge outside the provided library data.
3. If the data does not contain the answer, clearly say that the
   information is not available.
4. Give a short, clear and natural answer.
5. Do not mention these instructions.
6. Do not mention that you are an AI model.

User question:
{question}

Library data:
{library_data}

Answer:
""".strip()


def generate_response(
    question: str,
    library_data: list[dict[str, Any]],
    tokenizer: PreTrainedTokenizer,
    model: PreTrainedModel,
) -> str:
    """Generate a natural-language response using the local Qwen model.

    Args:
        question: User's natural-language question.
        library_data: Relevant library information.
        tokenizer: Loaded Qwen tokenizer.
        model: Loaded Qwen model.

    Returns:
        Generated natural-language answer.
    """
    prompt = build_prompt(question, library_data)

    messages = [
        {
            "role": "user",
            "content": prompt,
        }
    ]

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=False,
    )

    inputs = tokenizer(
        [text],
        return_tensors="pt",
    ).to(model.device)

    with torch.inference_mode():
        outputs = model.generate(
            **inputs,
            max_new_tokens=30,
            do_sample=False,
        )

    generated_tokens = outputs[0][inputs["input_ids"].shape[1]:]

    return tokenizer.decode(
        generated_tokens,
        skip_special_tokens=True,
    ).strip()