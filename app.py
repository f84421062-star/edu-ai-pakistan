import streamlit as st
from google import genai
from google.genai import types

# 1. Page Configuration
st.set_page_config(page_title="EduAI Pakistan", page_icon="📚", layout="centered")

st.title("📚 EduAI - Global Academic Assistant")
st.caption("100% of all premium tier subscriptions are automatically routed directly to local education charities.")

# 2. Core Configurations
# Change client = genai.Client(api_key=API_KEY) to this:
import os
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

client = genai.Client(api_key=API_KEY)

# 3. Sidebar Control Interface
st.sidebar.header("⚙️ User Dashboard")
user_tier = st.sidebar.selectbox("Select Your Account Tier", ["Free", "Basic", "Middle", "Premium"])

# Simulated Promo Tracking
total_users = 4501
max_promo = 10000

if total_users < max_promo:
    st.sidebar.success(f"🎉 10K Promo Active! You are User #{total_users}")
else:
    st.sidebar.info("💡 Standard Tiers Active")

# 4. Feature Selector Tabs
tab1, tab2, tab3 = st.tabs(["💬 Ask AI", "📝 Generate Quiz", "📍 Find Study Spaces"])

with tab1:
    st.subheader("Ask any Academic or Book-Related Question")
    user_query = st.text_input("Enter your topic (e.g., Explain Newton's laws):", key="query")
    if st.button("Submit Question"):
        if user_query:
            with st.spinner("AI scanning books..."):
                response = client.models.generate_content(model='gemini-3.6-flash', contents=user_query)
                st.write(response.text)

with tab2:
    st.subheader("🧠 Automatic Study Quiz Maker")
    quiz_topic = st.text_input("Enter quiz topic (e.g., Photosynthesis):", key="quiz")
    
    if st.button("Generate My Quiz"):
        if user_tier in ["Middle", "Premium"] or total_users < max_promo:
            if total_users < max_promo and user_tier == "Free":
                st.info("📢 Promotion applied! Bypassing standard feature locks for Rs. 0.")
            with st.spinner("Compiling test questions..."):
                prompt = f"Create a 3-question multiple-choice quiz about '{quiz_topic}'. Include answers below."
                response = client.models.generate_content(model='gemini-3.6-flash', contents=prompt)
                st.write(response.text)
        else:
            st.error("❌ Locked Feature! Interactive quizzes require a Middle Tier donation subscription (1,000 PKR).")

with tab3:
    st.subheader("🗺️ Plot Local Study Locations")
    city_input = st.text_input("Enter your city name in Pakistan (e.g., Rawalpindi):")
    if st.button("Map Locations"):
        if user_tier in ["Basic", "Middle", "Premium"] or total_users < max_promo:
            st.success(f"📍 Map successfully pinned for {city_input}! Showing public library locations within 5km.")
        else:
            st.error("❌ Locked Feature! Location plotting requires a Basic Tier donation subscription (500 PKR).")
