import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext

from id import *
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ContentType, Message,InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters import Text

logging.basicConfig(level=logging.INFO)

bot = Bot(token=api)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_repo(message: types.Message):
    key = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but = types.KeyboardButton(text='Онлайн Заявка')
    key.add(but)
    await message.answer("Хотите подать заявку? ", reply_markup=key)

    @dp.message_handler(Text(equals="Онлайн Заявка"))
    async def send_types(message: types.Message):
        wer = types.ReplyKeyboardMarkup(resize_keyboard=True)
        reg = types.KeyboardButton(text="Проводные услуги")
        op = types.KeyboardButton(text="Мобильная связь")
        wer.add(reg)
        wer.add(op)
        await message.answer("Тип заявки", reply_markup=wer)

    @dp.message_handler(Text(equals="Мобильная связь"))
    async def send_numbers(message: types.Message):
        keyboard2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button4 = types.KeyboardButton(text="+998 99 9809996")
        keyboard2.add(button4)
        await message.answer("Выберите Номер", reply_markup=keyboard2)

    @dp.message_handler(Text(equals="+998 99 9809996"))
    async def get_tarrif(message: types.Message):
        ok = types.ReplyKeyboardMarkup(resize_keyboard=True)
        lj = types.KeyboardButton(text="Milliy 50")
        mj = types.KeyboardButton(text="Milliy 70")
        ok.add(lj)
        ok.add(mj)
        await message.answer("Выберите Тариф", reply_markup=ok)


    @dp.message_handler(Text(equals="Milliy 50"))
    async def get_type(message: types.Message):
        kd = types.ReplyKeyboardMarkup(resize_keyboard=True)
        sim = types.KeyboardButton(text="SIM")
        esim = types.KeyboardButton(text="Esim")
        kd.add(sim)
        kd.add(esim)
        await message.answer("Выберите способ подключения", reply_markup=kd)







    @dp.message_handler(Text(equals="SIM"))
    async def send_link(message: types.Message):
        ikm = InlineKeyboardMarkup(row_width=2)
        ikb = InlineKeyboardButton(text="Условия1", url="https://uztelecom.uz/ru/o-kompanii-1/publichnaya-oferta-1")
        ikb2 = InlineKeyboardButton(text='Условия2',
                                    url="https://uztelecom.uz/ru/chastnym-litsam/onlayn-bronirovanie-mobilnykh-nomerov/42260?page_id=899",
                                    )
        ikb3 = InlineKeyboardButton(text='✅Согласится ', callback_data='num')
        ikm.add(ikb, ikb2, ikb3)
        await message.answer('соглашение офертой',  reply_markup=ikm)

    @dp.callback_query_handler()
    async def vote_callback(callback: types.CallbackQuery):
        if callback.data == 'num':
            await callback.answer(text="Соглашение принято")

    @dp.message_handler()
    async def get_photo(message: types.Message):
        await message.answer("Отправьте фото паспорта")





if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)
