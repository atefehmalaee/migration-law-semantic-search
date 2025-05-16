from services.chroma_engine import get_or_create_collection, add_documents_from_folder, query_documents

# Step 1: Load or create collection
collection = get_or_create_collection()

# Step 2: Add documents from /data folder
add_documents_from_folder(collection)

# Step 3: Query
query = "What are the visa requirements for skilled workers?"
results = query_documents(collection, query)

# Step 4: Print results
for idx, doc in enumerate(results["documents"][0]):
    print(f"\n🔍 Match {idx+1}:")
    print(f"Document ID: {results['ids'][0][idx]}")
    print(f"Distance: {results['distances'][0][idx]:.4f}")
    print(f"Content: {doc[:300]}...")
