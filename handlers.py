from aiogram import types, F, Router, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile

import text
import kb
import states
import db
import utils

user = states.User()
router = Router()


# Хендлер для начальной команды /start
@router.message(Command("start"))
async def start_handler(msg: Message, state: FSMContext):
    await state.set_state(states.UserStates.unconfirmed)
    await msg.answer(text=text.start_text,
                     reply_markup=kb.start_keyboard)


# Хендлер для начала регистрации
@router.callback_query(F.data == "key_and_api")
async def agreement(callback_query: types.CallbackQuery):
    await callback_query.message.answer(
        text='Please read our user agreement and accept it',
        reply_markup=kb.agreement_keyboard)
    await callback_query.answer()
    agreement1 = FSInputFile("agreement.docx")
    await callback_query.message.answer_document(document=agreement1)


# Хендлер для согласия с пользовательским соглашением
@router.callback_query(F.data == "agreement")
async def agreed(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(states.UserStates.unregistered)
    await callback_query.message.answer(text='You have successfully accepted the agreement!',
                                        reply_markup=kb.agreed_keyboard)


# Хендлер для начала ввода API
@router.callback_query(F.data == "api")
async def callback_query_handler(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text='Please, send your Binance API', reply_markup=kb.manual_keyboard)
    await callback_query.answer()


# Хендлер для присланного API
@router.message(states.UserStates.unregistered)
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
        await msg.answer(text=text.registration_text, reply_markup=kb.menu_keyboard)
    else:
        await state.set_state(states.UserStates.unregistered)
        await msg.answer(text='Your keys are wrong, please, send your API again', reply_markup=kb.agreed_keyboard)


# Хендлер для списка трейдеров
@router.callback_query(F.data == "list_of_traders")
async def list_of_traders(callback_query: types.CallbackQuery):
    traders = db.Data.get_traiders()
    result_text = []
    for i in range(len(traders)):
        x = f'{i + 1}) {traders[i]}\n'
        result_text.append(x)

    await callback_query.message.answer(text=f'Here i the list of traders:\n{"".join(result_text)}',
                                        reply_markup=kb.back_to_menu_keyboard)
    await callback_query.answer()


# Хендлер для пополнения баланса
@router.callback_query(F.data == "top_up")
async def top_up_balance(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text='Здесь будет пополнение аккаунта', reply_markup=kb.back_to_menu_keyboard)
    await callback_query.answer()


# Хендлер для инструкций
@router.callback_query(F.data == "instructions")
async def instructions(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text='Здесь будут инструкции', reply_markup=kb.back_to_menu_keyboard)
    await callback_query.answer()


# Хендлер для кнопки "Back to menu"
@router.callback_query(F.data == "back_to_menu")
async def menu(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text='Here is the menu', reply_markup=kb.menu_keyboard)
    await callback_query.answer()
