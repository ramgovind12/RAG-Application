import psycopg2
import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from modules.preprocess import get_pdf_content, get_chunks, get_embeddings


#loading environment variables
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

