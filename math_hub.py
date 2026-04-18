import streamlit as st
import google.generativeai as genai

# API Setup
# Jyoti, apni API Key yahan paste karein
genai.configure(api_key="AQ.Ab8RN6LpOQT9Ya6UejrSG-MQHQbkeQxYp9atHc17Jmdz0x6DYA")

# Website Layout (Branding: Math Expert AI)
st.set_page_config(page_title="Math Expert AI", page_icon="🔢")
st.title("🔢 Math Expert AI")
st.markdown("#### Your Professional AI Professor for Step-by-Step Solutions")
st.write("Specialized in Calculus, Algebra, and Advanced Mathematics for students worldwide.")

# Model selection logic
try:
    models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    selected_model = 'models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in models else models[0]
except:
    selected_model = "gemini-1.5-flash"

# User Input Box
user_input = st.text_area("Enter your Math problem here:", placeholder="Example: Solve the integral of sin(x) dx")

if st.button("Solve Step-by-Step"):
    if user_input:
        with st.spinner('Math Expert AI is analyzing the problem...'):
            try:
                model = genai.GenerativeModel(selected_model)
                # Instruction to provide detailed solution
                response = model.generate_content(f"You are Math Expert AI. Solve this math problem step-by-step in English: {user_input}")
                st.success("Detailed Solution:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Something went wrong. Please try again later.")
    else:
        st.warning("Please type a question first!")

# Sidebar Branding
st.sidebar.title("Math Expert AI")
st.sidebar.info("Developed by: Jyoti (M.Sc. Mathematics)")
st.sidebar.write("Aiming to provide high-quality math education globally.")