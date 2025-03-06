import os
import streamlit as st
from dotenv import load_dotenv
from modules.rag_engine import retrieve_similar_vectors
from modules.rag_engine import generate_response_ollama
from retrieval_modules.save_docs import process_and_store_pdfs


# os.environ["STREAMLIT_SERVER_ADDRESS"] = "192.168.1.33"
# os.environ["STREAMLIT_SERVER_PORT"] = "8501"
# os.environ["STREAMLIT_SERVER_ENABLECORS"] = "false"


load_dotenv()

DATA_FOLDER = "data"

def store_files(uploaded_files):
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)
    for file in uploaded_files:
        file_name = file.name
        file_path = os.path.join(DATA_FOLDER,file_name)

        with open(file_path,"wb") as f:
            f.write(file.getbuffer())
        print(f"File saved to {file_path}")

def save_in_database(uploaded_files):
    files = [os.path.join(DATA_FOLDER,file.name) for file in uploaded_files]
    process_and_store_pdfs(files)


# Streamlit app layout
st.title("Search with RAG")

# Initialize list to store filenames
uploaded_file_names = []

# Ensure the 'data' folder exists
if not os.path.exists('data'):
    os.makedirs('data')

# Upload documents via Streamlit sidebar
with st.sidebar:
    st.header("Upload Document")
    uploaded_files = st.file_uploader("Choose a file", type=["pdf"], accept_multiple_files=True)
    
    # Trigger actions only when files are uploaded and button is clicked
    if uploaded_files:
        if st.button("Store and Add to Database"):
            store_files(uploaded_files)
            save_in_database(uploaded_files)
            

# Display the uploaded file names on the main screen
if uploaded_file_names:
    st.write("Uploaded Files:", ", ".join(uploaded_file_names))




query = st.text_input("Enter your query:")


if st.button("Get Response"):
    if query:
        st.info("Fetching relevant context and generating response...")
        response = generate_response_ollama(query)
        st.success(response)
    else:
        st.warning("Please enter a query to continue.")




