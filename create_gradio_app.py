import gradio as gr

from langchain import LLMChain
from langchain import PromptTemplate
from langchain.llms import Cohere

from create_chain import chain as llm_chain


examples = [
    ["The tower is 324 metres (1,063 ft) tall,"],
    ["The Moon's orbit around Earth has"],
    ["The smooth Borealis basin in the Northern Hemisphere covers 40%"],
]

def create_UI(llm_chain):
    with gr.Blocks() as demo:
        chatbot = gr.Chatbot()
        msg = gr.Textbox()
        clear = gr.Button("Clear")
        # gr.Examples(examples=examples, label="Examples", inputs=gr.Textbox(lines=5, max_lines=6, label=chatbot),)
        gr.Examples(examples=examples, label="Examples", inputs=msg,)

        def user(user_message, history):
            return "", history + [[user_message, None]]

        def bot(history):
            print("Question: ", history[-1][0])
            bot_message = llm_chain.invoke(history[-1][0])

            bot_message = bot_message
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
    # demo.launch()
    demo.launch(share=True)
    # pass