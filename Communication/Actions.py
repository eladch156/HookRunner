class Action():
    def __init__(self):
        raise NotImplementedError
    @classmethod
    def create(cls, json):
        raise NotImplementedError
    def run(self):
        raise NotImplementedError