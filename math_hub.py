import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. API Key Setup
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("Secrets mein GOOGLE_API_KEY nahi mili!")
else:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

st.set_page_config(page_title="Global Math Expert AI", page_icon="🌍")
st.title("Global Math Expert AI 🌍🎓")

# 2. Language Selection Dropdown
language = st.selectbox(
    "Choose your language / Apni bhasha chunein:",
    ["English", "Hindi", "Spanish", "French", "German", "Arabic", "Bengali", "Russian"]
)

# 3. Model Setup
model = genai.GenerativeModel('gemini-1.5-pro')

# 4. Input UI
input_text = st.text_area("Ask your question / Sawal puchein:")
uploaded_file = st.file_uploader("Upload Image/Photo:", type=["jpg", "png", "jpeg"])

if st.button("Solve Step-by-Step"):
    try:
        content = []
        # AI ko instruction dena ki kis language mein jawab chahiye
        instruction = f"Please solve this math problem step-by-step and provide the final explanation in {language} language."
        
        if input_text:
            content.append(f"{instruction}\n\nQuestion: {input_text}")
        if uploaded_file:
            img = Image.open(uploaded_file)
            content.append(instruction)
            content.append(img)
            
        if content:
            with st.spinner(f"Solving in {language}..."):
                response = model.generate_content(content)
                st.success(f"Solution in {language}:")
                st.write(response.text)
        else:
            st.warning("Please provide a question!")
            
    except Exception as e:
        st.error(f"Technical Error: {e}")

# Visitor Counter
st.markdown("---")
st.markdown("![Visitors](https://api.visitorbadge.io/api/combined?path=https%3A%2F%2Fmathexpertai.streamlit.app&labelColor=%2337d67a&countColor=%23263238&style=flat)")
