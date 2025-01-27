class Odyssey():
    _instance_count = 0

    def __init__(self):
        Odyssey._instance_count += 1

    def start_game(self):
        print("I'm an odyssey!!!")

    @classmethod
    def get_instance_count(cls):
        return cls._instance_count

    @classmethod
    def clear_instance_count(cls):
        cls._instance_count = 0