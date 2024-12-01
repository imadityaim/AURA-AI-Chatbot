from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the Google Generative AI API
genai.configure(api_key="Your_API")

# Function to load Gemini Pro and get response
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])


def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response


# Initialize Streamlit app
st.set_page_config(page_title="AI-Chatbot")

st.header("AI-ChatBot!")
st.markdown("Welcome to the World of Gen-AI")

# Initialize chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state["chat_history"] = []

# Input field for user question
input_text = st.text_input("Feel Free to Ask your Query...", key="input")
submit = st.button("Get Result")

# Process the user's question and get the response
if submit and input_text:
    response = get_gemini_response(input_text)
    st.session_state['chat_history'].append(("You", input_text))

    st.subheader("Your response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

# Display the chat history inside an expander
with st.expander("History"):
    for role, text in st.session_state["chat_history"]:
        st.write(f"{role}: {text}")

# Footer for the app
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
        padding: 10px 0;
        font-size: 12px;
        color: black;
    }
    </style>
    <div class="footer">
        All Rights Reserved © 2024 | Designed by <a href="https://github.com/imadityaim">Aditya Navakhande</a>
    </div>
    """,
    unsafe_allow_html=True
)
