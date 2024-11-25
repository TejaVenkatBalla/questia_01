import React from "react";
import { useNavigate } from "react-router-dom";

const Home = () => {
    const navigate = useNavigate();

  return (
    <div style={{ textAlign: "center", marginTop: "20%" }}>
      <h1>Welcome to the Chatbot</h1>
      <button onClick={() => navigate("/quiz-questions")} style={buttonStyle}>
        Generate Quiz Questions
      </button>
      <button onClick={() => navigate("/quiz-evaluation")} style={buttonStyle}>
        Evaluate Quiz
      </button>
    </div>
  );
};

const buttonStyle = {
  margin: "20px",
  padding: "10px 20px",
  fontSize: "18px",
  cursor: "pointer",
};

export default Home;
