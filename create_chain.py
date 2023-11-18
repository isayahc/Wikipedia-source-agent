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

load_dotenv()  # take environment variables from .env. 
# https://pypi.org/project/python-dotenv/


COHERE_API_KEY = os.getenv("COHERE_API_KEY")

chat = ChatCohere(
    cohere_api_key=COHERE_API_KEY,
    )


template = """Question: {query}

Please only use wikipedia when searching for the answer.




When given a query you must generate a wikipedia article based on the query given;
You must oranization your article into sections just like in wikipedia
The structure is open ended however you must write this article in markdown;
Also you must have a reference section at the end with a list of all your refernces;
If you are unsure about the exact person the user is refering to please ask questions;

For the sake of clarity please add new lines between your inital output and the
generated wikipedia article


If there are many pages for a similar person or entity please as
the user to specify which one they are talking about before geenrating the article

Please make sure to include in-line citations

for example:
fact_1 [source_1]
fact_2 [source_2, source_3]
Answer: 
"""


prompt = PromptTemplate(template=template, input_variables=["query"])

# from cohere import conn

rag = CohereRagRetriever(llm=chat,)

model = chat
retriever = rag

def format_docs(docs):
    return "\n\n".join([d.page_content for d in docs])


chain = (
    {"context": retriever | format_docs, "query": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)



# if __name__ == "__main__":
#     sample = chain.invoke("Who is Barack Obama?")
#     print(sample)