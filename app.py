import streamlit as st
from pdfextract import extract_text_from_pdf
from similarity import rank_resumes

st.title("Resume Screening App")

resume_text = []

uploaded_files = st.file_uploader(
    "Upload Resumes", accept_multiple_files=True, type="pdf")


job_description = st.text_area("Enter Job Description")

if uploaded_files:
    for file in uploaded_files:
        text = extract_text_from_pdf(file)
        resume_text.append(text)

pressed = st.button("Rank Resumes")

if pressed:
    if not job_description:
        st.warning('Please enter job description', icon="⚠️")
    elif not resume_text:
        st.warning("Please upload resumes", icon="⚠️")
    else:
        st.write("Ranking Resumes...")
        ranked_resumes = rank_resumes(job_description, resume_text)
        for i in range(len(ranked_resumes)):
            st.write(f"Resume {i+1}")
            st.write(ranked_resumes['Resume'].iloc[i].strip()[:300] + "...")
            st.write(
                f"Similarity Score: {ranked_resumes['Similarity Score'].iloc[i]}")
            st.write("------")
