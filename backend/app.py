from flask import Flask, request, jsonify
import os
import google.generativeai as genai
from flask_cors import CORS

app = Flask(__name__)
# Allow CORS for all domains and routes
CORS(app)

# Configure API key for Google Generative AI
api_key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=api_key)

# Initialize the model with the generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction=(
        "Assist the teacher in conducting quizzes for students. When the teacher requests questions on a specific topic, "
        "generate questions based on their requirements. Ask the teacher if they do not provide:\n\n"
        "How many questions they need.\n"
        "The number of multiple-choice questions (MCQs) and subjective questions.\n"
        "The students' grade level.\n"
        "The desired difficulty level."
    ),
)

@app.route("/")
def rander():
    return jsonify("working...")

# Start a chat session
chat_session = model.start_chat()

@app.route('/bot_chat', methods=['POST'])
def chat_01():
    try:
        # Get the input message from the request JSON
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({"error": "Invalid request, 'message' is required"}), 400

        
        # Send the user's message
        user_message = data['message']
        response = chat_session.send_message(user_message)

        # Return the AI's response
        return jsonify({"response": response.text}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
#feedback_model
feedback_model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  system_instruction="You are a teacher's assistant. Your task is to evaluate student quizzes and provide a score.\n\nHere's how to assess the quiz:\n\n1. Carefully review the quiz question, student answer.\n2. Compare the student's answer to the correct answer.\n3. If the student's answer is completely correct, give a score of 100%.\n4. If the student's answer is completely incorrect, give a score of 0%.\n5. If the student's answer is partially correct, determine the percentage of the answer that is correct and provide a score accordingly. For example, if the answer is half correct, give a score of 50%.\n6. If the quiz question requires a specific format (e.g., multiple-choice, short answer, essay), evaluate the student's answer based on the format requirements.  If the format is incorrect, deduct points as appropriate.\n7. If the student's answer is ambiguous or unclear, provide feedback explaining why and suggest how the student could improve their answer.\n8. Provide the score and any relevant feedback.\n\n",
)

# Start a chat session
chat_session_02 = feedback_model.start_chat()

@app.route('/feedback_bot', methods=['POST'])
def chat_02():
    try:
        # Get the input message from the request JSON
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({"error": "Invalid request, 'message' is required"}), 400

        
        # Send the user's message
        user_message = data['message']
        response = chat_session_02.send_message(user_message)

        # Return the AI's response
        return jsonify({"response": response.text}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
