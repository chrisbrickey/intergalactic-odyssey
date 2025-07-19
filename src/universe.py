from src.scene import Scene

class Universe:
    def __init__(self):
        self.scenes = self.create_scenes()
        self.galactic_survey = [[i, scene.name] for i, scene in enumerate(self.scenes)]

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

        # TODO: Randomize order; Add more scenes
        return [galaxy1, galaxy2]