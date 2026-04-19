import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. API Key Setup
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("Secrets mein GOOGLE_API_KEY nahi mili!")
else:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

st.title("Global Math Expert AI 🌍🎓")

# 2. Smart Model Selection Logic (Aapka Idea)
try:
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    # Check karte hain ki Flash mil raha hai ya nahi, warna pehla available model le lenge
    if 'models/gemini-1.5-flash' in available_models:
        selected_model = 'models/gemini-1.5-flash'
    elif 'models/gemini-1.5-pro' in available_models:
        selected_model = 'models/gemini-1.5-pro'
    else:
        selected_model = available_models[0]
except Exception as e:
    # Agar list nahi mil rahi toh default par chale jayenge
    selected_model = "gemini-1.5-flash"

# Model ko set karna
model = genai.GenerativeModel(selected_model)

# 3. Language Selection
language = st.selectbox("Choose Language:", ["English", "Hindi", "Spanish", "French", "German"])

# 4. Input UI
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
            if not input_text:
                content.append(prompt)
            content.append(img)
            
        if content:
            with st.spinner(f"Using {selected_model} to solve..."):
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
