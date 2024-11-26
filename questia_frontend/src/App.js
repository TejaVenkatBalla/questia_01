import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/home";
import QuizQuestions from "./pages/QuizQuestions";
import QuizEvaluation from "./pages/QuizEvaluation";
import "./App.css"; 


const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/quiz-questions" element={<QuizQuestions />} />
        <Route path="/quiz-evaluation" element={<QuizEvaluation />} />
      </Routes>
    </Router>
  );
};

export default App;
