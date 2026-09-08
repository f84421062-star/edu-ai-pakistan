import streamlit as st
from datetime import datetime

# 1. Page Configuration & Professional Light Theme Style
st.set_page_config(page_title="FBISE Result Tracker", page_icon="🎓", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background-color: #f8fafc !important;
        color: #0f172a !important;
    }
    input, select, textarea {
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
        padding: 10px;
        border-radius: 10px;
        color: #0369a1;
        margin: 5px 0;
        font-weight: bold;
    }
    .status-box {
        background-color: #eff6ff;
        border-left: 5px solid #3b82f6;
        padding: 15px;
        border-radius: 4px;
        color: #1e40af;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Page Headers
st.markdown("<h2 style='text-align: center;'>🏛️ FBISE Automated Result Tracker</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-weight: bold;'>Federal Board of Intermediate and Secondary Education, Islamabad</p>", unsafe_allow_html=True)

# 3. Status Alert Information Box
st.markdown("""
<div class='status-box'>
    <strong>ℹ️ Live System Status:</strong><br>
    Locker is online. Use the testing simulation module below to verify live text capturing logs.
</div>
""", unsafe_allow_html=True)

# 4. Interactive Class & Roll Number Setup
st.subheader("📋 Step 1: Candidate Account Setup")
roll_no = st.text_input("Enter Student Roll Number:", placeholder="e.g., 584321", max_chars=8)
exam_class = st.selectbox("Select Your Examination Class Tier:", [
    "SSC-I (Class 9)", "SSC-II (Class 10)", "HSSC-I (Class 11)", "HSSC-II (Class 12)"
])

st.markdown("---")

# 5. Live Simulation Chat Box Component
st.subheader("💬 Step 2: Live Chat Testing Module")
st.write("Type some test messages below to build up a chat history context.")

# Initialize a simple session memory loop list to store test chats
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"sender": "System", "text": "FBISE automation engine initialized. Waiting for test signals..."}
    ]

# Form to send a message safely into history state
with st.form("chat_input_form", clear_on_submit=True):
    new_msg = st.text_input("Type a message to add to the chat thread:")
    send_btn = st.form_submit_button("💬 Send to Thread")
    if send_btn and new_msg:
        st.session_state.chat_history.append({"sender": "User", "text": new_msg})

# Print out the current conversation logs layout screen
st.write("**Current Live Chat Stream:**")
for msg in st.session_state.chat_history:
    st.markdown(f"<div class='chat-bubble-user'><b>[{msg['sender']}]:</b> {msg['text']}</div>", unsafe_allow_html=True)

st.markdown("---")

# 6. The Snapshot Capture Generator Machinery
st.subheader("📷 Step 3: Compile Live Chat Screenshot")
st.write("Clicking the button below takes a text-capture screenshot of everything written above!")

if st.button("📸 Take Chat Live Screenshot"):
    timestamp_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Compile all lines of chat log array cleanly into a single file string
    chat_snapshot_text = f"""==================================================
📷 LIVE INTERFACE CHAT SCREENSHOT REPORT LOG
==================================================
[Timestamp Captured]: {timestamp_str}
[Target Portal Site]: FBISE Islamabad Automated Track
[Current Roll No]   : {roll_no if roll_no else 'Not Specified'}
[Target Class Tier] : {exam_class}
--------------------------------------------------
📜 CONVERSATION THREAD RECORD ENTRIES:
"""
    for msg in st.session_state.chat_history:
        chat_snapshot_text += f"\n👉 [{msg['sender']}]: {msg['text']}"
        
    chat_snapshot_text += "\n=================================================="
    
    # Display the final compiled capture blueprint matrix text on screen
    st.success("🎉 Chat interface snapshot successfully compiled into file storage format!")
    st.text(chat_snapshot_text)
    
    # 📥 GENERATE THE CLICKABLE ASSET FILE DOWNLOAD TRIGGER BUTTON
    st.download_button(
        label="📥 Download Chat Screenshot File (.txt)",
        data=chat_snapshot_text,
        file_name=f"Chat_Screenshot_Log_{roll_no if roll_no else 'Test'}.txt",
        mime="text/plain"
    )
