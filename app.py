import streamlit as st
from google import genai
from google.genai import types
import os

# 1. Sleek Modern Layout (Gemini style)
st.set_page_config(page_title="Gemini Clone", page_icon="✨", layout="wide")

# Inject custom Gemini dark/light style adjustments using Markdown CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #131314;
        color: #e3e3e3;
    }
    div[data-testid="stSidebar"] {
        background-color: #1e1f20;
    }
    .stTextInput input {
        background-color: #282a2d !important;
        color: white !important;
        border-radius: 20px !important;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Secure Client Setup
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# 3. Sidebar (Just like the real Gemini sidebar layout)
st.sidebar.title("✨ Gemini Pro")
st.sidebar.button("➕ New chat", use_container_width=True)
st.sidebar.markdown("---")
st.sidebar.caption("🕒 Recent Activity")
st.sidebar.text_area("Chat History", "• How to build an app...\n• Python help...", height=100, disabled=True)

# 4. Main Chat Interface Headings
st.markdown("<h1 style='color: #4285F4;'>Hello, Developer</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #80868b;'>How can I help you today?</h3>", unsafe_allow_html=True)
st.caption("Ask me anything! From coding algorithms to video game builds, creative screenplays, or casual conversations.")

# 5. Maintaining Live Chat Memory State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Print existing historical messages cleanly as chat bubbles
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 6. Bottom Input Box (Matches the Gemini text bar input layout)
user_input = st.chat_input("Ask Gemini...")

if user_input:
    # Append the user's fresh message to the screen memory state
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Reach out to Google Cloud AI engine without ANY strict filters or blockers
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.models.generate_content(
                    model='gemini-3.6-flash',
                    contents=user_input,
                    config=types.GenerateContentConfig(
                        temperature=0.7 # High creativity value allows standard natural speech
                    )
                )
                model_reply = response.text
                st.write(model_reply)
                # Save assistant response to state memory loop
                st.session_state.messages.append({"role": "assistant", "content": model_reply})
            except Exception as e:
                st.error(f"Error communicating with AI engine: {e}")
