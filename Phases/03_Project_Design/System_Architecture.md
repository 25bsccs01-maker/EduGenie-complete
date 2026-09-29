# System Architecture

Student
   |
   v
Frontend – HTML/CSS/JavaScript
   |
   v
FastAPI Backend
   |
   +----------------------+
   |                      |
   v                      v
EduGenie Modules      Gemini Client
   |                      |
   +----------+-----------+
              |
              v
       Google Gemini API
              |
              v
       AI Generated Result
              |
              v
           Student