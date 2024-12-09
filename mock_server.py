from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route('/openai/deployments/<deployment_id>/chat/completions', methods=['POST'])
def completions(deployment_id):
    data = request.json
    logging.info(f"Received request: {request.json}")
    response = {
        "id": "mock-completion-id",
        "object": "text_completion",
        "created": 1234567890,
        "model": data.get("model", "text-davinci-003"),
        "choices": [
            {
                "text": "This is a simulated response from the mock server.",
                "index": 0,
                "logprobs": None,
                "finish_reason": "length"
            }
        ],
        "usage": {
            "prompt_tokens": len(data.get("prompt", "")),
            "completion_tokens": 10,
            "total_tokens": len(data.get("prompt", "")) + 10
        }
    }
    logging.info(f"Returning response: {response}")
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)