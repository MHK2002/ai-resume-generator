from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import re

app = Flask(__name__)
CORS(app)

ACTION_VERBS = [
    "Built", "Developed", "Implemented", "Designed", "Optimized",
    "Engineered", "Created", "Improved", "Automated", "Integrated",
    "Led", "Refactored", "Enhanced"
]

IMPACT_METRICS = [
    "by 20%", "by 25%", "by 30%", "by 40%", "significantly",
    "measurably", "with strong performance gains"
]

OUTCOME_PHRASES = [
    "improving user experience",
    "boosting application performance",
    "streamlining development workflows",
    "reducing manual effort",
    "enhancing system reliability",
    "increasing productivity",
    "ensuring scalability"
]

STRUCTURE_PATTERNS = [
    "{verb} {role} features using {skills}, {outcome}.",
    "{verb} scalable {role} solutions leveraging {skills}, {impact}.",
    "{verb} and {verb2} core components using {skills}, {outcome}.",
    "{verb} high-quality {role} modules with {skills}, {outcome}.",
    "{verb} end-to-end {role} systems using {skills}, {impact}."
]

def clean_skills(skills_text):
    skills = re.split(r",|\n", skills_text)
    skills = [s.strip() for s in skills if len(s.strip()) > 1]
    return skills[:5]

def extract_keywords(text):
    words = re.findall(r"\b[a-zA-Z]{4,}\b", text.lower())
    common = ["with", "using", "that", "this", "from", "into", "based"]
    keywords = [w for w in words if w not in common]
    return keywords[:5]

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json

    role = data.get("role", "Software Developer")
    skills_text = data.get("skills", "")
    experience = data.get("experience", "")

    skills_list = clean_skills(skills_text)
    keywords = extract_keywords(experience)

    skills_phrase = ", ".join(skills_list) if skills_list else "modern technologies"
    role_phrase = role.lower()

    bullets = []

    for _ in range(4):
        verb = random.choice(ACTION_VERBS)
        verb2 = random.choice([v for v in ACTION_VERBS if v != verb])
        outcome = random.choice(OUTCOME_PHRASES)
        impact = random.choice(IMPACT_METRICS)
        pattern = random.choice(STRUCTURE_PATTERNS)

        sentence = pattern.format(
            verb=verb,
            verb2=verb2,
            role=role_phrase,
            skills=skills_phrase,
            outcome=outcome,
            impact=impact
        )

        if keywords:
            sentence += f" while focusing on {', '.join(keywords[:2])}."

        bullets.append("• " + sentence)

    return jsonify({"text": "\n".join(bullets)})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5055, debug=True)
