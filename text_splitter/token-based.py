from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import TokenTextSplitter

splitter = TokenTextSplitter(
    chunk_size=100,
    chunk_overlap=10
)

data = TextLoader(
    "text_splitter/notes.txt",
    encoding="utf-8"  #encoding of the text file
)


docs = data.load()  # it loads a list of Document objects, each containing the text and metadata of a document
chunks = splitter.split_documents(docs)  # it splits the documents into smaller chunks based on the specified chunk size and overlap



#print(docs[0].page_content) # prints the content of the first document
print(chunks[0].page_content)  # prints the content of the first chunk

print(len(chunks))  # prints the number of chunks created