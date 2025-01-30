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

    def construct_universe(self):
        new_universe = Universe()

        # TODO: Add more complex logic for reducing count for large universes.
        # e.g. target = some proportion of size of universe, unless universe is small
        # In future versions, the game could prompt the user for easy, medium, or high difficulty. This changes the number or proportion of galaxies that must be visited.
        target_galaxy_count = len(new_universe.scenes)
        intro_message = f"Your mission is to explore {target_galaxy_count} galaxies, accumulate new technolgies, and return home safely to share what you've learned."
        print(intro_message)

        #   Game displays Universe/GalacticSurvey to user as numbers (index + 1) with name of galaxy.
        # 	User enters number (Game validates that it is an integer within range of GalacticSurvey array.)

    @classmethod
    def get_instance_count(cls):
        return cls._instance_count

    @classmethod
    def clear_instance_count(cls):
        cls._instance_count = 0