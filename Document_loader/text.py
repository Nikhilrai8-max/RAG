from langchain_community.document_loaders import TextLoader


data = TextLoader(
    "Document_loader/notes.txt",
    encoding="utf-8"  #encoding of the text file
)

docs = data.load()  # it loads a list of Document objects, each containing the text and metadata of a document



#print(docs[0].page_content) # prints the content of the first document
