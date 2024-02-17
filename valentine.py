




from telebot import TeleBot


bot = TeleBot('6774288462:AAHZ_EWC7TjU_wX0zhnew3cLL-dbqtoBFsQ')
TO_CHAT_ID = 1170688128
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Здравствуйте, это анонимный бот для ваших валентинок')
@bot.message_handler(content_types=['text', 'photo'])
def all_messages(message):
    if not(message.message_id == 'start'):
        bot.forward_message(2141073289, message.chat.id, message.message_id)
        bot.forward_message(6428648170, message.chat.id, message.message_id)
        bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)

bot.infinity_polling()