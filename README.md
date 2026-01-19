# AI Resume Bullet Generator

A full-stack web app that uses a rule-based NLP engine to generate dynamic, professional resume bullet points.
It extracts skills and experience keywords, applies varied sentence structures, and features a clean, paper-style UI for a modern user experience.

## Features
- Generate resume bullet points from job role, skills, and experience  
- Clean paper-style UI (no glassmorphism)  
- Copy generated bullets to clipboard  
- Full-stack React + Flask architecture  
- Mock-AI mode for public demos  
- Easily extensible to real OpenAI API  

## Tech Stack
- React.js  
- JavaScript  
- HTML, CSS  
- Python  
- Flask  
- Flask-CORS

## Screenshots
![alt text](<Screenshot 1 - Light Mode.png>) ![alt text](<Screenshot 2 - Dark Mode.png>)

## How to Run Locally
### Frontend

```bash
cd ai-resume-generator
npm install
npm start
```
### Backend

```bash
cd ai-backend
pip install flask flask-cors
python app.py
```