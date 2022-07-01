from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, render_template, request
import requests

app = Flask(__name__)
# chatterbot
# chatterbot-corpus
# pyyaml
# spacy #python -m spacy download en
# jupyter
# notebook
# pint

bot = ChatBot("chatbot", read_only=False,
              logic_adapters=[
                  {
                      "import_path": "chatterbot.logic.BestMatch",
                      "default_response": "Sorry I don't have an answer",
                      "maximum_similarity_threshold": 0.9
                  }
              ])


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/get")
def get_chatbot_response():
    userText = request.args.get('userMessage')
    rawData = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + userText + "&appid=26203770279f77ce5cf2b691d7079383")
    # print(rawData)
    result = rawData.json()
    # print(result)
    return result


if __name__ == "__main__":
    app.run(debug=True)
