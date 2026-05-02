from search import search_prompt, PROMPT_TEMPLATE
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

def main():
    question = 'Qual o faturamento da Empresa SuperTechIABrazil?'
    chain = search_prompt(question)
    if not chain:
        print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
        return
    system = ("system", PROMPT_TEMPLATE)
    user = ("human", "{question}")

    chat_prompt = ChatPromptTemplate([system, user])
    messages = chat_prompt.format_messages(contexto=chain, question=question)
    #for msg in messages:
    #    print(f"{msg.type}: {msg.content}")
    #model = ChatOpenAI(model="gpt-5-mini", temperature=0.5)
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",temperature=0.5)
    result = model.invoke(messages)
    print(result.content)

if __name__ == "__main__":
    main()