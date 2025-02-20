import streamlit as st
import google.generativeai as genai

# 🚨 API Key (Replace with your actual key)
API_KEY = "AIzaSyAzG4AstYwG-2vUCUGS1mHMCroodPtKrOA"

# Configure the Google Generative AI API
genai.configure(api_key=API_KEY)

# Load Gemini Pro model
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    """Get AI response from Gemini Pro"""
    response = chat.send_message(question)
    return response.text  # Extracting response text properly

# Streamlit App Configuration
st.set_page_config(page_title="Aura - AI Chatbot", page_icon="🤖", layout="wide")

# Custom CSS for Styling
st.markdown(
    """
    <style>
    .title { text-align: center; color: #2e3b4e; font-size: 2.5rem; font-weight: bold; }
    .subtitle { text-align: center; color: #4a5568; font-size: 1.2rem; }
    .footer-box { position: fixed; bottom: 0; left: 0; width: 100%; background-color: white;
                  text-align: center; padding: 10px 0; font-size: 14px; color: black; font-weight: bold;
                  border-top: 2px solid #ccc; }
    .ask-button-container { display: flex; justify-content: center; margin-top: 10px; }
    .ask-button-container button { width: 120px; font-size: 14px; padding: 5px 10px;
                                   background-color: #3182ce; color: white; border-radius: 5px;
                                   border: none; cursor: pointer; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and Subtitle
st.markdown('<h1 class="title">AURA 🤖</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your AI Chatbot Assistant.</p>', unsafe_allow_html=True)

# Chat History Initialization
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Sidebar for Chat History
st.sidebar.header("History")

# Button to Clear Chat History
if st.sidebar.button("Clear History"):
    st.session_state["chat_history"] = []

st.sidebar.markdown("---")  # Separator line

# Display Chat History in Sidebar
for role, text in (st.session_state["chat_history"]):  # Show latest first
    if role == "AURA":
        st.sidebar.markdown(f"**🤖 Aura:** {text}")
    else:
        st.sidebar.markdown(f"**🧑‍💻 You:** {text}")

# User Input Field
input_text = st.text_input("Ask me anything...", key="input")

# Ask Button
st.markdown('<div class="ask-button-container">', unsafe_allow_html=True)
if st.button("Ask"):
    if input_text:
        response = get_gemini_response(input_text)  # Get AI response
        st.session_state["chat_history"].append(("You", input_text))  # Store user query
        st.session_state["chat_history"].append(("AURA", response))  # Store AI response

        # Show only the latest AI response on the main page
        st.markdown(f"<strong>AURA:</strong> {response}", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Fixed Footer
st.markdown(
    """
    <div class="footer-box">
        All Rights Reserved © 2025 | Designed by Usha Subhash
    </div>
    """,
    unsafe_allow_html=True,
)
