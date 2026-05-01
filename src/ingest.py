import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
from langchain_postgres import PGVector

load_dotenv()

PDF_PATH = os.getenv("PDF_PATH")

def ingest_pdf():
    loader = PyPDFLoader(PDF_PATH)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=150)

    chunks = splitter.split_documents(docs)
    
    if not chunks:
        raise SystemExit(0)
    enriched = [
        Document(
            page_content=d.page_content,
            metadata={k: v for k, v in d.metadata.items() if v not in ("", None)}
        )
        for d in chunks
    ]    
    ids = [f"doc-{i}" for i in range(len(enriched))]
    #embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_EMBEDDING_MODEL","text-embedding-3-small"))
    embeddings = GoogleGenerativeAIEmbeddings(model=os.getenv("GOOGLE_EMBEDDING_MODEL","gemini-embedding-2-preview"))
    
    store = PGVector(
        embeddings=embeddings,
        collection_name=os.getenv("PG_VECTOR_COLLECTION_NAME"),
        connection=os.getenv("DATABASE_URL"),
        use_jsonb=True,
    )
    store.add_documents(documents=enriched, ids=ids)



if __name__ == "__main__":
    for k in ("OPENAI_API_KEY", "DATABASE_URL","PG_VECTOR_COLLECTION_NAME"):
        if not os.getenv(k):
            raise RuntimeError(f"Environment variable {k} is not set")
    try:
        ingest_pdf()
    except Exception as error:
        raise RuntimeError(f"ERROR:{error}")