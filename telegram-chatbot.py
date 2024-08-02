import pickle
import openai
import telebot

openai.api_key = "OPENAI_API_KEY"
telegram_key = "TELEGRAM_API_KEY"

bot = telebot.TeleBot(telegram_key)

