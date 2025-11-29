# CHATBOT
PROJECT OVERVIEW

The TalentScout Hiring Assistant is an AI-powered chatbot designed to assist recruitment teams with initial     candidate screening.
It collects essential candidate information, analyzes the candidate’s tech stack, and generates relevant technical interview questions using an LLM (Large Language Model).

INSTALLATION INSTRUCTIONS

1. Install dependencies  - pip install streamlit openai==0.28 (Note:openai==0.28 is required because GPT-3.5-turbo uses the older OpenAI API)

2. Add your OpenAI API Key - export OPENAI_API_KEY="your_api_key_here"

3. Run the app - streamlit run chatbot.py

USAGE GUIDE

1. Open the UI

2. Fill out the candidate's information

3. Submit the information.

4. Click Generate questions for the techincal stack.

5. View candidates information and the generated questions

6. Exit to end the converstion

TECHNICAL DETAILS

FrontedUI - Streamlit

LLM interface - OpenAI GPT 3.5-TURBO

Backend Logic - Python

PROMPT DESIGN

"You are an HR assistant. Generate 5 interview questions based on this tech stack: {tech_stack}.
Make questions clear, internship-level, and relevant to the technologies listed."

This prompt provides the role, includes the task and context and constraints is also clear.

CHALLENGES AND SOLUTIONS

1. OpenAI version errors - GPT model 3.5 turbo still required the older API.

2. If users enter nothing the LLM will fail - Displayes the syccesufull message after complete submition.

3. LLM generating irrelevant questions - Improved prompt by adding contraints and giving a clear instructions.
