import streamlit as st
from google import genai
from google.genai import types
import os

# 1. Dashboard Layout & Visual Appearance
st.set_page_config(page_title="Omni AI Hub", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0b0f19; color: #e4e6eb; }
    div[data-testid="stSidebar"] { background-color: #111827; }
    .stButton button { background-color: #3b82f6 !important; color: white !important; border-radius: 8px !important; }
    </style>
""", unsafe_allow_html=True)

# 2. Secure Cloud Core AI Client Setup
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# 3. App Header & Statistics
st.markdown("<h1 style='color: #60a5fa; text-align: center;'>⚡ OmniAI Ultimate Hub</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9ca3af;'>The All-in-One Global AI Dashboard with Zero Restrictions</p>", unsafe_allow_html=True)

# 4. Five Core Feature Modes Navigation Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "💬 Universal Chat", 
    "💻 Code Scripter", 
    "📄 Book Summarizer", 
    "🌐 Polyglot Translator", 
    "🧠 Brain Quiz Maker"
])

# MODE 1: Universal Anything Assistant
with tab1:
    st.subheader("🤖 Universal Omni-Chat Assistant")
    st.caption("Ask me absolutely anything: from video games to recipes, advice, storytelling, or complex life questions.")
    user_prompt = st.text_area("What is on your mind?", placeholder="Type anything here...", key="omni_chat")
    if st.button("Ask Omni Engine"):
        if user_prompt:
            with st.spinner("AI thinking..."):
                response = client.models.generate_content(model='gemini-3.6-flash', contents=user_prompt)
                st.write(response.text)

# MODE 2: Code Scripter & File Compiler
with tab2:
    st.subheader("💻 AI Code Builder & Download Hub")
    st.caption("Enter what program you want. The AI writes the raw code and compiles a downloadable file instantly.")
    code_request = st.text_input("What script do you want to build? (e.g., Build a Python snake game):")
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

# MODE 3: Book Summarizer & Data Cruncher
with tab3:
    st.subheader("📄 Dynamic Document & Text Book Summarizer")
    st.caption("Paste long articles, chapters, or textbook data below to get instant main-bullet executive breakdowns.")
    long_text = st.text_area("Paste walls of text or book chapters here:", height=150)
    if st.button("Extract Deep Summary"):
        if long_text:
            with st.spinner("Scanning and reading documents..."):
                sum_prompt = f"Provide a clean, bulleted executive summary highlighting key definitions and actionable takeaways from this text:\n{long_text}"
                response = client.models.generate_content(model='gemini-3.6-flash', contents=sum_prompt)
                st.write(response.text)

# MODE 4: Universal Language Polyglot Translator
with tab4:
    st.subheader("🌐 High-Fidelity Language Translator")
    st.caption("Translate expressions or full homework paragraphs perfectly across global and regional languages.")
    text_to_translate = st.text_input("Enter text content to translate:")
    target_lang = st.selectbox("Select Target Language:", ["Urdu (اردو)", "English", "Arabic (العربية)", "Spanish", "Chinese", "French"])
    if st.button("Translate Text"):
        if text_to_translate:
            with st.spinner("Processing translations..."):
                trans_prompt = f"Translate the following text into {target_lang} natively and write out pronunciation hints if helpful:\n{text_to_translate}"
                response = client.models.generate_content(model='gemini-3.6-flash', contents=trans_prompt)
                st.write(response.text)

# MODE 5: Interactive Brain Quiz & Test Prep Engine
with tab5:
    st.subheader("🧠 Automatic Dynamic Pop-Quiz Prep")
    st.caption("Instantly generate customized competitive exam or classroom tests for any topic to gauge mastery.")
    quiz_subject = st.text_input("Enter exam topic for testing (e.g., World War 2, Organic Chemistry):")
    if st.button("Generate Exam Blueprint"):
        if quiz_subject:
            with st.spinner("Compiling academic evaluations..."):
                quiz_prompt = f"Create a rigorous 3-question multiple choice evaluation quiz regarding {quiz_subject}. Provide a clearly marked answer key at the very bottom."
                response = client.models.generate_content(model='gemini-3.6-flash', contents=quiz_prompt)
                st.write(response.text)
