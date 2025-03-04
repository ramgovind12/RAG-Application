from sentence_transformers import SentenceTransformer
from modules.database import get_db_connection
import json
from mistralai import Mistral

def retrieve_similar_vectors(query_text, top_k=5):
    model = SentenceTransformer("all-mpnet-base-v2")
    query_vector = model.encode(query_text).tolist()

    conn, cursor = get_db_connection()

    vector_str = json.dumps(query_vector)

    query = f"""
    SELECT text, 1 - (embedding <=> '{vector_str}'::vector) AS similarity
    FROM embeddings
    ORDER BY embedding <=> '{vector_str}'::vector
    LIMIT {top_k};
"""


    try:
        cursor.execute(query)
        results = cursor.fetchall()
    except Exception as e:
        print(f"Error retrieving vectors: ",e)
        results = []
    finally:
        cursor.close()
        conn.close()
    
    # if len(results) < top_k:
    #     print(f"Only {len(results)} similar vectors found.")
    return results


from langchain_community.llms import Ollama
from operator import itemgetter
from langchain.prompts import PromptTemplate


def generate_response_ollama(query):

    MODEL = "mistral:latest"

    context = retrieve_similar_vectors(query)
    model = Ollama(model=MODEL, temperature=0.7, num_predict=1000)

    prompt = f"""You are an AI assistant. Use the following retrieved documents as context to answer the question.
    
    Context:
    {context}
    
    Question: {query}
    
    Provide a concise and accurate answer based on the given information.
    """
    
    response = model(prompt)
    
    return response
