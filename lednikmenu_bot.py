import telepot
import time
from pprint import pprint
from telepot.loop import MessageLoop

# token = '704863029:AAH271XQgaiUPOQ1jJniNDw3kToGuN2Exog' #lednikmenu_bot
token = '869400286:AAEnJt8AAzgypKOrh0UYf5lNqeEMak4d4ek' #robot-hobot

bot = telepot.Bot(token)

def handle(msg):
    id_chat = msg['chat']['id']
    pprint(str(id_chat) + '--' + msg['text'])
    if msg['text'] == '/start':
        bot.sendMessage(id_chat, "не надо")
    else:
        bot.sendMessage(id_chat, "Бот в разработке, скоро будет!")

MessageLoop(bot, handle).run_as_thread()

# Keep the program running.
while 1:
    time.sleep(10)