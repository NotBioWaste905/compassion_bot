import telebot
from telebot import types
import markov_generator as mg
from tkn import TOKEN
import random

bot = telebot.TeleBot(TOKEN)

answers = {"good": 0, "bad": 0}

greeting = """hi"""

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, greeting)

@bot.message_handler(regexp=".*")
def send_message(message):
    ran = random.randint(1, 4)
    keyboard = types.InlineKeyboardMarkup()
    good = types.InlineKeyboardButton(text="Хороший ответ", callback_data="good")
    bad = types.InlineKeyboardButton(text="Плохой ответ", callback_data="bad")
    keyboard.add(good)
    keyboard.add(bad)

    if ran == 1:
        bot.send_message(message.chat.id, mg.gen(mg.model_cluster_1), reply_markup=keyboard)
    elif ran == 2:
        bot.send_message(message.chat.id, mg.gen(mg.model_cluster_2), reply_markup=keyboard)
    elif ran == 3:
        bot.send_message(message.chat.id, mg.gen(mg.model_cluster_3), reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, mg.gen(mg.model_cluster_4), reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def thank(call):
    if call.data == "good":
        answers["good"] += 1
    else:
        answers["bad"] += 1

    bot.send_message(call.message.chat.id, f"Спасибо за оценку! На моём счету уже {answers['good']} хороших ответов и {answers['bad']} плохих... Стараюсь быть лучше!")


if __name__ == '__main__':
    bot.polling(none_stop=True) 