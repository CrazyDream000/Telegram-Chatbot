import pickle
import openai
import telebot

openai.api_key = "OPENAI_API_KEY"
telegram_key = "TELEGRAM_API_KEY"

bot = telebot.TeleBot(telegram_key)

def Generate_Respose(prompt):
    try:
        completions = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
    except:
        return "Openai server encountered a real time problem.\nPlease try again in some moments"
    message = completions.choices[0].text
    message = message.lstrip()
    return message


@bot.message_handler(content_types=['voice'])
def voice_processing(message):
    bot.reply_to(message, "Sorry, but I can't handle voice messages yet. I'm working on it.")


bot.infinity_polling()
