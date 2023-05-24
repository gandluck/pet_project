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

become_trdr = InlineKeyboardButton(text="Become a traider", callback_data="become_trdr")
list_of_traders_b1 = InlineKeyboardButton(text="List of traders", callback_data="list_of_traders")
top_up_b2 = InlineKeyboardButton(text="Top up account balance", callback_data="top_up")
instructions_b3 = InlineKeyboardButton(text="Instructions", callback_data="instructions")

menu_user_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[list_of_traders_b1],
                     [top_up_b2],
                     [become_trdr],
                     [instructions_b3]]
)
back_to_menu_b1 = InlineKeyboardButton(text="Back to menu", callback_data="back_to_menu")

back_to_menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[back_to_menu_b1]])

rate1_b = InlineKeyboardButton(text='Тариф 1', callback_data='rate1')
rate2_b = InlineKeyboardButton(text='Тариф 2', callback_data='rate2')
rate3_b = InlineKeyboardButton(text='Тариф 3', callback_data='rate3')

rates_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [rate1_b],
        [rate2_b],
        [rate3_b],
        [top_up_b2]
    ]
)

stat = InlineKeyboardButton(text='Statistics', callback_data='stat')
# balance = InlineKeyboardButton(text='Balance', callback_data='balance')
mailing = InlineKeyboardButton(text='Mailing', callback_data='mailing')
settings = InlineKeyboardButton(text='Settings', callback_data='settings')

menu_traider_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [stat],
        [top_up_b2],
        [mailing],
        [settings]]
)

back_to_menu_b2 = InlineKeyboardButton(text="Back to menu", callback_data="back_to_menu_tr")

back_to_menu_tr_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[back_to_menu_b2]])

mailing_b1 = InlineKeyboardButton(text='Yes', callback_data='mailing_yes')
mailing_b2 = InlineKeyboardButton(text="No, send again", callback_data='mailing_no')

mailing_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [mailing_b1],
        [mailing_b2],
        [back_to_menu_b2]
    ]
)

balance_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [mailing_b1],
        [mailing_b2],
        [back_to_menu_b2]
    ]
)