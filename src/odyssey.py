from src.universe import Universe

class Odyssey():
    _instance_count = 0

    def __init__(self):
        Odyssey._instance_count += 1

    def run_game(self):
        self.engage()
        self.construct_universe()

    def engage(self):
        print("I'm an odyssey!!!")

        command = ''
        while command != 'engage':
            command = input("Type 'engage' to begin: ")

        print("Engaging...")

    def construct_universe(self):
        Universe()

    @classmethod
    def get_instance_count(cls):
        return cls._instance_count

    @classmethod
    def clear_instance_count(cls):
        cls._instance_count = 0