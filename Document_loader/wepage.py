from langchain_community.document_loaders import WebBaseLoader

data = WebBaseLoader(
    "https://www.geeksforgeeks.org/python-programming-language/"
)
docs = data.load()

print(len(docs))  # prints the number of documents loaded
  # prints the content of the first page