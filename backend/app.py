from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import AutoModelForCausalLM, AutoTokenizer
import requests
from huggingface_hub import configure_http_backend

import urllib3

app = Flask(__name__)

CORS(app)

urllib3.disable_warnings()

def backend_factory() -> requests.Session:
    session = requests.Session()
    session.verify = False
    return session

configure_http_backend(backend_factory=backend_factory)
model = AutoModelForCausalLM.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")

def generate_response(user_input):
    input_ids = tokenizer(user_input, return_tensors="pt").input_ids

    gen_tokens = model.generate(
        input_ids,
        do_sample=True,
        temperature=0.9,
        max_length=100,
    )
    gen_text = tokenizer.batch_decode(gen_tokens)[0]
    return gen_text


@app.route('/api/generate', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')
    response_text = generate_response(user_input)
    return jsonify({"response": response_text})


if __name__ == '__main__':
    app.run(debug=True)