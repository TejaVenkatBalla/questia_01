from flask import Flask, request, jsonify
import base64
import vertexai
from vertexai.generative_models import GenerativeModel, SafetySetting

app = Flask(__name__)

# Initialize the Vertex AI project and location
PROJECT_ID = "macro-magpie-442713-k7"
LOCATION = "us-central1"

# System instructions
TEXTSI_1 = """Assist the teacher in conducting quizzes for students. When the teacher requests questions on a specific topic, generate questions based on their requirements. Ask the teacher if he does not provide:

How many questions they need.
The number of multiple-choice questions (MCQs) and subjective questions.
The students' grade level.
The desired difficulty level."""

# Safety settings
SAFETY_SETTINGS = [
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
]

generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

# Initialize Vertex AI
vertexai.init(project=PROJECT_ID, location=LOCATION)

# Define the generative model
model = GenerativeModel(
    "gemini-1.5-flash-002",
    system_instruction=[TEXTSI_1],
    generation_config=generation_config,
    safety_settings=SAFETY_SETTINGS
)

@app.route("/")
def rander():
    return jsonify("testing ")

@app.route("/quiz_bot", methods=["POST"])
def generate_content():
    try:
        # Extract request data
        data = request.json
        user_query = data.get("query")

        # Validate input
        if not user_query:
            return jsonify({"error": "Query is required"}), 400

        # Start chat session with the model
        chat = model.start_chat()

        # Generate response
        response = chat.send_message(
            user_query  # Use the user's query directly
        )

        # Return the response
        return jsonify({"generated_content": response.text}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
