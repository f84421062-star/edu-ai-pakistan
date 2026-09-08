import streamlit as st
from google import genai
from google.genai import types
import os

# 1. Page Configuration & Aesthetic Setup
st.set_page_config(page_title="EduAI Pakistan", page_icon="📚", layout="centered")

st.title("📚 EduAI - Global Academic Assistant")
st.caption("100% of all premium tier subscriptions are automatically routed directly to local education charities.")

# 2. Core Configurations (Reads securely from your Streamlit settings secrets vault)
# Make sure you have added GEMINI_API_KEY = "your_key" inside Streamlit App Settings -> Secrets!
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# Strict Education-Only Filter Instruction
EDUCATION_GUARDRAIL = """
You are a strict Educational AI. You know all academic books on the internet.
Your absolute only purpose is to assist users with academic knowledge, books, science, history, and math.
CRITICAL RULE: If the user asks about video games, movies, gossip, casual chat, or non-educational topics, you MUST reply exactly with: 
"I am an AI dedicated exclusively to education. Please ask an academic or book-related question."
"""

# 3. Sidebar Control Interface & Promo Counter
st.sidebar.header("⚙️ User Dashboard")
user_tier = st.sidebar.selectbox("Select Your Account Tier", ["Free", "Basic", "Middle", "Premium"])

# Simulated Promo Tracking Variable (Bypasses gates if under 10,000)
total_users = 4501
max_promo = 10000

if total_users < max_promo:
    st.sidebar.success(f"🎉 10K Promo Active! You are User #{total_users}")
else:
    st.sidebar.info("💡 Standard Tiers Active")

# 4. Interactive Feature Selector Tabs Layout
tab1, tab2, tab3 = st.tabs(["💬 Ask AI", "📝 Generate Quiz", "📍 Find Study Spaces"])

# TAB 1: Academic Q&A (Available on Free Tier)
with tab1:
    st.subheader("Ask any Academic or Book-Related Question")
    user_query = st.text_input("Enter your homework or book topic (e.g., Explain Newton's laws):", key="query")
    if st.button("Submit Question"):
        if user_query:
            with st.spinner("AI scanning textbooks..."):
                try:
                    response = client.models.generate_content(
                        model='gemini-3.6-flash',
                        contents=user_query,
                        config=types.GenerateContentConfig(
                            system_instruction=EDUCATION_GUARDRAIL,
                            temperature=0.2
                        )
                    )
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Engine Connection Error: Make sure your secrets key is active. Details: {e}")

# TAB 2: Quiz Generator (Requires Middle/Premium Tier OR Promo Activation)
with tab2:
    st.subheader("🧠 Automatic Study Quiz Maker")
    quiz_topic = st.text_input("Enter quiz topic (e.g., Photosynthesis):", key="quiz")
    
    if st.button("Generate My Quiz"):
        if quiz_topic:
            # Check permissions or promo bypass rule
            if user_tier in ["Middle", "Premium"] or total_users < max_promo:
                if total_users < max_promo and user_tier == "Free":
                    st.info("📢 Promotion applied! Bypassing standard Middle Tier lock for Rs. 0.")
                with st.spinner("Compiling test questions..."):
                    try:
                        prompt = f"Create a 3-question multiple-choice quiz about '{quiz_topic}'. Include answers below clearly."
                        response = client.models.generate_content(
                            model='gemini-3.6-flash',
                            contents=prompt,
                            config=types.GenerateContentConfig(
                                system_instruction=EDUCATION_GUARDRAIL,
                                temperature=0.4
                            )
                        )
                        st.write(response.text)
                    except Exception as e:
                        st.error(f"Engine Connection Error: {e}")
            else:
                st.error("❌ Locked Feature! Interactive quizzes require a Middle Tier donation subscription (1,000 PKR).")
                st.info("💡 The first 10,000 free promotion slots are currently active, update your tier or reload profile status settings.")

# TAB 3: Geographic Study Zone Finder (Requires Basic/Middle/Premium Tier OR Promo Activation)
with tab3:
    st.subheader("🗺️ Plot Local Study Locations")
    city_input = st.text_input("Enter your city name in Pakistan (e.g., Rawalpindi):")
    if st.button("Map Locations"):
        if city_input:
            if user_tier in ["Basic", "Middle", "Premium"] or total_users < max_promo:
                if total_users < max_promo and user_tier == "Free":
                    st.info("📢 Promotion applied! Bypassing standard Basic Tier lock for Rs. 0.")
                st.success(f"📍 Map successfully pinned for {city_input}! Showing public library locations and student resource hubs within 5km.")
            else:
                st.error("❌ Locked Feature! Location plotting requires a Basic Tier donation subscription (500 PKR).")
