import streamlit as st
import google.generativeai as genai
from PIL import Image

# API Key Setup
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("Secrets mein GOOGLE_API_KEY nahi mili!")
else:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

st.title("Global Math Expert AI 🌍🎓")

language = st.selectbox("Choose Language:", ["English", "Hindi", "Spanish", "French"])

# INPUTS
input_text = st.text_area("Question:")
uploaded_file = st.file_uploader("Upload Photo:", type=["jpg", "png", "jpeg"])

if st.button("Solve Now"):
    try:
        # AGAR PHOTO HAI TO VISION MODEL, WARNA NORMAL MODEL
        model_name = 'gemini-pro-vision' if uploaded_file else 'gemini-pro'
        model = genai.GenerativeModel(model_name)
        
        content = []
        prompt = f"Solve this math problem step-by-step in {language}."
        
        if uploaded_file:
            img = Image.open(uploaded_file)
            content = [prompt, img]
        else:
            content = [f"{prompt}\n\nQuestion: {input_text}"]

        with st.spinner("Solving..."):
            response = model.generate_content(content)
            st.success("Solution:")
            st.write(response.text)
            
    except Exception as e:
        st.error(f"Technical Error: {e}")
