from aiogram import types, F, Router, Dispatcher, Bot
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile

import text
import kb
import states
import db
import utils
import config
from states import user

router = Router()
bot = Bot(token=config.BOT_TOKEN)


# Хендлер для начальной команды /start
@router.message(Command("start"))
async def start_handler(msg: Message, state: FSMContext):
    await state.set_state(states.UserStates.unconfirmed)
    await msg.answer(text=text.start_text,
                     reply_markup=kb.start_keyboard)
    user.telegram_id = msg.from_user.id
    user.username = msg.from_user.username
    db.Data.create_record_user()

# Хендлер для кнопки "Enter Binance API and secret key"
@router.callback_query(F.data == "key_and_api")
async def agreement(callback_query: types.CallbackQuery):
    await callback_query.message.answer(
        text='Please read our user agreement and accept it',
        reply_markup=kb.agreement_keyboard)
    await callback_query.answer()
    agreement1 = FSInputFile("agreement.docx")
    await callback_query.message.answer_document(document=agreement1)


# Хендлер для кнопки "Yes, i agree"(пользовательское соглашение)
@router.callback_query(F.data == "agreement")
async def agreed(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(states.UserStates.unregistered)
    await callback_query.message.answer(
        text='You have successfully accepted the agreement!\nPlease, send your nickname')


# Хендлер для прием nickname
@router.message(states.UserStates.unregistered)
async def nickname(msg: Message, state: FSMContext):
    if db.Data.check_nickname(msg.text):
        user.nickname = msg.text
        await state.set_state(states.UserStates.unregistered_with_nickname)
        await msg.answer(text=f'Your nickname is: {user.nickname}',
                         reply_markup=kb.agreed_keyboard)
    else:
        await msg.answer('Your nickname is occupied by another user.\nPlease, send your nickname again!')


# Хендлер для кнопки "Press to enter Binance API"
@router.callback_query(F.data == "api")
async def callback_query_handler(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text='Please, send your Binance API', reply_markup=kb.manual_keyboard)
    await callback_query.answer()


# Хендлер для присланного API
@router.message(states.UserStates.unregistered_with_nickname)
async def get_api(msg: Message, state: FSMContext):
    user.api = msg.text
    await msg.answer(text='Please, send your secret key')
    await state.set_state(states.UserStates.unregistered_with_api)


# Хендлер для присланного secret key и проверки на правильность
@router.message(states.UserStates.unregistered_with_api)
async def get_secret_key(msg: Message, state: FSMContext):
    user.secret_key = msg.text
    await msg.answer(text=f'Your API: {user.api}\nYour secret key: {user.secret_key}')
    await msg.answer(text="Wait, we're checking your keys")
    if utils.check_api_keys(user.api, user.secret_key):
        await msg.answer(text='Your keys are correct!')
        await state.set_state(states.UserStates.registered)
        await msg.answer(text=text.registration_text, reply_markup=kb.menu_user_keyboard)
        db.Data.update_data_user_nickname_api_key()

    else:
        await state.set_state(states.UserStates.unregistered)
        await msg.answer(text='Your keys are wrong, please, send your API again', reply_markup=kb.agreed_keyboard)


# Хендлер для кнопки "List of traiders"
@router.callback_query(F.data == "list_of_traders")
async def list_of_traders(callback_query: types.CallbackQuery):
    traders = db.Data.get_traiders()
    result_text = []
    for i in range(len(traders)):
        x = f'{i + 1}) {traders[i]}\n'
        result_text.append(x)

    await callback_query.message.answer(text=f'Here is the list of traders:\n{"".join(result_text)}',
                                        reply_markup=kb.back_to_menu_keyboard)
    await callback_query.answer()


# Хендлер для кнопки "Top up balance"
@router.callback_query(F.data == "top_up")
async def top_up_balance(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text='Здесь будет пополнение аккаунта', reply_markup=kb.back_to_menu_keyboard)
    await callback_query.answer()


# Хендлер для кнопки "Instructions"
@router.callback_query(F.data == "instructions")
async def instructions(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text='Здесь будут инструкции', reply_markup=kb.back_to_menu_keyboard)
    await callback_query.answer()


# Хендлер для кнопки "Back to menu" для registered
@router.callback_query(states.UserStates.registered, F.data == "back_to_menu")
async def menu(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text='Here is the menu', reply_markup=kb.menu_user_keyboard)
    await callback_query.answer()


# Хендлер для кнопки "Become a traider"
@router.callback_query(F.data == "become_trdr")
async def become_tradier(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text='Your balance: Заглушка')
    await callback_query.message.answer(
        text='Here is a list of subscription rates:\n1) Первый тариф\n2) Второй тариф\n3) Третий тариф\nВыберите тариф',
        reply_markup=kb.rates_keyboard)
    await callback_query.answer()


# Хендлер для первого тарифа
@router.callback_query(F.data == "rate1")
async def rate1(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer(
        text='Заглушка проверки успешности проведения транзакции.\nТранзакция прошла успешно')
    await state.set_state(states.UserStates.traider)
    await callback_query.answer()
    await callback_query.message.answer(text='Here is your menu',
                                        reply_markup=kb.menu_traider_keyboard)


# Хендлер для второго тарифа
@router.callback_query(F.data == "rate2")
async def rate1(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer(
        text='Заглушка проверки успешности проведения транзакции.\nТранзакция прошла успешно')
    await state.set_state(states.UserStates.traider)
    await callback_query.answer()
    await callback_query.message.answer(text='Here is your menu',
                                        reply_markup=kb.menu_traider_keyboard)


# Хендлер для третьего тарифа
@router.callback_query(F.data == "rate3")
async def rate1(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer(
        text='Заглушка проверки успешности проведения транзакции.\nТранзакция прошла успешно')
    await state.set_state(states.UserStates.traider)
    user.role = 'Traider'
    await callback_query.answer()
    await callback_query.message.answer(text='Here is your menu',
                                        reply_markup=kb.menu_traider_keyboard)


# Хендлер для кнопки "Statistics"
@router.callback_query(F.data == "stat")
async def stat(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(text='Заглушка',
                                        reply_markup=kb.back_to_menu_tr_keyboard)


# Хендлер для кнопки "Balance"
@router.callback_query(F.data == "balance")
async def stat(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(text='Заглушка',
                                        reply_markup=kb.back_to_menu_tr_keyboard)


# Хендлер для кнопки "Mailing"
@router.callback_query(F.data == "mailing")
async def stat(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await state.set_state(states.UserStates.mailing)
    await callback_query.message.answer(text='Please, send your message for mailing',
                                        reply_markup=kb.back_to_menu_tr_keyboard)


# Хендлер для сообщения для рассылки
@router.message(states.UserStates.mailing)
async def mailing(msg: Message):
    user.text_for_mailing = msg.text
    await msg.answer(text=f'Your text: {user.text_for_mailing}\nIs text OK?', reply_markup=kb.mailing_keyboard)


# Хендлер для кнопки "Settings"
@router.callback_query(F.data == "settings")
async def stat(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(text='Заглушка',
                                        reply_markup=kb.back_to_menu_tr_keyboard)


# Хендлре для кнопки "Back to menu" для traider
@router.callback_query(F.data == "back_to_menu_tr")
async def back_to_menu_tr(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(states.UserStates.traider)
    await callback_query.answer()
    await callback_query.message.answer(text="Here is your menu",
                                        reply_markup=kb.menu_traider_keyboard)


# Хендлер для кнопки "No" при подтверждении сообщения для рассылки
@router.callback_query(F.data == "mailing_no")
async def mailing_no(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text='Please, send text for mailing again.')
    await callback_query.answer()


# Хендлер для кнопки "Yes" при подтверждениии сообщения для рассылки
@router.callback_query(F.data == "mailing_yes")
async def mailing_yes(callback_query: types.CallbackQuery):
    # lst = [827694335, 1043075099]
    # for i in lst:
    #     await bot.send_message(chat_id=i,
    #                            text=user.text_for_mailing)
    for i in db.Data.get_ids_for_mailing():
        await bot.send_message(chat_id=i,
                               text=user.text_for_mailing)
    await callback_query.message.answer(text='The mailing was made successfully!',
                                        reply_markup=kb.back_to_menu_tr_keyboard)

    await callback_query.answer()
