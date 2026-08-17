from click import prompt
from dotenv import load_dotenv

load_dotenv()
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_community.document_loaders import TextLoader

data = TextLoader(
    "Document_loader/notes.txt",
    encoding="utf-8"  #encoding of the text file
)
docs = data.load()

template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a summerzing assistant."),
        ("human", "{data}")
    ]
)


model = ChatMistralAI(
    model="mistral-small-latest"
)

prompt = template.format_prompt(data=docs[0].page_content)



result = model.invoke(prompt)
print(result.content)