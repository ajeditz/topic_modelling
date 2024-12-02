import streamlit as st
from pdf_reader import pdf_to_text, uploaded_pdf_to_text
from analyser import paperAnalyser

# Streamlit app interface
def main():
    st.set_page_config(page_title="Syllabus and PYQ Analyzer", layout="wide")
    # Center align the title
    st.markdown("<h1 style='text-align: center;'>9 Pointers</h1>", unsafe_allow_html=True)

    # Sidebar instructions
    with st.sidebar:
        st.header("Instructions:")
        st.markdown("""
            1. Upload the syllabus PDF in the 'Syllabus' section.
            2. Upload multiple previous year question PDFs in the 'Previous Year Question Papers' section.
            3. Optionally, provide any additional instructions.
            4. Press the 'Analyze Paper' button to get the analysis.
        """)

    # File upload for syllabus and PYQs
    syllabus_file = st.file_uploader("Upload Syllabus PDF", type="pdf")
    pyq_files = st.file_uploader("Upload Previous Year Question Papers (Multiple PDFs)", type="pdf", accept_multiple_files=True)

    # Input box for additional instructions
    additional_instructions = st.text_area("Additional Instructions",placeholder="Like : Give me 3 most important questions")

    # Button to analyze
    if st.button("Analyze Paper"):
        if syllabus_file and pyq_files:
            with st.spinner("Analyzing..."):
                syllabus_text = uploaded_pdf_to_text(syllabus_file)  # Extract text from syllabus using OCR
                pyqs_text = ""
                # Loop through each uploaded PYQ file and extract text
                for pyq in pyq_files:
                    pyqs_text += uploaded_pdf_to_text(pyq)  
                analysis_result = paperAnalyser(syllabus_text, pyqs_text, additional_instructions)  # Analyze the paper
                st.success("Analysis Complete!")
                st.text_area("Analysis Result", analysis_result, height=300)
        else:
            st.warning("Please upload both the syllabus and PYQ PDFs before analyzing.")

if __name__ == "__main__":
    main()