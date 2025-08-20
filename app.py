import streamlit as st
import google.generativeai as genai
import os

# Configure API (keep backend clean, no frontend mention)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Page setup
st.set_page_config(page_title="UX Questionnaire Generator", page_icon="📝")

st.title("📝 UX Questionnaire Generator")

# Input
prompt = st.text_area(
    "Enter context for questionnaire",
    placeholder="e.g., For a mobile banking app onboarding flow..."
)

# CTA
if st.button("Generate Questions"):
    if prompt.strip():
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(
            prompt + "\nGenerate 5 UX research questions for this context."
        )

        st.subheader("Generated Questions")
        st.write(response.text)

        # Copy to Clipboard
        st.code(response.text, language="markdown")
        st.button("📋 Copy to Clipboard", on_click=lambda: st.session_state.update(
            {"copied": response.text}
        ))
        
        if "copied" in st.session_state:
            st.success("✅ Questions copied to clipboard! (Press Ctrl+V to paste)")
    else:
        st.warning("Please enter some context first.")
