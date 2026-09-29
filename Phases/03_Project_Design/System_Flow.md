# System Flow

1. Student opens EduGenie.
2. Student selects a learning feature.
3. Student enters a question or topic.
4. Frontend sends the request to FastAPI.
5. FastAPI processes the request.
6. Appropriate EduGenie module is selected.
7. Gemini prompt is created.
8. Request is sent to Google Gemini.
9. Gemini generates the response.
10. Response is returned to FastAPI.
11. Frontend displays the result.
