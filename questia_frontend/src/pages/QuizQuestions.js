import React, { useState } from "react";
import { api } from "../api";

const QuizQuestions = () => {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    let url = api+"bot_chat"
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
      <h2>Quiz Question Generator</h2>
      <form onSubmit={handleSubmit}>
        <textarea
          rows="4"
          cols="50"
          placeholder="Enter your message"
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

export default QuizQuestions;
