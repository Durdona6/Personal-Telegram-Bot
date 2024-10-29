from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.bio import categoryMenu



SocialNetworks = InlineKeyboardMarkup(
    inline_keyboard=[ 
        [
            InlineKeyboardButton(text='Linkedin', url='https://www.linkedin.com/in/otajonbozorboyev/' ),
            InlineKeyboardButton(text='Leetcode', url='https://leetcode.com/otajonbozorboyev571/' )
        ],
        [
            InlineKeyboardButton(text='Git Hub', url='https://github.com/otajonbozorboyev' ),
            InlineKeyboardButton(text='T.me', url='https://t.me/otajonbozorboyev' )
        ],
        [
            InlineKeyboardButton(text='🔙ortga', callback_data="ortga", reply_markup=categoryMenu)
        ],
    ]
)

main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔝Asosiy menu", callback_data='menu')
        ],
    ]
)


resume = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='⬇️Download', callback_data='download')
        ],
    ]
)