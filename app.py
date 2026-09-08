import streamlit as st
from google import genai
from google.genai import types
import os

# 1. Page Configuration & Custom Styling Forcing Clear Black Text Input
st.set_page_config(page_title="Omni AI Hub", page_icon="⚡", layout="wide")

# CSS to make the app background a bright, clean white-gray and force all input text to be black
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f2f6 !important;
        color: #000000 !important;
    }
    input, textarea, select {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 2px solid #3b82f6 !important;
        font-weight: bold !important;
    }
    p, h1, h2, h3, span, label {
        color: #111827 !important;
    }
    .stTab button p {
        color: #111827 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Secure Cloud Core AI Client Setup
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# 3. Custom Stylized AI Logo and Header Layout
st.markdown("<h2 style='text-align: center;'>🛡️🤖⚡ CYBER-SHIELD OMNI-AI</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-weight: bold;'>The All-in-One Global AI Dashboard — Light Mode Edition</p>", unsafe_allow_html=True)

# 4. Five Navigation Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "💬 Universal Chat", 
    "💻 Code Scripter", 
    "📄 Book Summarizer", 
    "🌐 Polyglot Translator", 
    "🧠 Brain Quiz Maker"
])

# MODE 1: Universal Chat
with tab1:
    st.subheader("🤖 Universal Omni-Chat Assistant")
    user_prompt = st.text_area("What is on your mind?", placeholder="Type your query here...", key="omni_chat")
    if st.button("Ask Omni Engine"):
        if user_prompt:
            with st.spinner("AI thinking..."):
                response = client.models.generate_content(model='gemini-3.6-flash', contents=user_prompt)
                st.write(response.text)

# MODE 2: Code Scripter
with tab2:
    st.subheader("💻 AI Code Builder & Download Hub")
    code_request = st.text_input("What script do you want to build? (e.g., Python calculator):")
    file_ext = st.selectbox("Select File Extension Format:", [".py", ".html", ".js", ".css", ".cs", ".txt"])
    if st.button("Compile Code Script"):
        if code_request:
            with st.spinner("Writing raw programming scripts..."):
                sys_rule = "You are an expert coder. Return ONLY clean working script files. No talk, no explanations."
                response = client.models.generate_content(
                    model='gemini-3.6-flash', contents=code_request,
                    config=types.GenerateContentConfig(system_instruction=sys_rule, temperature=0.2)
                )
                generated_script = response.text
                st.code(generated_script, language="python")
                st.download_button(
                    label=f"📥 Download Compiled {file_ext} File",
                    data=generated_script, file_name=f"AI_Generated_Script{file_ext}", mime="text/plain"
                )

# MODE 3: Book Summarizer
with tab3:
    st.subheader("📄 Dynamic Document & Text Book Summarizer")
    long_text = st.text_area("Paste walls of text or book chapters here:", height=150, key="summary_input")
    if st.button("Extract Deep Summary"):
        if long_text:
            with st.spinner("Scanning documents..."):
                sum_prompt = f"Provide a clean, bulleted executive summary highlighting key definitions from this text:\n{long_text}"
                response = client.models.generate_content(model='gemini-3.6-flash', contents=sum_prompt)
                st.write(response.text)

# MODE 4: Language Translator
with tab4:
    st.subheader("🌐 High-Fidelity Language Translator")
    text_to_translate = st.text_input("Enter text content to translate:")
    target_lang = st.selectbox("Select Target Language:", ["Urdu", "English", "Arabic", "Spanish", "French"])
    if st.button("Translate Text"):
        if text_to_translate:
            with st.spinner("Processing translations..."):
                trans_prompt = f"Translate the following text into {target_lang}:\n{text_to_translate}"
                response = client.models.generate_content(model='gemini-3.6-flash', contents=trans_prompt)
                st.write(response.text)

# MODE 5: Interactive Brain Quiz
with tab5:
    st.subheader("🧠 Automatic Dynamic Pop-Quiz Prep")
    quiz_subject = st.text_input("Enter topic for testing (e.g., Photosynthesis):")
    if st.button("Generate Exam Blueprint"):
        if quiz_subject:
            with st.spinner("Compiling academic evaluations..."):
                quiz_prompt = f"Create a rigorous 3-question multiple choice evaluation quiz regarding {quiz_subject}. Provide a clearly marked answer key at the very bottom."
                response = client.models.generate_content(model='gemini-3.6-flash', contents=quiz_prompt)
                st.write(response.text)
