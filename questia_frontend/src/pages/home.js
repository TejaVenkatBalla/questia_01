import React, { useEffect, useState } from "react";
import { useNavigate, useLocation } from "react-router-dom";

const Home = () => {
    const navigate = useNavigate();
    const location = useLocation();
    const [queryParams, setQueryParams] = useState({});

    // Effect to log and set query parameters
    useEffect(() => {
        const params = new URLSearchParams(location.search);
        const paramsObject = {};
        params.forEach((value, name) => {
            paramsObject[name] = value;
            console.log(`${name}: ${value}`); // Log to console
        });
        setQueryParams(paramsObject); // Set state with query parameters
    }, [location]);

    return (
        <div style={{ textAlign: "center", marginTop: "20%" }}>
            <h1>Welcome to the Chatbot</h1>
            <button onClick={() => navigate("/quiz-questions")} style={buttonStyle}>
                Generate Quiz Questions
            </button>
            <button onClick={() => navigate("/quiz-evaluation")} style={buttonStyle}>
                Evaluate Quiz
            </button>

            {/* Display query parameters */}
            <div style={{ marginTop: "20px" }}>
                <h2>Query Parameters:</h2>
                <ul>
                    {Object.entries(queryParams).map(([key, value]) => (
                        <li key={key}>
                            <strong>{key}:</strong> {value}
                        </li>
                    ))}
                </ul>
            </div>
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