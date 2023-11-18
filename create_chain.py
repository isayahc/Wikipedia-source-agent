import os

from langchain.chat_models import ChatCohere
from langchain.schema import AIMessage, HumanMessage


## cohere with connector
## cohere with internet

# https://python.langchain.com/docs/modules/data_connection/retrievers/
# https://python.langchain.com/docs/integrations/llms/cohere

from langchain.chat_models import ChatCohere
from langchain.retrievers import CohereRagRetriever
from langchain.schema.document import Document

from langchain.chains import LLMChain
from langchain.llms import Cohere
from langchain.prompts import PromptTemplate


from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough

# from langchain.chat_models import SystemMessagePromptTemplate

from langchain.prompts import (
ChatPromptTemplate,
MessagesPlaceholder,
SystemMessagePromptTemplate,
HumanMessagePromptTemplate,
                                )
from dotenv import load_dotenv

from prompt import wikipedia_template, general_internet_template

load_dotenv()  # take environment variables from .env. 
# https://pypi.org/project/python-dotenv/

def format_docs(docs):
    return "\n\n".join([d.page_content for d in docs])


COHERE_API_KEY = os.getenv("COHERE_API_KEY")

chat = ChatCohere(
    cohere_api_key=COHERE_API_KEY,
    )

template = wikipedia_template
prompt = PromptTemplate(template=template, input_variables=["query"])

rag = CohereRagRetriever(llm=chat,)

model = chat
retriever = rag


chain = (
    {"context": retriever | format_docs, "query": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

def create_chain_from_template(template, retriever, model):
    prompt = PromptTemplate(template=template, input_variables=["query"])
    chain = (
        {"context": retriever | format_docs, "query": RunnablePassthrough()}
        | prompt
        | model
        | StrOutputParser()
    )
    return chain



# if __name__ == "__main__":
#     sample = chain.invoke("Who is Barack Obama?")
#     print(sample)