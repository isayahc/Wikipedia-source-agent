import gradio as gr

from langchain import LLMChain
from langchain import PromptTemplate
from langchain.llms import Cohere

import os

from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env. 
# https://pypi.org/project/python-dotenv/

COHERE_API_KEY = os.getenv("COHERE_API_KEY")


def create_UI(llm_chain):
    with gr.Blocks() as demo:
        chatbot = gr.Chatbot()
        msg = gr.Textbox()
        clear = gr.Button("Clear")
        # llm_chain, llm = llm, llm

        def user(user_message, history):
            return "", history + [[user_message, None]]

        def bot(history):
            print("Question: ", history[-1][0])
            bot_message = llm_chain(history[-1][0])

            bot_message = bot_message["text"]
            print("Response: ", bot_message)
            history[-1][1] = ""
            history[-1][1] += bot_message
            return history

        msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(bot, chatbot, chatbot)
        clear.click(lambda: None, None, chatbot, queue=False)
    return demo


if __name__ == "__main__":
    
    # Initializing the LLM and the Toolset
    llm = chat = Cohere(
        cohere_api_key=COHERE_API_KEY,
        )


    template = """Question: {question}
    Answer: Let's think step by step."""
    prompt = PromptTemplate(template=template, input_variables=["question"])

    llm_chain = LLMChain(prompt=prompt, llm=llm)

    demo = create_UI(llm_chain)

    demo.queue()
    demo.launch()