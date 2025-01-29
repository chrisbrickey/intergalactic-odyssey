class Scene:
    def __init__(self, name, description, puzzle, reward):
        self.validate_name(name)
        self.name = name

        self.description = description
        self.puzzle = puzzle
        self.reward = reward

    def validate_name(self, name):
        if not isinstance(name, str):
            raise TypeError('Name must be a string.')
        if len(name) < 1:
            raise ValueError('Name cannot be empty string.')