import os 
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv() #Read the .env file and load the environment variables


llm = init_chat_model(
    model= os.getenv(key="MODEL_NAME"),
    temperature=os.getenv(key="TEMPERATURE"),
    api_key=os.getenv(key="API_KEY")
)

SYSTEM_PROMPT = "You are a helpful AI Assistant!"

history = [
    {"role": "system", "content" : SYSTEM_PROMPT}
    ]

print ("Welcome to Cue Chat!")

while True:
    question= input("You! ").strip()

    if not question:
        continue

    if question.lower() in ("exit", "quit", "bye"):
        print ("Goodbye!")
        break

    history.append({"role" : "user", "content": question})
    response = llm.invoke(input=history)
    history.append({"role": "assistant", "content": response.content})
    print(f"Bot: {response.content}")