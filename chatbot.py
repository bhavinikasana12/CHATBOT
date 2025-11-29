
import os
import streamlit as st
from llm import generate_questions  # Your LLM function from llm.py

# ----------------------
# Streamlit App
# ----------------------
st.set_page_config(page_title="TalentScout Hiring Assistant", page_icon="🤖", layout="centered")
st.title("🤖 TalentScout Hiring Assistant")
st.write("Welcome! I am your AI hiring assistant. I will collect your information and generate technical questions based on your tech stack.")

# Initialize session state
if "conversation" not in st.session_state:
    st.session_state.conversation = []
if "candidate_info" not in st.session_state:
    st.session_state.candidate_info = {}

# ----------------------
# Candidate Information
# ----------------------
with st.form(key="candidate_info_form"):
    st.subheader("Candidate Information")
    full_name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    years_exp = st.number_input("Years of Experience", min_value=0, max_value=50, step=1)
    desired_position = st.text_input("Desired Position(s)")
    location = st.text_input("Current Location")
    tech_stack = st.text_input("Tech Stack (languages, frameworks, tools)")

    submitted = st.form_submit_button("Submit Information")

    if submitted:
        # Store candidate info
        st.session_state.candidate_info = {
            "full_name": full_name,
            "email": email,
            "phone": phone,
            "years_exp": years_exp,
            "desired_position": desired_position,
            "location": location,
            "tech_stack": tech_stack
        }
        st.success("Candidate information submitted successfully!")

# ----------------------
# Generate Technical Questions
# ----------------------
if st.session_state.candidate_info and st.session_state.candidate_info.get("tech_stack"):
    st.subheader("Technical Questions")

    if st.button("Generate Questions"):
        tech_stack_input = st.session_state.candidate_info["tech_stack"]
        try:
            questions = generate_questions(tech_stack_input)  # Call your LLM code
            st.session_state.conversation.append({"role": "assistant", "text": questions})
            st.write(questions)
        except Exception as e:
            st.error(f"Error generating questions: {e}")

# ----------------------
# Display Candidate Info (Optional)
# ----------------------
if st.session_state.candidate_info:
    st.subheader("Candidate Summary")
    for key, value in st.session_state.candidate_info.items():
        st.write(f"**{key.replace('_',' ').title()}:** {value}")

# ----------------------
# Exit / End Conversation
# ----------------------
if st.button("Exit"):
    st.write("Thank you for using TalentScout Hiring Assistant. We will get back to you with next steps!")
    st.session_state.conversation = []
    st.session_state.candidate_info = {}