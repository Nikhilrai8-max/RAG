# Text is naturally organized into hierarchical units such as paragraphs, sentences, and words. We can leverage this inherent structure to inform our splitting strategy, creating split that maintain natural language flow, maintain semantic coherence within split, and adapts to varying levels of text granularity. LangChain’s RecursiveCharacterTextSplitter implements this concept:
# The RecursiveCharacterTextSplitter attempts to keep larger units (e.g., paragraphs) intact.
# If a unit exceeds the chunk size, it moves to the next level (e.g., sentences).
# This process continues down to the word level if necessary.
# It typically uses separators like:
# \n\n — paragraphs
# \n — lines
# " " — words
# "" — individual characters


from langchain_community.document_loaders import TextLoader


data = TextLoader(
    "Document_loader/notes.txt",
    encoding="utf-8"  #encoding of the text file
)

docs = data.load()


from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)
chunks = text_splitter.split_documents(docs)  # it splits the documents into smaller chunks based on the specified chunk size and overlap