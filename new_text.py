from dotenv import load_dotenv, find_dotenv
from langchain.llms import OpenAI

load_dotenv(find_dotenv())

llm = OpenAI(temperature=0)

status = True

while status:
    text = input("\nDigite sua pergunta: ")

    print(llm(text)) 

    test = input("Continuar [s]sim [n]não: ")

    status = True if test == 's' else False

