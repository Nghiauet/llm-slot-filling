import time as times

from langchain.callbacks.base import BaseCallbackHandler
from langchain.chat_models import ChatOpenAI

from app.slot_filling_conversation_stream import SlotFilling
from app.slot_memory import SlotMemory


class MyCallbackHandler(BaseCallbackHandler):
    def on_llm_new_token(self, token, **kwargs) -> None:
        # print every token on a new line
        print(f"#{token}#")


llm = ChatOpenAI(temperature=0.7)
memory = SlotMemory(llm=llm)
llm_stream = ChatOpenAI(temperature=0.7, streaming=True, callbacks=[MyCallbackHandler()])
slot_filling = SlotFilling(llm=llm_stream, memory=memory)
chain = slot_filling.create()
begin = times.time()
print(chain.predict(input="xin chào tôi bị đau chim"))
slot_filling.log()
end = times.time()
print(f"Done in {end - begin} seconds")

# command = input("You: ")

# while True:
#     start = times.time()
#     response = chain.predict(input=command)
#     end = times.time()
#     print(f"AI: {response}")
#     slot_filling.log()
#     print(f"Done in {end - start} seconds")
#     command = input("You: ")
#     if command == "exit":
#         break
