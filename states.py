from aiogram.fsm.state import State, StatesGroup


class UserStates(StatesGroup):
    unconfirmed = State()
    unregistered = State()
    unregistered_with_nickname = State()
    unregistered_with_api = State()
    registered = State()
    traider = State()
    mailing = State()
    balance = State()
    nickname = State()
