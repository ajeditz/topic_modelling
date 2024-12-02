import google.generativeai as genai
from prompt import prompt
import streamlit as st
key=st.secrets["geminiAPIkey"]

genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-1.5-flash")



def paperAnalyser(syllabus, pyqs, additional_instructions):
    analysis=model.generate_content(prompt(syllabus,pyqs,additional_instructions))
    analysis=analysis.text
    
    return analysis
    

# if __name__=="__main__":
    # print(paperAnalyser(syllabus, pyqs))
