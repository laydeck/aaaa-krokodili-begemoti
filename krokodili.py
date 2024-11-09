from password import gen_pass

import telebot 
token='token'
    # Замени 'TOKEN' на токен твоего бота
    # Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot(token)
@bot.message_handler(func=lambda m: True, content_types=['new_chat_participant'])
def on_user_joins(message):
    if not is_api_group(message.chat.id):
        return

    name = message.new_chat_participant.first_name
    if hasattr(message.new_chat_participant, 'last_name') and message.new_chat_participant.last_name is not None:
        name += u" {}".format(message.new_chat_participant.last_name)

    if hasattr(message.new_chat_participant, 'username') and message.new_chat_participant.username is not None:
        name += u" (@{})".format(message.new_chat_participant.username)

    bot.reply_to(message, text_messages['welcome'].format(name=name))

# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)
        
@bot.message_handler(commands=['info'])
def send_info(message):
    print(message)
    bot.reply_to(message, message)
    
@bot.message_handler(commands=['gen_pass'])
def send_password(message):
    bot.reply_to(message, gen_pass(10))
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.send_message(message.chat.id, "манке")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")
    
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

print('бот запущен') 
bot.polling()
 
