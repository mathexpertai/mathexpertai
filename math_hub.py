import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. API Key Setup
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("Secrets mein GOOGLE_API_KEY nahi mili!")
else:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

st.title("Global Math Expert AI 🌍🎓")

# 2. Language Selection
language = st.selectbox("Choose Language:", ["English", "Hindi", "Spanish", "French", "German"])

# 3. Model Setup (Using the most recent stable version)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# 4. Inputs
input_text = st.text_area("Question:")
uploaded_file = st.file_uploader("Upload Photo:", type=["jpg", "png", "jpeg"])

if st.button("Solve Now"):
    try:
        content = []
        prompt = f"Solve this math problem step-by-step in {language} language."
        
        if input_text:
            content.append(f"{prompt}\n\nQuestion: {input_text}")
        
        if uploaded_file:
            img = Image.open(uploaded_file)
            # Agar sirf image hai toh prompt pehle jayega
            if not input_text:
                content.append(prompt)
            content.append(img)
            
        if content:
            with st.spinner("Analyzing..."):
                response = model.generate_content(content)
                st.success(f"Solution in {language}:")
                st.write(response.text)
        else:
            st.warning("Please provide a question or photo!")
            
    except Exception as e:
        st.error(f"Technical Error: {e}")

# Visitor Counter
st.markdown("---")
st.markdown("![Visitors](https://api.visitorbadge.io/api/combined?path=https%3A%2F%2Fmathexpertai.streamlit.app&labelColor=%2337d67a&countColor=%23263238&style=flat)")
