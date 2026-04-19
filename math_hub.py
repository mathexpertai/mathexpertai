import streamlit as st
import google.generativeai as genai
from PIL import Image

# Secrets se API Key lena
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

st.set_page_config(page_title="Math Expert AI", page_icon="🎓")
st.title("Math Expert AI 🎓")
st.write("Sawal likhein ya photo upload karein, step-by-step solution payein!")

# Model setup - Gemini 1.5 Flash (Sabse fast aur photo ke liye best)
model = genai.GenerativeModel('gemini-pro')

# Input Options
input_text = st.text_area("Apna sawal yahan likhein:", placeholder="Example: Solve the integral of sin(x) dx")
uploaded_file = st.file_uploader("Sawal ki photo upload karein", type=["jpg", "jpeg", "png"])

if st.button("Solve Step-by-Step"):
    if input_text or uploaded_file:
        with st.spinner("Math Expert AI is analyzing the problem..."):
            try:
                content = []
                if input_text:
                    content.append(input_text)
                if uploaded_file:
                    img = Image.open(uploaded_file)
                    content.append(img)
                
                # AI se response mangna
                response = model.generate_content(content)
                
                st.success("Detailed Solution:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Something went wrong. Please try again later.")
    else:
        st.warning("Please type a question or upload an image first!")

# --- Visitor Counter ---
st.markdown("---")
st.markdown("![Visitors](https://api.visitorbadge.io/api/combined?path=https%3A%2F%2Fmathexpertai.streamlit.app&labelColor=%2337d67a&countColor=%23263238&style=flat)")
