from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove

key_and_api_b1 = InlineKeyboardButton(text="Enter Binance API and secret key", callback_data="key_and_api")
manual_b2 = InlineKeyboardButton(text="How to get API",
                                 url='https://www.binance.com/en-BH/support/faq/how-to-create-api-360002502072')
start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[key_and_api_b1],
                     [manual_b2]]
)

agreement_b1 = InlineKeyboardButton(text="Yes, I agree", callback_data="agreement")
agreement_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[agreement_b1]]
)

agreed_b1 = InlineKeyboardButton(text="Press to enter Binance API", callback_data="api")
agreed_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[agreed_b1]]
)

manual_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[manual_b2]]
)

list_of_traders_b1 = InlineKeyboardButton(text="List of traders", callback_data="list_of_traders")
top_up_b2 = InlineKeyboardButton(text="Top up account balance", callback_data="top_up")
instructions_b3 = InlineKeyboardButton(text="Instructions", callback_data="instructions")
menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[list_of_traders_b1],
                     [top_up_b2],
                     [instructions_b3]]
)
back_to_menu_b1 = InlineKeyboardButton(text="Back to menu", callback_data="back_to_menu")
back_to_menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[back_to_menu_b1]])
