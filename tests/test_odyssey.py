import pytest
from src.odyssey import Odyssey
from src.universe import Universe

@pytest.fixture(autouse=True)
def new_odyssey():
   # Setup
   new_odyssey = Odyssey()

   yield new_odyssey

   # Teardown
   new_odyssey.value = None

# TODO: Adapt test to focus only on engage method to prevent adding to mock_user_input as game expands
def test_run_game_prompt_advances_only_with_correct_user_input(new_odyssey, mocker):
    # Arrange
    mock_user_input = mocker.patch('builtins.input', side_effect=['not engage', 'still not engage', 'engage'])
    mock_retrieve_universe = mocker.patch.object(new_odyssey, 'retrieve_universe')

    # Act
    new_odyssey.run_game()

    # Assert
    assert mock_user_input.call_count == 3
    mock_retrieve_universe.assert_called_once()

def test_engage_output(new_odyssey, mocker, capsys):
    # Arrange
    mocker.patch('builtins.input', side_effect=['engage'])

    # Act
    new_odyssey.engage()
    captured = capsys.readouterr()

    # Assert
    assert captured.out.startswith("I'm an odyssey!!!\n")

def test_retrieve_universe_output(new_odyssey, capsys):
    # Act
    new_odyssey.retrieve_universe()
    captured = capsys.readouterr()

    # Assert
    assert captured.out.endswith("what you've learned.\n")

def test_select_starting_index_output(new_odyssey, capsys):
    # Arrange
    survey = Universe().galactic_survey

    # Act
    result = new_odyssey.select_starting_index(survey)
    captured = capsys.readouterr()

    # Assert
    assert captured.out.endswith("You're headed to Galaxy 1.\n")
    assert type(result) == int
    assert result in range (0, len(survey))