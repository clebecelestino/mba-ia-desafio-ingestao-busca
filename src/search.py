
import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

PROMPT_TEMPLATE = """
CONTEXTO:
{contexto}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.

EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
Pergunta: "Qual é a capital da França?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Quantos clientes temos em 2024?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Você acha isso bom ou ruim?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

PERGUNTA DO USUÁRIO:
{question}

RESPONDA A "PERGUNTA DO USUÁRIO"
"""

def search_prompt(question=None):
    #embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_EMBEDDING_MODEL","text-embedding-3-small"))
    embeddings = GoogleGenerativeAIEmbeddings(model=os.getenv("GOOGLE_EMBEDDING_MODEL","gemini-embedding-2-preview"))
    store = PGVector(
        embeddings=embeddings,
        collection_name=os.getenv("PG_VECTOR_COLLECTION_NAME"),
        connection=os.getenv("DATABASE_URL"),
        use_jsonb=True,
    )
    results = store.similarity_search_with_score(question, k=10)
    return results