from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset

import requests
from huggingface_hub import configure_http_backend

import urllib3
urllib3.disable_warnings()

def backend_factory() -> requests.Session:
    session = requests.Session()
    session.verify = False
    return session

configure_http_backend(backend_factory=backend_factory)

# Prepare dataset
data = {"text": ["What's the weather like?", "Book a flight for tomorrow."],
        "labels": [0, 1]}  # 0 = "Check Weather", 1 = "Book Flight"
dataset = Dataset.from_dict(data)

# Load pre-trained model and tokenizer
model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

# Tokenize data
def preprocess(examples):
    return tokenizer(examples["text"], truncation=True, padding=True)

tokenized_dataset = dataset.map(preprocess, batched=True)

# Train model
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=8,
)
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
)

trainer.train()

# Predict intent
inputs = tokenizer("Is it sunny today?", return_tensors="pt")
outputs = model(**inputs)
predicted_class = outputs.logits.argmax().item()
print(f"Predicted intent: {predicted_class}")
