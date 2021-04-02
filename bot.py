import aiogram
import requests
import matplotlib.pyplot as plt
import os

bot = aiogram.Bot(token = '1797033259:AAHRy5PszHmG1QUi_wgEyvC1e08fnOKKfPw')
dp = aiogram.Dispatcher(bot)
url = 'http://api.exchangeratesapi.io/v1/latest?access_key=767366a9c7b953b7d6f43e0e74e40329'
ex = requests.get(url).json()
@dp.message_handler(commands = ['list', 'lst'])
async def arrange(message):
    listq = ''
    for i in ex['rates']:
        listq = listq + i + ':' + str(round((ex['rates'][i]), 2)) + '\n'
    await message.answer(listq)

@dp.message_handler(commands = ['exchange'])
async def exchange(message):
    value = float(message['text'].split(' ')[1])
    first = message['text'].split(' ')[2]
    second = message['text'].split(' ')[4]
    for i in ex['rates']:
        if i == first:
            first1 = ex['rates'][i]

    for i in ex['rates']:
        if i == second:
            second1 = ex['rates'][i]
    result = second1*value/first1
    await message.answer(str(round(result,2)) +' '+ second)
@dp.message_handler(commands = ['history'])
async def history(message):
    first = message['text'].split(' ')[1]
    second = message['text'].split(' ')[2]
    for i in ex['rates']:
        if i == first:
            first1 = ex['rates'][i]

    for i in ex['rates']:
        if i == second:
            second1 = ex['rates'][i]
    x = [1, 2]
    y = []
    y.append(first1)
    y.append(second1)
    fig, ax = plt.subplots()
    ax = plt.bar(x,y)
    if os.path.exists('graph.png'):
        os.remove('graph.png')
    fig.savefig('graph.png')

    with open('graph.png', 'rb') as result:

        await bot.send_photo(message.chat.id, result)
        legend = "comparative statistics to EUR for "   + first + " and " +  second
        await message.answer(legend)
if __name__ == '__main__':

	aiogram.executor.start_polling(dp)

