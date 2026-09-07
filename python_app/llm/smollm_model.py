"""SmolLM2-360M-Instruct local model utilities."""

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


MODEL_NAME = "HuggingFaceTB/SmolLM2-360M-Instruct"


def load_smollm_model():
    """Load the SmolLM2 tokenizer and model on CPU.

    Returns:
        Tuple containing the tokenizer and model.
    """
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
    )

    print("Model device:", next(model.parameters()).device)
    print("PyTorch threads:", torch.get_num_threads())
    return tokenizer, model