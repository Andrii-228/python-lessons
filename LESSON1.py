import telebot

bot = telebot.TeleBot("your token here")
name='andriibot'
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.reply_to(message, "Привіт! Як твої справи?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text in ['добре', 'чудово', 'нормально']:
        bot.reply_to(message, 'Прекрасно, я радий це чути')
    elif message.text == 'справи так собі':
        bot.reply_to(message, 'Мені прикро, але сподіваюсь, що завтра справи будуть значно краще:)')
    elif message.text == 'Як тебе звати?':
        bot.reply_to(message, f'Мене звати {name}')    
    else:
        bot.reply_to(message, 'Вибач, я не запрограмований на цю відповідь')
        
    
bot.infinity_polling()
