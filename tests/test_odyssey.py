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

def test_odyssey_attributes_on_creation(new_odyssey):
    assert new_odyssey.universe is None
    assert new_odyssey.game_plan is None

def test_run_game_prompt_advances_only_with_correct_user_input(new_odyssey, mocker):
    # Arrange
    mock_user_input = mocker.patch('builtins.input', side_effect=['not engage', 'still not engage', 'engage', '1'])
    mock_retrieve_universe = mocker.patch.object(new_odyssey, 'retrieve_universe')
    mocker.patch.object(new_odyssey, 'develop_game_plan')

    # Act
    new_odyssey.run_game()

    # Assert
    assert mock_user_input.call_count == 4
    mock_retrieve_universe.assert_called_once()

def test_run_game_retrieves_universe(new_odyssey, mocker):
    # Arrange
    mocker.patch('builtins.input', side_effect=['engage', '1'])

    # Act
    new_odyssey.run_game()

    # Assert
    assert new_odyssey.universe is not None
    assert isinstance(new_odyssey.universe, Universe)

# TODO: 1) improve test by testing that starting index is first
#       2) add test that first index is selected as starting index in game plan
def test_run_game_develops_game_plan(new_odyssey, mocker):
    # Arrange
    mocker.patch('builtins.input', side_effect=['engage', '1'])

    # Act
    new_odyssey.run_game()
    updated_game_plan = new_odyssey.game_plan

    # Assert
    assert updated_game_plan is not None
    assert len(set(updated_game_plan)) == len(updated_game_plan)
    assert len(updated_game_plan) == len(new_odyssey.universe.scenes)

def test_retrieve_universe_output(new_odyssey, capsys):
    # Act
    new_odyssey.retrieve_universe()
    captured = capsys.readouterr()

    # Assert
    assert captured.out.endswith("what you've learned.\n")

def test_select_starting_index_output_user_input_valid(new_odyssey, mocker, capsys):
    # Arrange
    survey = Universe().galactic_survey
    user_input = str(len(survey)) # user selects highest number displayed
    mocker.patch('builtins.input', side_effect=[user_input])

    # Act
    result = new_odyssey.select_starting_index(survey)
    captured = capsys.readouterr()

    # Assert
    assert captured.out.endswith(f"You're headed to Galaxy {user_input}: {survey[result][1]}.\n")
    assert type(result) == int
    assert result in range (0, len(survey))

def test_select_starting_index_output_user_input_invalid(new_odyssey, mocker, capsys):
    # Arrange
    survey = Universe().galactic_survey
    user_input = 'Galaxy 1' # cannot be parsed to int
    mocker.patch('builtins.input', side_effect=[user_input])

    # Act
    result = new_odyssey.select_starting_index(survey)
    captured = capsys.readouterr()

    # Assert
    assert captured.out.endswith(f"You're headed to Galaxy {result + 1}: {survey[result][1]}.\n")
    assert type(result) == int
    assert result in range (0, len(survey))


def test_select_starting_index_output_with_user_input_out_of_range(new_odyssey, mocker, capsys):
    # Arrange
    survey = Universe().galactic_survey
    user_input = len(survey) + 1
    mocker.patch('builtins.input', side_effect=[user_input])

    # Act
    result = new_odyssey.select_starting_index(survey)
    captured = capsys.readouterr()

    # Assert
    assert captured.out.endswith(f"You're headed to Galaxy {result + 1}: {survey[result][1]}.\n")
    assert type(result) == int
    assert result in range(0, len(survey))