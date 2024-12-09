from transformers import AutoModel, AutoTokenizer
from huggingface_hub import snapshot_download

# Specify the model name (replace with your model)

model_name = "Swathyarun/GPT2_fine_tune"


# # Define the local directory to save the model
# local_dir = "./local_model"

# # Download model and tokenizer
# snapshot_download(repo_id=model_name, cache_dir=local_dir)

# # Load the model and tokenizer from the local directory
# tokenizer = AutoTokenizer.from_pretrained(local_dir)
# model = AutoModel.from_pretrained(local_dir)

print("Model downloaded and loaded from local directory!")

#git clone https://huggingface.co/Swathyarun/GPT2_fine_tune aceinference/app/local_model