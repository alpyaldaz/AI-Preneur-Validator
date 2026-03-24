import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI-Preneur Validator", page_icon="🚀")

st.title("🚀 AI-Preneur Startup Validator")
st.markdown("Instantly evaluate app ideas and generate technical roadmaps for the 301 App-preneurship Program.")

# User Inputs
api_key = st.text_input("Enter your Gemini API Key:", type="password")
idea = st.text_area("What is your app idea? (e.g., A marketplace for local bakers)")
target = st.text_input("Who is the target audience?")

if st.button("Validate My Idea"):
    if not api_key or not idea:
        st.warning("⚠️ Please enter your API Key and App Idea to proceed.")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = f"""
            Act as an expert App-preneur and Tech Lead. 
            Evaluate this app idea: '{idea}' for the target audience: '{target}'. 
            Provide: 
            1. Viability Score (out of 10) 
            2. Core MVP Features (Top 3) 
            3. Recommended Tech Stack 
            4. Potential Monetization Strategy.
            Keep it concise and professional.
            """
            
            with st.spinner("Analyzing market viability..."):
                response = model.generate_content(prompt)
                st.success("Analysis Complete!")
                st.markdown(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
