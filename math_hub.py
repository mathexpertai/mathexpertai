import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. API Key Setup
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("Secrets mein GOOGLE_API_KEY nahi mili! Please Streamlit settings check karein.")
else:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

st.title("Math Expert AI 🎓")

# 2. Model Selection (Stable Version)
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. Input UI
input_text = st.text_area("Sawal likhein:")
uploaded_file = st.file_uploader("Photo upload karein:", type=["jpg", "png", "jpeg"])

if st.button("Solve Now"):
    try:
        content = []
        if input_text:
            content.append(input_text)
        if uploaded_file:
            img = Image.open(uploaded_file)
            content.append(img)
            
        if content:
            with st.spinner("AI Professor solve kar raha hai..."):
                response = model.generate_content(content)
                st.success("Solution:")
                st.write(response.text)
        else:
            st.warning("Kuch toh likhiye ya photo upload kariye!")
            
    except Exception as e:
        # Ye line humein asli error batayegi
        st.error(f"Technical Error: {e}")

# Visitor Counter
st.markdown("---")
st.markdown("![Visitors](https://api.visitorbadge.io/api/combined?path=https%3A%2F%2Fmathexpertai.streamlit.app&labelColor=%2337d67a&countColor=%23263238&style=flat)")
