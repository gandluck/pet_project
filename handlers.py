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

router = Router()
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()


# Хендлер для начальной команды /start
@router.message(Command('start'))
async def start_handler(msg: Message, state: FSMContext):
    if msg.from_user.id not in db.Data.get_all_ids():
        start_command = msg.text
        referrer_id = str(start_command[7:])
        if str(referrer_id) != "":
            if str(referrer_id) != str(msg.from_user.id):
                db.Data.create_record_user(msg.from_user.id, msg.from_user.username)
                db.Data.create_subscribtion(msg.from_user.id, referrer_id)
                await msg.answer(
                    text=f'You have been successfully subscribed for "{db.Data.get_traider_nickname_by_telegramid(referrer_id)}"')
                await state.set_state(states.UserStates.unconfirmed)
                await msg.answer(text=text.start_text,
                                 reply_markup=kb.start_keyboard)
            else:
                await msg.answer(text='You cannot register with your own link!')
        else:
            await state.set_state(states.UserStates.unconfirmed)
            await msg.answer(text=text.start_text,
                             reply_markup=kb.start_keyboard)
            db.Data.create_record_user(msg.from_user.id, msg.from_user.username)


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
    await state.set_state(states.UserStates.nickname)
    await callback_query.message.answer(
        text='You have successfully accepted the agreement!\nPlease, send your nickname')
    await callback_query.answer()


# Хендлер для прием nickname
@router.message(states.UserStates.nickname)
async def nickname(msg: Message):
    if db.Data.check_nickname(msg.text):
        db.Data.update_data_user_nickname(telegram_id=msg.from_user.id,
                                          nickname=msg.text)
        await msg.answer(
            text=f'Your nickname is: {db.Data.get_nickname(msg.from_user.id)}\nIf you want to change it, just send it again',
            reply_markup=kb.agreed_keyboard)
    else:
        await msg.answer('Your nickname is occupied by another user.\nPlease, send your nickname again!')


