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

  #     assert type(element) == list
  #     assert type(element[0]) == int
  #     assert type(element[1]) == str
  #     assert survey[i][0] == i
  #     assert survey[i][1] == scenes[i].name

def test_name_is_non_empty_string():
    with pytest.raises(TypeError):
        Scene(9, '', '', '')
    with pytest.raises(ValueError):
        Scene('', '', '', '')