import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ParseMode
from config import TOKEN
from time import sleep
from pars import weather
from pars import weather1
from pars import weather2
from pars import kal

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Погода")
    keyboard.add(button_1)
    button_2 = types.KeyboardButton(text="Таймер")
    keyboard.add(button_2)
    button_3 = types.KeyboardButton(text="Календарь")
    keyboard.add(button_3)    
    button_4 = types.KeyboardButton(text="Помощь")
    keyboard.add(button_4)
    await message.answer('Спасибо, что выбрал меня. Чтобы узнать мои команды пиши "Помощь"', reply_markup=keyboard)

@dp.message_handler(commands='timer')
async def timer(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_5 = types.KeyboardButton(text="5 минут")
    keyboard.add(button_5)
    button_6 = types.KeyboardButton(text="30 минут")
    keyboard.add(button_6)
    button_7 = types.KeyboardButton(text="1 час")
    keyboard.add(button_7)
    await message.answer('Чтобы вернуться нажми /start', reply_markup=keyboard)


@dp.message_handler()
async def echo(message: types.Message):
    if "Помощь" in message.text:
        await message.answer("Мои команды: Погода, Таймер, Календарь")
    elif "Погода" in message.text:
        await message.answer('Погода в Челябинске {} градусов'.format(weather.text))
        sleep(0.5)
        await message.answer('{}'.format(weather1.text))
        sleep(0.5)
        await message.answer('{}'.format(weather2.text)) 
    elif "Таймер" in message.text:
        await message.answer("(Команды во время таймера не работают) Чтобы активировать таймер нажми /timer")
    elif "Календарь" in message.text:  
        await message.answer('Сегодня {}'.format(kal.text)) 
# с маленькой буквы
    elif "таймер" in message.text:
        await message.answer("(Команды во время таймера не работают) Чтобы активировать таймер нажми /timer")
    elif "календарь" in message.text:  
        await message.answer('Сегодня {}'.format(kal.text))
    elif "помощь" in message.text:
        await message.answer("Мои команды: Погода, Таймер, Календарь")
    elif "погода" in message.text:
        await message.answer('Погода в Челябинске {} градусов'.format(weather0.text))
        sleep(0.5)
        await message.answer('{}'.format(weather1.text))
        sleep(0.5)
        await message.answer('{}'.format(weather2.text))
# нет разницы с какой буквы            
    elif "30 минут" in message.text:
    	await message.answer('Таймер включен')
    	sleep(1800)
    	await message.answer('Прошло 30 минут! Чтобы вернуться нажми /start')
    elif "5 минут" in message.text:
    	await message.answer('Таймер включен')
    	sleep(300)
    	await message.answer('Прошло 5 минут! Чтобы вернуться нажми /start')
    elif "1 час" in message.text:
    	await message.answer('Таймер включен')
    	sleep(3600)
    	await message.answer('Прошел 1 час! Чтобы вернуться нажми /start')    	   	
# Неизвестная команда       
    else:
        await message.answer("Я тебя не понимаю:(")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)