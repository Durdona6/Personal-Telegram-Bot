from aiogram.types import Message, CallbackQuery
from loader import dp
from keyboards.inline.bio import categoryMenu
from keyboards.inline.social import main_menu,SocialNetworks, resume
from aiogram.types import InputFile



@dp.callback_query_handler(text='bio')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/photo.jpg')
    msg = '<b>Ismi-sharifi:</b>\nOtajon Bozorboyev'
    msg += "<b>Tug'ilgan yili va joyi:</b>\n8-yanvar 1999-yil;\nJizzax viloyati,Jizzax shahri\n"
    msg += "<b>Ta'limi:</b>\nToshkent temir yo'l transport kasb-hunar kolleji (2018)\n"
    msg += "<b>Ish tajribasi:</b>\n"
    msg += """"-O'zbekiston temir yo'llari" AJ tashkiloti Jizzax temir yo'l msasofasi xodimlar bo'limi nazoratchisi (HR)(2018-2023);\n-Astro Education Python Backend Mentor(2023-2024);Tramplin IT Academy Backend dasturchi va Pythin backend mentor (2024-hozirgacha)\n"""
    msg += "<b>Texnik ko'nikmalari:</b>\nC, Python, Django, Django Rest, SQLite, MySQL, PostgreSQL, Git, GitHub, HTML, CSS, Java Script, Telegram Bot, Microsoft Office(Word, Excel, Power Point, Paint, va h.k.lar)\n"
    msg += "<b>Tillar:</b>\nO'zbek tili(Ona tili);\nIngliz tili(B2);\nArab tili(O'qiy olish);\nYapon tili(N3)"
    await call.message.answer_photo(photo_file,caption=msg, reply_markup=main_menu)

@dp.callback_query_handler(text='menu')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/photo.jpg')
    await call.message.answer_photo(photo_file,"To'liq malumot uchun bosing⤵️",reply_markup=categoryMenu)

@dp.callback_query_handler(text='ortga')
async def select_category(call: CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/photo.jpg')
    await call.message.answer_photo(photo_file,"To'liq malumot uchun bosing⤵️",reply_markup=categoryMenu)

@dp.callback_query_handler(text='resume')
async def select_categoty(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer('Skachat qilish uchun bosing⤵️',reply_markup=resume)

    
@dp.callback_query_handler(text='download')
async def select_category(call:CallbackQuery):
    await call.message.delete()  
    pdf_file = InputFile(path_or_bytesio='photo/Otajon.pdf')
    await call.message.answer_document(pdf_file,'Otajon Bozorboyevning resumesi⤵️',reply_markup=main_menu)

@dp.callback_query_handler(text='social')
async def select_category(call:CallbackQuery):
    await call.message.delete()
    photo_file = InputFile(path_or_bytesio='photo/linkedin.jpg')
    await call.message.answer_photo(photo_file,reply_markup=SocialNetworks)