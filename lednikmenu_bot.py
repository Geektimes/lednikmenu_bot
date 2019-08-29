import telepot
token = '704863029:AAH271XQgaiUPOQ1jJniNDw3kToGuN2Exog' #lednikmenu_bot

SetProxy = telepot.api.set_proxy("http://136.243.47.220:3128")
bot = telepot.Bot(token)

from pprint import pprint
from telepot.loop import MessageLoop

def handle(msg):
 id_chat = msg['chat']['id']
 pprint(str(id_chat) + '--' + msg['text'])
 if msg['text'] == '/start':
     bot.sendMessage(id_chat, "не надо")
 else:
     bot.sendMessage(id_chat, "Бот в разработке, скоро будет!")

MessageLoop(bot, handle).run_as_thread()

# Keep the program running.
while True:
    n = input('To stop enter "stop":')
    if n.strip() == 'stop':
        break