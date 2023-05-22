from aiogram.fsm.state import State, StatesGroup
class UserStates(StatesGroup):
    unconfirmed = State()
    unregistered = State()
    unregistered_with_api = State()
    registered = State()

class User:
    def __init__(self, api=None, secret_key=None):
        self.api = api
        self.secret_key = secret_key

