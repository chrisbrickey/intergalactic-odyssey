from src.scene import Scene

class Universe:
    def __init__(self):
        # TODO: Randomize the order before assigning to attribute
        # TODO: Use input parameter (e.g. galaxy_count) to determine
        # TODO: Determine if and where the input galaxy_count should be validated to prevent game from trying to play more galaxies than exist.
        self.scenes = self.create_scenes()

    def create_scenes(self):
        # TODO: Extract to config/scenes.yaml; config = yaml.safe_load(open("config/scenes.yaml"))
        name1 = 'The Enigmatic Medium'
        description1 = 'This galaxy...'
        puzzle1 = 'Star Birth'
        reward1 = 'Nebula Drive'
        galaxy1 = Scene(name1, description1, puzzle1, reward1)

        name2 = 'The Frozen Galaxy'
        description2 = 'This galaxy...'
        puzzle2 = 'The Crystallized Labrynth'
        reward2 = 'Scorching Saber'
        galaxy2 = Scene(name2, description2, puzzle2, reward2)

        # TODO: Add more scenes
        return [galaxy1, galaxy2]