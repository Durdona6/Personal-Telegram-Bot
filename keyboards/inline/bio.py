from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='✍️Bio', callback_data="bio"),
            InlineKeyboardButton(text='📝Resume', callback_data="resume")
        ],
        [
            InlineKeyboardButton(text='🌍Social Networks', callback_data="social"),
            InlineKeyboardButton(text="📞Murojat uchun", callback_data='murojat', url="https://t.me/obozorboyev_bot")
        ],      
    ]
)
