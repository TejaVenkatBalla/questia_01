import React, { useState } from "react";
import { api } from "../api";

const QuizEvaluation = () => {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    let url = api+"feedback_bot"
    try {
      const res = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message }),
      });

      if (!res.ok) {
        throw new Error(`Error: ${res.status}`);
      }

      const data = await res.json();
      setResponse(data.response);
    } catch (error) {
      console.error(error);
      setResponse("Error: Could not fetch response.");
    }
  };

  return (
    <div style={{ textAlign: "center", marginTop: "20%" }}>
      <h2>Quiz Evaluation</h2>
      <form onSubmit={handleSubmit}>
        <textarea
          rows="4"
          cols="50"
          placeholder="Enter student answer and question"
          style={{
            width: "80%",
            minHeight: "100px",
            resize: "vertical", // Allow resizing only vertically
            padding: "10px",
            fontSize: "16px",
            lineHeight: "1.5",
            borderRadius: "5px",
            border: "1px solid #ccc",
            boxShadow: "inset 0 1px 3px rgba(0, 0, 0, 0.1)",
          }}
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          required
        />
        <br />
        <button type="submit">Submit</button>
      </form>
      {response && <p><strong>Response:</strong> {response}</p>}
    </div>
  );
};

export default QuizEvaluation;
