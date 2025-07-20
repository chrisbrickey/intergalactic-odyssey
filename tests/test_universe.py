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

def test_scenes_attribute_on_creation(new_universe):
  assert hasattr(new_universe, 'scenes')
  scenes = new_universe.scenes
  assert len(scenes) > 0
  assert all(isinstance(element, Scene) for element in scenes)

# def test_survey_attribute_on_creation(new_universe):
#   assert hasattr(new_universe, 'galactic_survey')
#   survey = new_universe.galactic_survey
#   assert len(survey) == len(new_universe.scenes)
#   assert type(survey[0][0]) == int
#   assert type(survey[0][1]) == str