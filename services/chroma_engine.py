import os
from dotenv import load_dotenv
import chromadb
from chromadb.utils import embedding_functions

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

chroma_client = chromadb.PersistentClient(path="./db/chroma_persist")
embedding_fn = embedding_functions.OpenAIEmbeddingFunction(
    api_key=openai_api_key,
    model_name="text-embedding-3-small"
)

def get_or_create_collection(name="migration_law"):
    return chroma_client.get_or_create_collection(
        name, embedding_function=embedding_fn
    )

def add_documents_from_folder(collection, folder_path="data/"):
    import os
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
                doc_id = os.path.splitext(filename)[0]
                collection.upsert(ids=[doc_id], documents=[text])

def query_documents(collection, query_text, n_results=3):
    results = collection.query(query_texts=[query_text], n_results=n_results)
    return results
