import gradio as gr
from ch7.chatbot_gradio.gpt4_integration import get_tongyichat_answer

def chatbot(question):
    return get_tongyichat_answer(question)

iface = gr.Interface(fn=chatbot, inputs="text", outputs="text")
iface.launch()