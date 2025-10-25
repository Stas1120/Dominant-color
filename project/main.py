import telebot
from colours import dominant_color
import os

# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
   bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')
   
@bot.message_handler(content_types=['photo'])
def photo(message):
    if message.photo:
        file_info = bot.get_file(message.photo[-1].file_id)
        print(file_info)
        file_name = file_info.file_path.split('/')[-1]
        downloaded_file = bot.download_file(file_info.file_path)
        with open(file_name, 'wb') as new_file:
            new_file.write(downloaded_file)
        res = dominant_color(f"./{file_name}")
        bot.reply_to(message, f"На изображении преобладает {res}")
        os.remove(f"./{file_name}")
    else:
          bot.reply_to(message, "Вы забыли отправить изображение")
bot.polling()