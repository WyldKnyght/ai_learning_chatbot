from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Elsie_AI')

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')