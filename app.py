import os
import streamlit as st
from dotenv import load_dotenv
from modules.rag_engine import retrieve_similar_vectors
from modules.rag_engine import generate_response_ollama
from modules.database import process_and_store_pdfs


# os.environ["STREAMLIT_SERVER_ADDRESS"] = "192.168.1.33"
# os.environ["STREAMLIT_SERVER_PORT"] = "8501"
# os.environ["STREAMLIT_SERVER_ENABLECORS"] = "false"


load_dotenv()

# Function to store uploaded files
def store_uploaded_file(uploaded_files, uploaded_file_names):
    if uploaded_files:
        for uploaded_file in uploaded_files:
            file_path = os.path.join('data', uploaded_file.name)
            with open(file_path, 'wb') as f:
                f.write(uploaded_file.getbuffer())
            uploaded_file_names.append(uploaded_file.name)

    st.success(f"Uploaded {len(uploaded_files)} file(s): {', '.join(uploaded_file_names)}")

# Function to add to database
def add_to_database(uploaded_files):
    updated_file_paths = ['data/' + uploaded_file.name for uploaded_file in uploaded_files]
    process_and_store_pdfs(updated_file_paths)

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
            store_uploaded_file(uploaded_files, uploaded_file_names)  # Store files and update list
            add_to_database(uploaded_files)  # Add to database

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




