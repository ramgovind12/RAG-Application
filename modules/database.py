import psycopg2
import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from modules.preprocess import get_pdf_content, get_chunks, get_embeddings

load_dotenv()

def get_db_connection():
    DB_PARAMS = {
        'host': os.getenv('DBHOST'),
        'user': os.getenv('DBUSER'),
        'password': os.getenv('DBPASSWORD'),
        'dbname': os.getenv('DBNAME'),
        'port': os.getenv('DBPORT')  
    }

    conn = psycopg2.connect(**DB_PARAMS)
    cursor = conn.cursor()
    print("Connected to the database successfully!")
    return conn, cursor

def insert_items(text, filename, embedding, cursor, conn):
    try:
        sql = "INSERT INTO embeddings (text, filename, embedding) VALUES (%s, %s, %s);"
        cursor.execute(sql, (text, str(filename), embedding))       
        conn.commit()
        print("Data inserted successfully!")
    except Exception as e:
        print("Error inserting data:", e)

def process_and_store_pdfs(pdf_files):
    conn, cursor = None, None
    try:
        for file in pdf_files:
            raw_text = get_pdf_content(file)

            text_chunks = get_chunks(raw_text)
            print(len(text_chunks))

            model = SentenceTransformer("all-mpnet-base-v2")

            conn, cursor = get_db_connection()

            for chunk in text_chunks:
                embedding = model.encode(chunk).tolist()  
                insert_items(chunk, file, embedding, cursor, conn)

            print("All data processed and stored successfully!")
    except Exception as e:
        print("Error during processing:", e)
    finally:
        if cursor:
            cursor.close()  # Close cursor if it's initialized
        if conn:
            conn.close()  # Close connection if it's initialized
