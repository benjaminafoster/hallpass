class User:
    def __init__(self, username:str, password:bytes):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'User: {self.username}'
