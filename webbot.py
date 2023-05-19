import streamlit as st
import pandas as pd
import base64
import os
from dotenv import load_dotenv
import openai
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
# from pandasai.llm.openai import OpenAI
# from pandasai import PandasAI

embeddings = HuggingFaceEmbeddings()
load_dotenv()
#Token OPENAPI
openaitoken = os.getenv('OPENAI_TOKEN')
openai.api_key = openaitoken

LOGO_IMAGE = "./bluspd.png"
st.markdown(
    f"""
    <div style="text-align: center;">
    <img class="logo-img" src="data:png;base64,{base64.b64encode(open(LOGO_IMAGE, 'rb').read()).decode()}">
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("<h1 style='text-align: center; color: #c7913d; font-family:sans-serif'>CHATBLU</h1>", unsafe_allow_html=True) 
st.markdown("<h3 style='text-align: center; color: #1498b0; font-family:sans-serif'>Your everyday trusted companion</h3>", unsafe_allow_html=True)
menu = st.sidebar.selectbox("Select Menu", ("Chat dengan GPT-4","Document Analytic", "Data to Insight","Knowledge Base PPKBLU"))

if menu == "Chat dengan GPT-4":
    st.write("Chat Dengan ChatBLU")
    prompt = st.text_area('Masukkan pertanyaan yang ingin ditanyakan :')
    if st.button ("Run Prompt"):
        response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
        with st.spinner('Wait for it...'):
            st.write("Selesai")
        
        st.text_area("Response",value = response.choices[0].text)
if menu == "Document Analytic":
    st.write(" ## 🛠 Under Construction ")
if menu == "Knowledge Base PPKBLU":
    st.write("Chat dengan Peraturan BLU")
    st.write("### Saat ini baru tersedia dengan PMK 129/2020")
    question = st.text_area("Question")
    if st.button("Tanya"):
        new_db = FAISS.load_local("faiss", embeddings)
        docs = new_db.similarity_search(question)
        st.write(docs[0].page_content)
    
if menu == "Data to Insight":
    st.write(" ## 🛠 Under Construction ")
    # llm = OpenAI(api_token=openaitoken)
    # pandas_ai = PandasAI(llm)