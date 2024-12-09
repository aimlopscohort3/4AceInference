from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Import the shared model and tokenizer from __init__.py
from app import model, tokenizer


def generate_response(input_text: str, max_length: int = 100) -> str:
    """
    Generates a response for the given input using the fine-tuned model.

    Args:
        input_text (str): The input text for the model.
        max_length (int): Maximum length of the generated response.

    Returns:
        str: The generated response text.
    """
    try:
        # Tokenize the input text
        inputs = tokenizer(input_text, return_tensors="pt", truncation=True, max_length=512)

        # Generate output from the model
        outputs = model.generate(
            inputs["input_ids"],
            max_length=max_length,
            pad_token_id=tokenizer.pad_token_id,
            num_beams=5,  # Optional: Adjust for diversity
            early_stopping=True  # Stop once a complete response is generated
        )

        # Decode the output into text
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return generated_text
    except Exception as e:
        return f"Error during inference: {str(e)}"