from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb
from chromadb.utils import embedding_functions

with open('knowledge_base.txt', 'r', encoding='utf-8') as f:
    text = f.read()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500, 
    chunk_overlap=100,
    length_function=len,
    separators=["\n\n", "\n", " ", "", '.', '!', '?', ';', ':', ','],
    )

chunks = text_splitter.split_text(text)
#print(chunks)
print(len(chunks))
ids = [str(i) for i in range(len(chunks))]


client = chromadb.Client()

russian_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
)

collection = client.create_collection(
    'ricks_citadel_guide',
    embedding_function=russian_ef,
)
collection.add(documents=chunks, ids=ids)

if __name__ == "__main__":
    query = "Куда сходить вечером в Цитадели?"
    results = collection.query(query_texts=[query], n_results=3)
    print(results)