import time as times

from langchain.llms import OpenAI

start = times.time()
llm = OpenAI(
    streaming=True,
    temperature=0.7,
)

text = "Hướng dẫn các bước xây dựng một chatbot realtime"

prediction = llm(text)
end = times.time()
print(prediction.strip())
print(f"Time: {end - start}")
