class User:
    def __init__(self, user_id: int, name: str):
        self._id = user_id
        self._name = name 

    @property
    def id(self):
        return self._id

    @property
    def user_id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return f"<User [ID: {self._id}, Név: {self._name}]>"
