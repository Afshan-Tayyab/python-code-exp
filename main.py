import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

st.title("🐍 Python Code Explainer")

code = st.text_area("Type your Python code here:")

if st.button("Explain Code"):
    if code.strip() == "":
        st.warning("Please enter some Python code first.")
    else:
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"Explain this Python code in simple terms:\n\n{code}"
            )

            st.subheader("Explanation:")
            st.markdown(response.text)

        except Exception as e:
            st.error(f"Error: {e}")