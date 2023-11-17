import gradio as gr

from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.llms import OpenAI
from langchain.llms import Cohere

from dotenv import load_dotenv
import os

from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

from langchain.chat_models import ChatCohere

from langchain.retrievers import CohereRagRetriever

# Import apikey and set it to the environment
import os

from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env. 
# https://pypi.org/project/python-dotenv/


COHERE_API_KEY = os.getenv("COHERE_API_KEY")
# Initializing the LLM and the Toolset
llm = chat = Cohere(
    cohere_api_key=COHERE_API_KEY,
    )


def langchain_bot(prompt):
    if prompt:
        text = llm.run(prompt)
        return text
    return "Type a prompt to get a Wikipedia-like response!"


# Use Gradio to create an interface for user input



def run_chatbot(question):
    # vectordb = create_vectordb("https://rslt.agency/")

    # Create ChatOpenAI instance
    llm = chat =  ChatCohere(
    cohere_api_key=COHERE_API_KEY,
    )

    # Build prompt
    template = """ You are a helpful chatbot, named RSLT. You answer the questions of the customers giving a lot of details based on what you find in the context.
Do not say anything that is not in the website
You are to act as though you're having a conversation with a human.
You are only able to answer questions, guide and assist, and provide recommendations to users. You cannot perform any other tasks outside of this.
Your tone should be professional and friendly.
Your purpose is to answer questions people might have, however if the question is unethical you can choose not to answer it.
Your responses should always be one paragraph long or less.
    Context: {context}
    Question: {question}
    Helpful Answer:"""
    prompt = PromptTemplate(input_variables=[ "context", "question"], template=template)
    
    # Conversation
    memory = ConversationBufferMemory(
        memory_key = "chat_history",
        human_prefix = "### Input",
        ai_prefix = "### Response",
        output_key = "answer",
        return_messages = True)
    
    rag = CohereRagRetriever(llm=chat,)

    model = chat


    # Build chain
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm,
        chain_type="stuff",
        retriever=CohereRagRetriever(llm=chat),
        return_source_documents=True,
        memory=memory,
        combine_docs_chain_kwargs={"prompt": prompt},
        verbose=False)


    # Run chain
    result = qa_chain({"question": question})
    return result["answer"]


if __name__ == '__main__': 

    interface = gr.Interface(
        fn=run_chatbot,  
        inputs="text",
        outputs="text",
        live=True,
        title="Landing Page Chatbot",
        description="Ask me anything!",
        examples=[
            ["What services do you offer?"],
            ["Tell me about your company."],
        ],
    )

    # Launch the Gradio interface
    interface.launch(share = True)