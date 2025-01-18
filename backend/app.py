from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({'hi': 'hi'})

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')



if __name__ == '__main__':
    app.run(debug=True)