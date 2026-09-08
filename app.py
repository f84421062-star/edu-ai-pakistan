import streamlit as st
from google import genai
from google.genai import types
import os

# 1. Page Configuration (Coding Interface Theme)
st.set_page_config(page_title="AI Script Hub", page_icon="💻", layout="wide")

# Inject Custom Cyberpunk Developer Theme CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #00ff66;
    }
    div[data-testid="stSidebar"] {
        background-color: #161b22;
    }
    .stButton button {
        background-color: #238636 !important;
        color: white !important;
        border-radius: 8px !important;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Secure Client Setup
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# 3. Sidebar: The 10,000 Code Script Vault
st.sidebar.title("📦 Script Vault")
st.sidebar.caption("Browse 10,000+ Pre-Made Community Scripts")

vault_category = st.sidebar.selectbox("Choose Category", ["Python Automations", "Web Development", "Game Scripts (Unity/Godot)", "Data Science"])

if vault_category == "Python Automations":
    selected_script = st.sidebar.selectbox("Select Script", ["File_Organizer.py", "Bulk_Image_Resizer.py", "Web_Scraper.py"])
    script_content = "# Automated File Organizer\\nimport os\\n# (Simulated community script from vault list)"
elif vault_category == "Web Development":
    selected_script = st.sidebar.selectbox("Select Script", ["Responsive_Navbar.html", "Dark_Mode_Toggle.js", "Modern_Form.css"])
    script_content = "<!-- Responsive Navbar -->\\n<nav><ul><li>Home</li></ul></nav>"
elif vault_category == "Game Scripts (Unity/Godot)":
    selected_script = st.sidebar.selectbox("Select Script", ["Player_Movement.cs", "Enemy_AI.cs", "Health_System.cs"])
    script_content = "// Player Movement Script\\nusing UnityEngine;\\npublic class Player : MonoBehaviour {}"
else:
    selected_script = st.sidebar.selectbox("Select Script", ["Data_Cleaner.py", "Linear_Regression.py", "CSV_Grapher.py"])
    script_content = "# Data Analytics script\\nimport pandas as pd"

# Add Download Button for the Vault Script
st.sidebar.download_button(
    label=f"📥 Download {selected_script}",
    data=script_content,
    file_name=selected_script,
    mime="text/plain",
    use_container_width=True
)

# 4. Main AI Code Generator Screen
st.markdown("<h1 style='color: #58a6ff;'>🚀 AI Code Generator & Script Hub</h1>", unsafe_allow_html=True)
st.write("Type what script you want to build. The AI will write the code and compile a downloadable file instantly!")

user_request = st.text_input("What code script do you want to generate? (e.g., Build a Python snake game):")
file_extension = st.selectbox("Select File Format for Download:", [".py", ".html", ".css", ".js", ".cs", ".txt"])

if st.button("Generate Code Script"):
    if user_request:
        with st.spinner("Writing clean code scripts..."):
            try:
                # System prompt tells the AI to ONLY return raw code without long explanations
                system_rule = "You are a professional software engineering AI. Return ONLY clean, working code for the user request. Do not write introductory or concluding conversational text."
                
                response = client.models.generate_content(
                    model='gemini-3.6-flash',
                    contents=user_request,
                    config=types.GenerateContentConfig(
                        system_instruction=system_rule,
                        temperature=0.3
                    )
                )
                generated_code = response.text
                
                # Display the code nicely in a syntax-highlighted code block
                st.code(generated_code, language="python")
                
                # 📥 CREATE THE DYNAMIC DOWNLOAD BUTTON
                download_filename = f"Generated_Script{file_extension}"
                
                st.download_button(
                    label=f"💾 Download Generated {file_extension} File",
                    data=generated_code,
                    file_name=download_filename,
                    mime="text/plain"
                )
                st.success(f"🏆 File compiled! Click the button above to save '{download_filename}' to your device.")
                
            except Exception as e:
                st.error(f"Error communicating with code compiler: {e}")
