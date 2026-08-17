RAG = Retrieval-Augmented Generation.

It's a technique used in GenAI where an LLM retrieves relevant information from your own data first, and then uses that information to generate an answer.

Simple intuition

Without RAG:

User
 ↓
LLM
 ↓
Answer

The LLM answers mainly from what it learned during training.

With RAG:

User Question
      ↓
Retrieve relevant documents
      ↓
Relevant chunks
      ↓
LLM + retrieved context
      ↓
Answer
Example

Suppose you have a PDF containing your company's employee policies.

User asks:

"How many days of annual leave do employees get?"

A normal LLM may not know your company's specific policy.

With RAG:

Question
   ↓
Convert question → embedding
   ↓
Search vector database
   ↓
Find relevant policy paragraph
   ↓
Send paragraph + question to LLM
   ↓
"Employees receive 24 days of annual leave..."

The important part is that the LLM gets your actual document content as context.

Main components of a RAG system
              RAG PIPELINE


Documents
   │
   ▼
Load documents
   │
   ▼
Split into chunks
   │
   ▼
Create embeddings
   │
   ▼
Vector Database
   │
   │
   │ User question
   ▼
Question embedding
   │
   ▼
Similarity Search
   │
   ▼
Relevant chunks
   │
   ▼
LLM
   │
   ▼
Final Answer
What is an embedding?

An embedding converts text into a vector of numbers representing its semantic meaning.

For example:

"How much annual leave do I get?"
                ↓
        [0.12, -0.43, 0.87, ...]

A similar question such as:

"How many vacation days are allowed?"

will have a mathematically similar vector.

That's how the system finds relevant chunks even when the exact words don't match.

RAG vs Fine-tuning
RAG	Fine-tuning
Retrieves external knowledge	Changes model behavior/weights
Good for private documents	Good for specialized behavior/style
Easy to update documents	Retraining/update process needed
Can provide source context	Knowledge is incorporated into model
Common for PDF/chatbot systems	Common for specialized model behavior
Typical RAG tech stack

You might see:

Python
   ↓
LangChain / LlamaIndex
   ↓
Embedding Model
   ↓
FAISS / Chroma / Pinecone / Weaviate
   ↓
OpenAI / Gemini / Groq / Mistral / other LLM

Since you're working on a RAG project, the most useful thing to learn next is the complete RAG pipeline: document loading → chunking → embeddings → vector database → retrieval → prompt → LLM.