# Хендлер для кнопки "Press to enter Binance API"
@router.callback_query(F.data == "api")
async def callback_query_handler(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer(text='Please, send your Binance API', reply_markup=kb.manual_keyboard)
    await state.set_state(states.UserStates.unregistered_with_nickname)
    await callback_query.answer()


# Хендлер для присланного API
@router.message(states.UserStates.unregistered_with_nickname)
async def get_api(msg: Message, state: FSMContext):
    db.Data.update_data_user_api(telegram_id=msg.from_user.id,
                                 api=msg.text)
    await msg.answer(text='Please, send your secret key')
    await state.set_state(states.UserStates.unregistered_with_api)


# Хендлер для присланного secret key и проверки на правильность
@router.message(states.UserStates.unregistered_with_api)
async def get_secret_key(msg: Message, state: FSMContext):
    db.Data.update_data_user_key(telegram_id=msg.from_user.id,
                                 secret_key=msg.text)
    await msg.answer(
        text=f'Your API: {db.Data.get_api(msg.from_user.id)}\nYour secret key: {db.Data.get_secret(msg.from_user.id)}')
    await msg.answer(text="Wait, we're checking your keys")
    if utils.check_api_keys(db.Data.get_api(msg.from_user.id), db.Data.get_secret(msg.from_user.id)):
        await msg.answer(text='Your keys are correct!')
        await state.set_state(states.UserStates.registered)
        await msg.answer(text=text.registration_text, reply_markup=kb.menu_user_keyboard)

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


# Хендлер для книпки "Subscribtion"
@router.callback_query(F.data == "subscribtion")
async def subscribtion(callback_query: types.CallbackQuery):
    nickname_of_traider = db.Data.check_subscribe(callback_query.from_user.id)
    if nickname_of_traider == None:
        await callback_query.message.answer(text='You do not have subscribtion now',
                                            reply_markup=kb.back_to_menu_keyboard)
        await callback_query.answer()
    else:
        await callback_query.message.answer(
            text=f'You have subscribtion for "{db.Data.check_subscribe(callback_query.from_user.id)}"',
            reply_markup=kb.back_to_menu_keyboard)
        await callback_query.answer()


# Хендлер для кнопки "Instructions"
@router.callback_query(F.data == "instructions")
async def instructions(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text='Здесь будут инструкции', reply_markup=kb.back_to_menu_keyboard)
    await callback_query.answer()


# Хендлер для кнопки "Back to menu" для registered
@router.callback_query(F.data == "back_to_menu")
async def menu(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text='Here is the menu', reply_markup=kb.menu_user_keyboard)
    await callback_query.answer()


# Хендлер для кнопки "Become a traider"
@router.callback_query(F.data == "become_trdr")
async def become_tradier(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text=f'Your balance: {db.Data.get_balance(callback_query.from_user.id)}')
    await callback_query.message.answer(
        text='Here is a list of subscription rates:\n1) Первый тариф\n2) Второй тариф\n3) Третий тариф\nВыберите тариф',
        reply_markup=kb.rates_keyboard)
    await callback_query.answer()


# Хендлер для первого тарифа
@router.callback_query(F.data == "rate1")
async def rate1(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer(
        text='Заглушка проверки успешности проведения транзакции.\nТранзакция прошла успешно')
    db.Data.update_data_user_become_traider(callback_query.from_user.id)
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
    db.Data.update_data_user_become_traider(callback_query.from_user.id)
    await callback_query.answer()
    await callback_query.message.answer(text='Here is your menu',
                                        reply_markup=kb.menu_traider_keyboard)


# Хендлер для третьего тарифа
@router.callback_query(F.data == "rate3")
async def rate1(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer(
        text='Заглушка проверки успешности проведения транзакции.\nТранзакция прошла успешно')
    await state.set_state(states.UserStates.traider)
    db.Data.update_data_user_become_traider(callback_query.from_user.id)
    await callback_query.answer()
    await callback_query.message.answer(text='Here is your menu',
                                        reply_markup=kb.menu_traider_keyboard)


# Хендлер для кнопки "Statistics"
@router.callback_query(F.data == "stat")
async def stat(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(
        text=f'Your amount of referralers: {db.Data.get_amount_of_referralers(callback_query.from_user.id)}',
        reply_markup=kb.back_to_menu_tr_keyboard)


# Все хендлеры для взаимодействия с балансом
# Хендлер для кнопки "Balance"
@router.callback_query(F.data == "balance")
@router.callback_query(F.data == "top_up")
async def stat(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()
    balance = db.Data.get_balance(callback_query.from_user.id)
    if db.Data.get_role(callback_query.from_user.id) == 'User':
        await callback_query.message.answer(
            text=f'Your balance: {balance}\nPlease, send how much you want to put on your balance',
            reply_markup=kb.back_to_menu_keyboard)
    else:
        await callback_query.message.answer(
            text=f'Your balance: {balance}\nPlease, send how much you want to put on your balance',
            reply_markup=kb.back_to_menu_tr_keyboard)

    await state.set_state(states.UserStates.balance)


# Хендлер для приема суммы для пополнения баланса
@router.message(states.UserStates.balance)
async def toping_up_balance(msg: Message):
    db.Data.top_up_balance(telegram_id=msg.from_user.id,
                           balance=int(msg.text))
    if db.Data.get_role(msg.from_user.id) == 'User':
        await msg.answer(text=f'Your balance has been sucessfully toped up!\nYour balance: {db.Data.get_balance(msg.from_user.id)}',
                         reply_markup=kb.back_to_menu_keyboard)
    else:
        await msg.answer(text=f'Your balance has been sucessfully toped up!\nYour balance: {db.Data.get_balance(msg.from_user.id)}',
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
    db.Data.update_data_user_mailing(telegram_id=msg.from_user.id,
                                     text=msg.text)
    await msg.answer(text=f'Your text: {msg.text}\nIs text OK?', reply_markup=kb.mailing_keyboard)


# Хендлер для кнопки "No" при подтверждении сообщения для рассылки
@router.callback_query(F.data == "mailing_no")
async def mailing_no(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text='Please, send text for mailing again.')
    await callback_query.answer()


# Хендлер для кнопки "Yes" при подтверждениии сообщения для рассылки
@router.callback_query(F.data == "mailing_yes")
async def mailing_yes(callback_query: types.CallbackQuery):
    for i in db.Data.get_ids_for_mailing(callback_query.from_user.id):
        await bot.send_message(chat_id=i,
                               text=db.Data.get_mailing(callback_query.from_user.id))
    await callback_query.message.answer(text='The mailing was made successfully!',
                                        reply_markup=kb.back_to_menu_tr_keyboard)

    await callback_query.answer()


# Хендлер для кнопки "Settings"
@router.callback_query(F.data == "settings")
async def stat(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(text='Заглушка',
                                        reply_markup=kb.back_to_menu_tr_keyboard)


# Хендлер для кнопки "Create referral link"
@router.callback_query(F.data == "create_ref_link")
async def create_ref_link(callback_query: types.CallbackQuery):
    await callback_query.message.answer(
        text=f'Your referral link is:\nhttps://t.me/{config.BOT_NAME}?start={callback_query.from_user.id}',
        reply_markup=kb.back_to_menu_tr_keyboard)
    await callback_query.answer()


# Хендлре для кнопки "Back to menu" для traider
@router.callback_query(F.data == "back_to_menu_tr")
async def back_to_menu_tr(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(states.UserStates.traider)
    await callback_query.answer()
    await callback_query.message.answer(text="Here is your menu",
                                        reply_markup=kb.menu_traider_keyboard)
