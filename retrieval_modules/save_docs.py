from modules.database import insert_items,get_db_connection
from  modules.preprocess import get_pdf_content, get_embeddings, get_chunks

def process_and_store_pdfs(pdf_files):
    conn, cursor = None, None
    try:
        for file in pdf_files:
            raw_text = get_pdf_content(file)

            text_chunks = get_chunks(raw_text)
            print(len(text_chunks))

            conn, cursor = get_db_connection()

            for chunk in text_chunks:
                embedding = get_embeddings(chunk) 
                insert_items(chunk, file, embedding, cursor, conn)

            print("All data processed and stored successfully!")
    except Exception as e:
        print("Error during processing:", e)
    finally:
        if cursor:
            cursor.close()  # Close cursor if it's initialized
        if conn:
            conn.close()  # Close connection if it's initialized
