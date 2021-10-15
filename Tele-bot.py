from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import random


def roll(st):
    R = ''
    while ' ' in st:
        st = st[:st.find(' ')] + st[st.find(' ') + 1:]
    n = st[:st.find('d')]
    if int(n) < 100 or n != '':
        n = int(n)
    else:
        n = 1
    print(n)
    if '+' in st:
        modif = int(st[st.find('+')+1:])
        d = int(st[st.find('d') + 1:st.find('+')])
    elif '-' in st:
        modif = - int(st[st.find('-')+1:])
        d = int(st[st.find('d') + 1:st.find('-')])
    else:
        modif = 0
        d = int(st[st.find('d') + 1:])
    s = 0
    for i in range(n):
        t = random.randint(1, d)
        s += t
        R += str('1d' + str(d) + ' = ' + str(t)+'\n')
    s = s + modif
    if modif > 0 or n != 1:
        R += str(str(n) + 'd' + str(d) + ' + ' + str(modif) + ' = ' + str(s))
    elif modif < 0 or n != 1:
        R += str(str(n) + 'd' + str(d) + ' - ' + str(abs(modif)) + ' = ' + str(s))
    print(R)
    return R


bot = Bot(token='2039550263:AAG4d-EGO4pMzolWBk5DdrVohTVWjv-2snA')
dp = Dispatcher(bot)
congr = ['твой бросок:', 'судьба на твоей стороне:', 'надеюсь повезет:', 'о великий рандом!']


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nВремя кидать кубы!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Надо просто написать какие кубы и сколько кинуть. Что-то вроде 5d6 + 7")


@dp.message_handler()
async def echo_message(msg: types.Message):
    z = random.choices(congr)[0]
    x = msg.chat.id
    y = msg.text
    if "d" in y:
        print('Надо посчитать', y)
        try:
            await bot.send_message(x, str(msg.from_user.username + ' '+ z +'\n' + roll(y)))
            print('Ура ответили')
        except:
            pass


if __name__ == '__main__':
    executor.start_polling(dp)