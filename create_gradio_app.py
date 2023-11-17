import gradio as gr

from langchain import LLMChain
from langchain import PromptTemplate
from langchain.llms import Cohere

from create_chain import chain as llm_chain



def create_UI(llm_chain):
    with gr.Blocks() as demo:
        chatbot = gr.Chatbot()
        msg = gr.Textbox()
        clear = gr.Button("Clear")

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
    demo = create_UI(llm_chain)
    demo.queue()
    demo.launch()
    # pass