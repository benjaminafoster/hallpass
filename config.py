from users import User

class Config:
    def __init__(self):
        pass

    def add_user(self, user:User):
        self.current_user = user
