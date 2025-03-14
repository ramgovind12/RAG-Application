# Retrieval Augmented Generation (RAG) Application with PGVector and Streamlit UI

This repository contains an implementation of a Retrieval Augmented Generation (RAG) application leveraging PostgreSQL with the PGVector extension as the vector database, and Streamlit for a user-friendly interface. This project demonstrates how to build a system that can retrieve relevant information from a knowledge base, use it to enhance the responses of a Large Language Model (LLM), and provide an interactive experience through a web UI.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Data Ingestion](#data-ingestion)
- [Querying via Streamlit UI](#querying-via-streamlit-ui)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Project Overview

This project aims to provide a practical example of building a RAG system with a user-friendly web interface. It focuses on:

-   **Vector Storage:** Utilizing PGVector for efficient storage and retrieval of vector embeddings.
-   **Knowledge Retrieval:** Implementing semantic search to find relevant information from a document corpus.
-   **LLM Integration:** Demonstrating how to integrate retrieved information with an LLM to generate informed responses.
-   **Streamlit UI:** Providing an interactive web interface for querying and visualizing results.
-   **Scalability:** Designing the system to be scalable and adaptable to larger datasets.

## Features

-   **PGVector Integration:** Seamless integration with PostgreSQL and the PGVector extension for vector storage and similarity search.
-   **Document Ingestion:** Scripts for ingesting and embedding documents into the vector database.
-   **Semantic Search:** Implementation of semantic search using vector embeddings.
-   **LLM Interaction:** Example of integrating retrieved information with an LLM (e.g., OpenAI, Hugging Face models).
-   **Streamlit UI:** User-friendly web interface for querying and displaying results.
-   **Configurable Parameters:** Easily configurable parameters for database connection, embedding models, and LLM settings.
-   **Clear Code Structure:** Well-organized code with clear documentation.

## Technologies Used

-   **Python:** Programming language for the application.
-   **PostgreSQL:** Relational database with PGVector extension.
-   **PGVector:** PostgreSQL extension for vector similarity search.
-   **Embedding Model (e.g., Sentence Transformers, OpenAI Embeddings):** For generating vector embeddings.
-   **LLM (e.g., OpenAI API, Hugging Face Transformers):** For generating responses.
-   **Streamlit:** For creating the web UI.
-   **Libraries:**
    -   `psycopg2` or `asyncpg` (for PostgreSQL interaction)
    -   `langchain` (optional, for RAG framework)
    -   `sentence-transformers` or `openai` (for embeddings)
    -   `streamlit` (for UI)
    -   `dotenv` (for environment variable management)
    -   (List other relevant libraries)

## Prerequisites

-   **PostgreSQL with PGVector:** Ensure PostgreSQL is installed and the PGVector extension is enabled. Refer to the PGVector documentation for installation instructions.
-   **Python 3.8+:** Python environment with necessary libraries installed.
-   **API Keys (if applicable):** API keys for embedding models and LLMs (e.g., OpenAI API key).

## Installation

1.  **Clone the repository:**

    ```bash
    git clone [repository_url]
    cd [repository_name]
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**

    -   Create a `.env` file in the root directory.
    -   Add the necessary environment variables, such as:

        ```
        POSTGRES_HOST=your_host
        POSTGRES_PORT=your_port
        POSTGRES_USER=your_user
        POSTGRES_PASSWORD=your_password
        POSTGRES_DB=your_database
        OPENAI_API_KEY=your_openai_api_key (if using OpenAI)
        EMBEDDING_MODEL=your_embedding_model_name (e.g., "sentence-transformers/all-mpnet-base-v2")
        ```

## Usage

## Configuration

-   Modify the `.env` file to configure database connection details, API keys, and other parameters.
-   Adjust configuration parameters within the Python scripts as needed.

## Data Ingestion

1.  **Prepare your document corpus:** Place your documents in a designated directory.
2.  **Run the ingestion script:**

    ```bash
    python ingest_data.py --data_path path/to/your/documents
    ```

    -   This script will read the documents, generate embeddings, and store them in the PGVector database.

## Querying via Streamlit UI

1.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

    -   This will launch the web UI in your browser.
2.  **Enter your query:** Use the provided text input to enter your search query.
3.  **View the results:** The application will display the retrieved information and the LLM's response in the web UI.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues to suggest improvements or report bugs.

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Commit your changes.
4.  Push to your fork.
5.  Submit a pull request.

## License

[MIT License](LICENSE) (or specify your chosen license)

## Acknowledgements

-   PGVector project: [https://github.com/pgvector/pgvector](https://github.com/pgvector/pgvector)
-   Streamlit: [https://streamlit.io/](https://streamlit.io/)
-   (List any other relevant projects or resources)
