from aiogram import types
from aiogram.types import InputFile
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.bio import categoryMenu 

from loader import dp

@dp.message_handler(CommandStart())
async def select_start(message: types.Message):
    photo_file = InputFile(path_or_bytesio='photo/otb.jpg')
    await message.answer_photo(photo_file,f'Salom{message.from_user.first_name} <b>Otajon Bozorboyev</b>ning shaxsiy boti', reply_markup = categoryMenu)    
