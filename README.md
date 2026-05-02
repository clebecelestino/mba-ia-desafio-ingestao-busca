# MBA Challenge in Software Engineering with AI - Full Cycle

Describe below how to implement your solution.

## Semantic Ingestion and Search with LangChain and Postgres
### Objective
You must deliver software capable of:
- Ingestion: Reading a PDF file and saving its information in a PostgreSQL database with the pgVector extension.
- Search: Allowing the user to ask questions via command line (CLI) and receive answers based solely on the PDF content.

### Mandatory technologies
- Language: Python
- Framework: LangChain
- Database: PostgreSQL + pgVector
- Docker & Docker Compose
  
### Required project structure
├── docker-compose.yml
├── requirements.txt   #Dependencies
├── .env.example       # OPENAI_API_KEY variable template
├── src/
│   ├── ingest.py   # PDF ingestion script
│   ├── search.py   # Search script
│   ├── chat.py     # CLI for user interaction
├── document.pdf    # PDF for ingestion
└── README.md       # Execution instructions
## New Project Structure
src/
├── config/settings.py
├── models/
│   ├── produto_model.py
│   └── usuario_model.py
├── views/
│   └── routes.py
├── controllers/
│   ├── produto_controller.py
│   └── pedido_controller.py
├── middlewares/error_handler.py
└── app.py (composition root)

## Project setup and execution
### VirtualEnv for Python
- Windows: 
`python -m venv venv
 venv\Script\activate.bat `
- Linux: 
`python3 -m venv venv
source venv/bin/activate `

### Execution order
1. Create the database: docker compose up -d
2. Install the libraries: pip install -r requirements.txt
3. Execute PDF ingestion: python src/ingest.py
4. Run the chat: python src/chat.py

## System requirement
1. PDF ingestion
- [X] The PDF should be divided into chunks of 1000 characters with an overlap of 150.
- [X] Each chunk must be converted into embedding.
- [X] Vectors should be stored in a PostgreSQL database using pgVector.
2. Consultation via CLI
- [X] Create a Python script to simulate a chat in the terminal.
- [X] Steps to take when receiving a question:
  - [X] Vectorize the question.
  - [X] Find the 10 most relevant results (k=10) in the vector database
  - [X] Set up the prompt and call the LLM.
  - [X] Return the answer to the user.
