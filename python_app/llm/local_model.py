"""Local Qwen model loading utilities."""

from transformers import AutoModelForCausalLM, AutoTokenizer


MODEL_NAME = "Qwen/Qwen3-0.6B"


def load_local_model():
    """Load the Qwen model and tokenizer on CPU."""
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
    )

    return tokenizer, model