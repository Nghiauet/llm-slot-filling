import gradio as gr
from langchain.chat_models import ChatOpenAI

from app.slot_filling_conversation import SlotFilling
from app.slot_memory import SlotMemory

llm = ChatOpenAI(temperature=0.2)
memory = SlotMemory(llm=llm)
print("Loading...")
slot_filling = SlotFilling(llm=llm, memory=memory)
print("Done!")
chain = slot_filling.create()


def execute_chat(message, history):
    print(f"You: {message}")
    history = history or []
    response = chain.predict(input=message)
    print(f"AI: {response}")
    slot_filling.log()
    history.append((message, response))
    return history, history


chatbot = gr.Chatbot().style(color_map=("green", "pink"))
demo = gr.Interface(
    execute_chat,
    ["text", "state"],
    [chatbot, "state"],
    # allow_flagging="never",
)
if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
    )
