import pytest
from src.universe import Universe
from src.scene import Scene

@pytest.fixture(autouse=True)
def new_universe():
   # Setup
   new_universe = Universe()

   yield new_universe

   # Teardown
   new_universe.value = None

def test_attributes_on_creation(new_universe):
  assert hasattr(new_universe, 'scenes')
  assert hasattr(new_universe, 'galactic_survey')
  assert type(new_universe.scenes) == list
  assert type(new_universe.galactic_survey) == list

def test_create_scenes(new_universe):
  scenes = new_universe.create_scenes()
  assert type(scenes) == list
  assert len(scenes) > 0
  for element in scenes:
      assert type(element) == Scene

def test_create_galactic_survey(new_universe):
  # Arrange
  scenes = new_universe.scenes

  # Act
  survey = new_universe.create_galactic_survey()

  # Validate structure [[0, scene_name0], [1, scene_name1]]
  assert type(survey) == list
  assert len(survey) == len(new_universe.scenes)

  for i, element in enumerate(survey):
    assert type(element) == list
    assert type(element[0]) == int
    assert type(element[1]) == str
    assert survey[i][0] == i
    assert survey[i][1] == scenes[i].name