from src.universe import Universe
from src.scene import Scene

def test_attributes_on_creation():
  universe1 = Universe()
  assert hasattr(universe1, 'scenes')

  scenes = universe1.scenes
  assert type(scenes) == list
  assert len(scenes) > 0
  for element in scenes:
      assert type(element) == Scene