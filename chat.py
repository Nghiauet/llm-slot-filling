from langchain.chat_models import ChatOpenAI

from app.slot_filling_conversation import SlotFilling
from app.slot_memory import SlotMemory

llm = ChatOpenAI(temperature=0.7)
memory = SlotMemory(llm=llm)
slot_filling = SlotFilling(llm=llm, memory=memory)
chain = slot_filling.create()

command = input("You: ")
import time as times

while True:
    start = times.time()
    response = chain.predict(input=command)
    end = times.time()
    print(f"AI: {response}")
    slot_filling.log()
    print(f"Done in {end - start} seconds")
    command = input("You: ")
    if command == "exit":
        break
