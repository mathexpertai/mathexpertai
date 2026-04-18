import streamlit as st
import google.generativeai as genai
from PIL import Image

# Secrets se API Key lena
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

st.title("Math Expert AI 🎓")
st.write("Sawal likhein ya photo upload karein, step-by-step solution payein!")

# Model setup (Flash model photo/video ke liye best hai)
model = genai.GenerativeModel('gemini-1.5-flash')

# Input ke do tarike: Text ya Photo
input_text = st.text_area("Apna sawal yahan likhein:")
uploaded_file = st.file_uploader("Sawal ki photo ya video upload karein", type=["jpg", "jpeg", "png", "mp4"])

if st.button("Solve Step-by-Step"):
    if input_text or uploaded_file:
        with st.spinner("AI Professor soch raha hai..."):
            content = []
            if input_text:
                content.append(input_text)
            if uploaded_file:
                # Agar photo hai toh use process karein
                if uploaded_file.type.startswith('image'):
                    img = Image.open(uploaded_file)
                    content.append(img)
                # Video ke liye (Experimental)
                else:
                    content.append("Analyze this video and solve the math problem shown in it.")
            
            response = model.generate_content(content)
            st.success("Solution Taiyar Hai!")
            st.write(response.text)
    else:
        st.warning("Kripya kuch likhein ya photo upload karein.")

# --- Visitor Counter Badge ---
st.markdown("---")
st.markdown("![Visitors](https://api.visitorbadge.io/api/combined?path=https%3A%2F%2Fmathexpertai.streamlit.app&labelColor=%2337d67a&countColor=%23263238&style=flat)")
