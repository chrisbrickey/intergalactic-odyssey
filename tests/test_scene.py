import pytest
from src.scene import Scene

def test_attributes_on_creation():
  zorba = Scene(
      'Zorba',
      'This planet has two moons.',
      'Cool the Core',
      'Time Travel')
  assert zorba.name == 'Zorba'
  assert zorba.description.startswith('This planet')
  assert zorba.puzzle == 'Cool the Core'
  assert zorba.reward == 'Time Travel'

def test_name_is_non_empty_string():
    with pytest.raises(TypeError):
        Scene(9, '', '', '')
    with pytest.raises(ValueError):
        Scene('', '', '', '')