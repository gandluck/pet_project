from aiogram.fsm.state import State, StatesGroup
class UserStates(StatesGroup):
    unconfirmed = State()
    unregistered = State()
    unregistered_with_nickname = State()
    unregistered_with_api = State()
    registered = State()
    traider = State()
    mailing = State()

class User:
    def __init__(self, api=None, secret_key=None, nickname=None, telegram_id=None, text_for_mailing=None, username=None, role=None):
        self.api = api
        self.secret_key = secret_key
        self.nickname = nickname
        self.telegram_id = telegram_id
        self.text_for_mailing = text_for_mailing
        self.username = username
        self.role = role