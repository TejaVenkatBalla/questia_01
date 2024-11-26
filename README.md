# AI-Powered Quiz Chatbot  

An AI-driven chatbot designed to help teachers streamline their workflow by automating quiz creation and evaluation. This project uses **Gemini**, Google's advanced AI platform, for generating quiz questions and evaluating student responses. The application is built with Flask for the backend and deployed using **Google Cloud Platform (GCP)** via **Cloud Run**.

---

## **Features**  

1. **Quiz Preparation Bot**  
   - Generates quiz questions based on a specified topic, number of questions, and difficulty level.  

2. **Quiz Evaluation Bot**  
   - Evaluates student responses to quizzes and provides detailed feedback to teachers.  

3. **Scalable Deployment**  
   - Deployed using Cloud Run for a serverless, scalable, and cost-effective solution.  

---

## **Tech Stack**  

- **Backend**: Flask, Google Generative AI (Gemini)  
- **Deployment**: Google Cloud Platform (Cloud Run)  
- **Frontend**: React  

---

## **Medium Blog**
(https://medium.com/@tejavenkatballa/how-to-build-a-chatbot-using-gemini-f0bf22f6a3c6)

## **Medium Blog Content**

Tittle : How to Build a Chatbot Using Gemini


Chatbots have revolutionized the way we interact with technology, offering seamless communication and automated assistance across industries. With advancements in AI, building intelligent and highly functional chatbots has become more accessible than ever. Enter Gemini, Google’s next-generation AI platform, which simplifies the process of developing conversational agents with its robust generative capabilities.

In this guide, we’ll walk through creating a chatbot that helps teachers prepare quizzes and assess student performance. Using Gemini’s powerful capabilities, this bot streamlines quiz generation and evaluation, saving time and improving efficiency. Let’s get started!

### Step 1: Setting Up Gemini
1. **Access the Gemini Platform:** Log in to your Google Cloud Console and enable Gemini APIs in your project.
2. **Install Required SDKs:** Install the necessary Google Cloud libraries using `pip install google-cloud`. These libraries allow seamless interaction with Gemini APIs.
3. **Authenticate:** Download your Google Cloud credentials and authenticate your project using:
   ```
   gcloud auth application-default login
   ```

### Step 2: Designing the Chatbot
1. **Define Use Cases:**
   - **Quiz Preparation Bot:** Generates quiz questions based on a topic, number of questions, and difficulty level.
   - **Quiz Evaluation Bot:** Evaluates student answers and provides insights to teachers.
2. **Set Up API Endpoints:** For this use case, create two endpoints:
   - `/generate_quiz`: Handles quiz generation requests.
   - `/evaluate_quiz`: Processes and evaluates student responses.

### Step 3: Building the Backend
1. **Integrate Gemini for Question Generation:**  
   Use Gemini’s generative capabilities to dynamically create quiz questions. Example Python code:
   ```python
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
   ```

2. **Add Evaluation Logic:**  
   Use Gemini to analyze student responses and generate feedback. Example:
   ```python
   feedback_model = genai.GenerativeModel(
       model_name="gemini-1.5-pro",
       generation_config=generation_config,
       system_instruction="You are a teacher's assistant. Your task is to evaluate student quizzes and provide a score.\n\nHere's how to assess the quiz:\n\n1. Carefully review the quiz question, student answer.\n2. Compare the student's answer to the correct answer.\n3. If the student's answer is completely correct, give a score of 100%.\n4. If the student's answer is completely incorrect, give a score of 0%.\n5. If the student's answer is partially correct, determine the percentage of the answer that is correct and provide a score accordingly. For example, if the answer is half correct, give a score of 50%.\n6. If the quiz question requires a specific format (e.g., multiple-choice, short answer, essay), evaluate the student's answer based on the format requirements.  If the format is incorrect, deduct points as appropriate.\n7. If the student's answer is ambiguous or unclear, provide feedback explaining why and suggest how the student could improve their answer.\n8. Provide the score and any relevant feedback.\n\n",
   )
   ```

3. **Build RESTful APIs:**  
   Use Flask or FastAPI to expose these functions:
   ```python
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
   ```

### Step 4: Deployment with Cloud Run
1. **Containerize the Application:**  
   Create a Dockerfile for your Flask app:
   ```Dockerfile
   # Use the official Python image as the base image
   FROM python:3.9-slim

   # Set the working directory inside the container
   WORKDIR /app

   # Copy only the requirements file first for better caching
   COPY requirements.txt requirements.txt

   # Install dependencies
   RUN pip install --no-cache-dir -r requirements.txt

   # Copy the rest of the application code
   COPY . .

   # Expose port 8080 for Cloud Run
   EXPOSE 8080

   # Command to run the application
   CMD ["python", "app.py"]
   ```

2. **Deploy to Cloud Run:**
   - Build the Docker image:
     ```
     gcloud builds submit --tag gcr.io/<your-project-id>/chatbot
     ```
   - Deploy to Cloud Run:
     ```
     gcloud run deploy chatbot --image gcr.io/<your-project-id>/chatbot --platform managed
     ```

### Step 5: Testing and Iteration
1. **Test API Endpoints:**  
   Use tools like Postman to verify the functionality of `/generate_quiz` and `/evaluate_quiz`.
2. **Iterate and Improve:**  
   Based on user feedback, refine your chatbot’s prompts and evaluation methods for better results.

### Ease of Development with Gemini and GCP
Building and deploying these chatbots became significantly easier with the help of Gemini and Google Cloud Platform (GCP). Gemini’s advanced generative capabilities enabled me to quickly create the quiz generation and evaluation bots, streamlining the AI development process.

On the deployment side, Cloud Run from GCP provided a seamless, serverless environment to deploy the chatbots, ensuring scalability without worrying about managing infrastructure. The combination of Gemini for AI capabilities and GCP for deployment made the entire process fast, efficient, and scalable, allowing for a smooth end-to-end solution.

### Conclusion
Building a chatbot with Gemini is straightforward and powerful. In this guide, we developed a bot that helps teachers create quizzes and evaluate student performance, streamlining their workflow. Gemini’s generative AI and Google Cloud Platform’s Cloud Run simplify development and deployment, making it easy to scale your chatbot for real-world use.

Start building your chatbot today and unlock the potential of AI in education!

### Additional Information
To learn more about Google Cloud services and to create impact for the work you do, get around to these steps right away:
- Register for Code Vipassana sessions
- Join the meetup group Datapreneur Social
- Sign up to become Google Cloud Innovator

---


