import streamlit as st
import streamlit.components.v1 as components

# 1. Page Configuration & Professional Light Theme Style
st.set_page_config(page_title="FBISE Result Tracker", page_icon="🎓", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background-color: #f8fafc !important;
        color: #0f172a !important;
    }
    input, select {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 2px solid #1e3a8a !important;
        font-weight: bold !important;
    }
    h1, h2, h3, label, p {
        color: #1e3a8a !important;
    }
    .chat-bubble-user {
        background-color: #e0f2fe;
        padding: 12px;
        border-radius: 12px;
        color: #0369a1;
        margin: 8px 0;
        font-weight: bold;
        border-left: 4px solid #0284c7;
    }
    .status-box {
        background-color: #eff6ff;
        border-left: 5px solid #3b82f6;
        padding: 15px;
        border-radius: 4px;
        color: #1e40af;
        margin-bottom: 20px;
    }
    /* This wraps everything we want to photograph inside a clean screenshot container */
    #capture-area {
        padding: 15px;
        background-color: #f8fafc;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# HTML Wrapper Start for Screenshot Engine
st.markdown('<div id="capture-area">', unsafe_allow_html=True)

# 2. Page Headers
st.markdown("<h2 style='text-align: center;'>🏛️ FBISE Automated Result Tracker</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-weight: bold;'>Federal Board of Intermediate and Secondary Education, Islamabad</p>", unsafe_allow_html=True)

# 3. Status Alert Box
st.markdown("""
<div class='status-box'>
    <strong>ℹ️ Live Image Capture System Status:</strong><br>
    The script below captures an official .PNG image proof of your session dashboard instantly.
</div>
""", unsafe_allow_html=True)

# 4. Student Inputs
st.subheader("📋 Step 1: Candidate Account Setup")
roll_no = st.text_input("Enter Student Roll Number:", placeholder="e.g., 584321", max_chars=8)
exam_class = st.selectbox("Select Your Examination Class Tier:", ["SSC-I (Class 9)", "SSC-II (Class 10)", "HSSC-I (Class 11)", "HSSC-II (Class 12)"])

st.markdown("---")

# 5. Live Simulation Chat Box Component
st.subheader("💬 Step 2: Live Chat Testing Module")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"sender": "System", "text": "FBISE image automation engine initialized. Standby for capture test..."}
    ]

with st.form("chat_input_form", clear_on_submit=True):
    new_msg = st.text_input("Type a message to add to the screen display loop:")
    send_btn = st.form_submit_button("💬 Add Message")
    if send_btn and new_msg:
        st.session_state.chat_history.append({"sender": "User", "text": new_msg})

for msg in st.session_state.chat_history:
    st.markdown(f"<div class='chat-bubble-user'><b>[{msg['sender']}]:</b> {msg['text']}</div>", unsafe_allow_html=True)

# HTML Wrapper End for Screenshot Engine
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.subheader("📷 Step 3: Trigger PNG Screenshot Image Download")

# 6. The Magic Javascript Engine that photographs your web page canvas layout
screenshot_js = """
<script src="https://cloudflare.com"></script>
<script>
function takeActualScreenshot() {
    // Find the main chat area element on the page
    var element = window.parent.document.getElementById('capture-area');
    if(!element) {
        // Fallback search if iframe structure shifts
        element = window.parent.document.querySelector('.main') || window.parent.document.body;
    }
    
    // Photograph the HTML structure layout canvas
    html2canvas(element, { useCORS: true, logging: false }).then(function(canvas) {
        // Convert canvas drawings directly into a physical image download stream link
        var imageStream = canvas.toDataURL("image/png");
        var downloadTrigger = window.parent.document.createElement('a');
        downloadTrigger.href = imageStream;
        downloadTrigger.download = 'FBISE_Live_Chat_Screenshot.png';
        window.parent.document.body.appendChild(downloadTrigger);
        downloadTrigger.click();
        window.parent.document.body.removeChild(downloadTrigger);
    });
}
</script>
<button onclick="takeActualScreenshot()" style="
    background-color: #22c55e;
    color: white;
    border: none;
    padding: 12px 24px;
    font-size: 16px;
    font-weight: bold;
    border-radius: 8px;
    cursor: pointer;
    width: 100%;
">📸 Take Chat PNG Screenshot Image</button>
"""

# Embed the responsive javascript button frame securely into your interface workspace
components.html(screenshot_js, height=60)
