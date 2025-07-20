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
        command = ''
        while command != 'engage':
            command = input("Type 'engage' to begin: ")

    def retrieve_universe(self):
        new_universe = Universe()

        # TODO on target_galaxy_count: As the possible size of a universe grows, add logic to control the number of galaxies that the user must explore.
        # e.g. target = proportion of size of universe (unless universe is small)

        # TODO (future development): Prompt user for difficulty level (easy, medium, high).
        #  This changes the number (or proportion) of galaxies that must be visited.

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

        next_scene_index = survey[0][0]

        # Watch out for off-by-one. User is working with figures that represent index + 1.
        user_selection = input("Enter the number of the galaxy you wish to explore first:  ")
        minimum = survey[0][0] + 1
        maximum = survey[-1][0] + 1
        if self.validate_input_text_to_int(user_selection, minimum, maximum):
            next_scene_index = int(user_selection) - 1
        else:
            print("\nYour entry is not valid so your itinerary has been selected for you.")

        next_scene_name = survey[next_scene_index][1]
        print(f"\nBuckle up! You're headed to Galaxy {next_scene_index + 1}: {next_scene_name}.")

        return next_scene_index

    @staticmethod
    def validate_input_text_to_int(input_string, min, max):
        is_valid = False

        try:
            input_int = int(input_string)
            if input_int in range(min, max + 1):
                is_valid = True
        except ValueError:
            pass

        return is_valid

    @classmethod
    def get_instance_count(cls):
        return cls._instance_count

    @classmethod
    def clear_instance_count(cls):
        cls._instance_count = 0