import re
import pandas as pd
import os
import json
import streamlit as st

from PyPDF2 import PdfReader
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_core.prompt_values import StringPromptValue
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def get_pdf_text(pdf_doc):
    text = ""
    pdf_reader = PdfReader(pdf_doc)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def extract_data(pages_data):
    template = '''
        You are a highly proficient invoice information extractor. 

        1. **Scrutinize the provided invoice image and extract ONLY the Customer Details, Products, and Total Amount.** Structure this data into a STRICTLY VALID JSON format.
        2. **Enclose all extracted values within double quotes.** Ensure any nested objects or arrays adhere to proper JSON syntax. 
        3. **Transform the Invoice data into JSON format.** Employ appropriate JSON tags corresponding to the data in the image. 
        4. **Return the JSON response without starting with ```json and ending with ```.**

        Invoice Data:
        {pages_data} 
    '''

    prompt_value = StringPromptValue(text=template.format(pages_data=pages_data))  

    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
    full_response = model.invoke(prompt_value) 

    parsed_data = json.loads(full_response.content)
    return parsed_data 

def create_docs(pdf_list):
    all_data = []
    for filename in pdf_list:
        raw_data = get_pdf_text(filename)
        json_data = extract_data(raw_data)
        all_data.append(json_data)
    return all_data

# Streamlit App
st.set_page_config(
    page_title="PDF to JSON Extractor", 
    page_icon="📄", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <div style='text-align: center; color: #2c3e50;'>
        <h1>📄 PDF to JSON Extractor 📝</h1>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <style>
    body {
        background-color: #f0f4f8;
        color: #F9E795;
    }
    .main {
        padding: 2rem;
        border-radius: 10px;
        background-color: #101820;
    }
    .stButton > button {
        background-color: #8AAAE5;
        font-color: #990011;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 0.8rem 1.2rem;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #2980b9;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .stSubheader {
        color: #34495e;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .stExpander {
        background-color: #ecf0f1;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stFileUploader label {
        background-color: #e0e6ed;
        padding: 1rem;
        border: 1px dashed #bdc3c7;
        border-radius: 5px;
        text-align: center;
        cursor: pointer;
        color: #34495e;
    }
    .stFileUploader label:hover {
        background-color: #d5dbdb;
    }
    .stFileUploader [type="file"] {
        display: none;
    }
    .sidebar .sidebar-content {
        background-color: #2c3e50;
        color: #ecf0f1;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

main_container = st.container()

with main_container:
    col1, col2 = st.columns([1, 2], gap="medium")

    with col1:
        st.subheader("📂 Upload your PDFs")
        uploaded_files = st.file_uploader(
            "",
            type="pdf", 
            accept_multiple_files=True,
            help="Drag and drop your PDF files here or click to browse",
        )

        if uploaded_files:
            st.success(f"✅ {len(uploaded_files)} file(s) uploaded!")

        extract_button = st.button("🚀 Extract Data", use_container_width=True)
        clear_button = st.button("🧹 Clear Files", on_click=lambda: st.experimental_rerun(), use_container_width=True)

    with col2:
        st.subheader("📝 Extracted JSON Data")
        if extract_button and uploaded_files:
            with st.spinner("🤖 Working on it... This may take a few moments."):
                all_extracted_data = create_docs(uploaded_files)
                st.success("✅ Extraction Complete!")

            for idx, data in enumerate(all_extracted_data):
                with st.expander(f"Invoice {idx + 1}", expanded=False):
                    st.json(data)
                    st.download_button(
                        label="📥 Download JSON",
                        data=json.dumps(data, indent=4),
                        file_name=f"extracted_data_{idx + 1}.json",
                        mime="application/json",
                        help="Download the extracted JSON data",
                        use_container_width=True
                    )
        elif extract_button and not uploaded_files:
            st.warning("⚠️ Please upload some PDFs first!")

with st.sidebar:
    st.header("Instructions for User")
    st.markdown("""
    1. **Upload PDFs**: Use the file uploader to select one or more PDF files.
    2. **Extract Data**: Click the 'Extract Data' button to process the files.
    3. **Review Results**: Expand each invoice section to view the extracted JSON data.
    4. **Download JSON**: Use the download buttons to save the extracted data for each invoice.
    5. **Clear Files**: Click 'Clear Files' to reset and upload new files.
    """)

    st.markdown("---")
    st.markdown("### About")
    st.info(
        "This app extracts invoice information from PDF files and converts it to JSON format. "
        "It uses AI to analyze the content and structure the data for easy processing."
    )