from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import CharacterTextSplitter


def get_pdf_content(documents):
    if isinstance(documents, str):
        documents = [documents]

    raw_text = ""

    for document in documents:
        try:
            pdf_reader = PdfReader(document)
            for page in pdf_reader.pages:
                text = page.extract_text()
                if text:  
                    raw_text += text
        except FileNotFoundError:
            print(f"File not found: {document}")
        except Exception as e:
            print(f"An error occurred while processing {document}: {e}")

    return 


def get_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    text_chunks = text_splitter.split_text(text)
    return text_chunks


def get_embeddings(chunk):
    model = SentenceTransformer("all-mpnet-base-v2")
    embeddings = model.encode(chunk)
    return embeddings