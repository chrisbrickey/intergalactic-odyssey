from src.universe import Universe

class Odyssey():
    _instance_count = 0

    def __init__(self):
        Odyssey._instance_count += 1

    def run_game(self):
        self.engage()
        the_universe = self.retrieve_universe()
        galactic_survey = the_universe.galactic_survey
        starting_scene_index = self.select_starting_index(galactic_survey)

    def engage(self):
        print("I'm an odyssey!!!")

        command = ''
        while command != 'engage':
            command = input("Type 'engage' to begin: ")

    def retrieve_universe(self):
        new_universe = Universe()

        # TODO on target_galaxy_count: As the possible size of a universe grows, add logic to control the number of galaxies that the user must explore.
        # e.g. target = proportion of size of universe (unless universe is small)
        target_galaxy_count = len(new_universe.scenes)
        intro_message = f"\n\nYour mission is to explore {target_galaxy_count} galaxies, accumulate new technolgies, and return home safely to share what you've learned."
        print(intro_message)

        return new_universe

    def select_starting_index(self, survey):
        print("\n\nThe most recent galactic survey uncovered the following galaxies.\n")
        for index, name in survey:
            print(f"Galaxy {(index + 1)}: {name}")
            # Galaxy 1: <name>
            # Galaxy 2: <name>

        # TODO: Allow user to choose starting point; For now default to first galaxy
        next_scene_index = survey[0][0]
        print(f"\n\nBuckle up! You're headed to Galaxy {next_scene_index + 1}.")

        return next_scene_index

    @classmethod
    def get_instance_count(cls):
        return cls._instance_count

    @classmethod
    def clear_instance_count(cls):
        cls._instance_count = 0