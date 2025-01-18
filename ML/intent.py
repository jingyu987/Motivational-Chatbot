# from transformers import RobertaTokenizerFast, RobertaForSequenceClassification, TextClassificationPipeline


# import requests
# from huggingface_hub import configure_http_backend

# import urllib3
# urllib3.disable_warnings()

# def backend_factory() -> requests.Session:
#     session = requests.Session()
#     session.verify = False
#     return session

# configure_http_backend(backend_factory=backend_factory)

# # Load fine-tuned model by HuggingFace Model Hub
# HUGGINGFACE_MODEL_PATH = "bespin-global/klue-roberta-small-3i4k-intent-classification"
# loaded_tokenizer = RobertaTokenizerFast.from_pretrained(HUGGINGFACE_MODEL_PATH )
# loaded_model = RobertaForSequenceClassification.from_pretrained(HUGGINGFACE_MODEL_PATH )

# # using Pipeline
# text_classifier = TextClassificationPipeline(
#     tokenizer=loaded_tokenizer, 
#     model=loaded_model, 
#     return_all_scores=True
# )

# # predict
# text = ""

# preds_list = text_classifier(text)
# best_pred = preds_list[0]
# print(f"Label of Best Intentatioin: {best_pred[0]['label']}")
# print(f"Score of Best Intentatioin: {best_pred[0]['score']}")


from textblob import Textblob

blob = Textblob("I love Adoran San")
print(blob.noun_phrases)