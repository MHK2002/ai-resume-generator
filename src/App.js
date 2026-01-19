import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [role, setRole] = useState("");
  const [skills, setSkills] = useState("");
  const [experience, setExperience] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);
  const [dark, setDark] = useState(false);

  useEffect(() => {
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme === "dark") setDark(true);
  }, []);

  useEffect(() => {
    localStorage.setItem("theme", dark ? "dark" : "light");
  }, [dark]);

  async function generateBullets() {
    if (!role || !skills || !experience) {
      alert("Please fill all fields");
      return;
    }

    setLoading(true);

    try {
      const response = await fetch("http://127.0.0.1:5055/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ role, skills, experience }),
      });

      const data = await response.json();
      setResult(data.text);
    } catch (error) {
      console.error("FRONTEND ERROR:", error);
      setResult("Error generating bullets.");
    }

    setLoading(false);
  }

  return (
    <div className={`page ${dark ? "dark" : ""}`}>
      <div className="card">
        <div className="top-bar">
          <h1>AI Resume Bullet Generator</h1>
          <button className="theme-btn" onClick={() => setDark(!dark)}>
            {dark ? "☀️" : "🌙"}
          </button>
        </div>

        <p className="subtitle">
          Generate professional resume bullet points using AI
        </p>

        <label>Target Job Role</label>
        <input
          placeholder="e.g. Frontend Developer"
          value={role}
          onChange={e => setRole(e.target.value)}
        />

        <label>Your Skills</label>
        <textarea
          placeholder="e.g. React, JavaScript, CSS, Git"
          value={skills}
          onChange={e => setSkills(e.target.value)}
        />

        <label>Your Experience Summary</label>
        <textarea
          placeholder="Briefly describe your experience or projects"
          value={experience}
          onChange={e => setExperience(e.target.value)}
        />

        <button onClick={generateBullets} disabled={loading}>
          {loading ? "Generating..." : "Generate Bullet Points"}
        </button>

        {result && (
          <div className="result">
            <h3>Generated Bullet Points</h3>
            <pre>{result}</pre>
            <button
              className="copy-btn"
              onClick={() => navigator.clipboard.writeText(result)}
            >
              Copy to Clipboard
            </button>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
