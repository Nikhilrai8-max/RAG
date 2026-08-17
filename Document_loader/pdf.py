from langchain_community.document_loaders import PyPDFLoader

data = PyPDFLoader(
    "Document_loader/sample.pdf"  # encoding of the text file
)


docs = data.load()

print(len(docs))  # prints the number of pages in the PDF each page is a separate document and contains the text and metadata of that page


