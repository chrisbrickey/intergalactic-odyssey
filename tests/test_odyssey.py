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

@pytest.fixture(autouse=True)
def universe_fixture():
   # Setup
   universe_fixture = Universe()

   yield universe_fixture

   # Teardown
   universe_fixture.value = None

def test_odyssey_attributes_on_creation(new_odyssey):
    assert new_odyssey.universe is None

# TODO: Adapt test to focus only on engage method to prevent adding to mock_user_input as game expands
def test_run_game_prompt_advances_only_with_correct_user_input(new_odyssey, mocker):
    # Arrange
    mock_user_input = mocker.patch('builtins.input', side_effect=['not engage', 'still not engage', 'engage', '1'])
    mock_retrieve_universe = mocker.patch.object(new_odyssey, 'retrieve_universe')

    # Act
    new_odyssey.run_game()

    # Assert
    assert mock_user_input.call_count == 4
    mock_retrieve_universe.assert_called_once()

def test_run_game_triggers_universe_retrieval(new_odyssey, mocker):
    # Arrange
    mocker.patch('builtins.input', side_effect=['engage', '1'])

    # Act
    new_odyssey.run_game()

    # Assert
    assert isinstance(new_odyssey.universe, Universe)

def test_retrieve_universe_output(new_odyssey, capsys):
    # Act
    new_odyssey.retrieve_universe()
    captured = capsys.readouterr()

    # Assert
    assert captured.out.startswith("\n\nYour mission is to explore")
    assert captured.out.endswith("return home safely to share what you've learned.\n")

def test_select_starting_index_output_user_input_valid(new_odyssey, universe_fixture, mocker, capsys):
    # Arrange
    survey_fixture = universe_fixture.galactic_survey
    user_input = str(len(survey_fixture)) # user selects highest number displayed
    mocker.patch('builtins.input', side_effect=[user_input])
    mocker.patch.object(new_odyssey, 'universe', universe_fixture)

    # Act
    result = new_odyssey.select_starting_index()
    captured = capsys.readouterr()

    # Assert
    assert captured.out.endswith(f"You're headed to Galaxy {user_input}: {survey_fixture[result][1]}.\n")
    assert result == int(user_input) - 1

def test_select_starting_index_output_user_input_invalid(new_odyssey, universe_fixture, mocker, capsys):
    # Arrange
    survey_fixture = universe_fixture.galactic_survey
    user_input = 'Galaxy 1' # cannot be parsed to int
    mocker.patch('builtins.input', side_effect=[user_input])
    mocker.patch.object(new_odyssey, 'universe', universe_fixture)

    # Act
    result = new_odyssey.select_starting_index()
    captured = capsys.readouterr()

    # Assert
    assert captured.out.endswith(f"You're headed to Galaxy {result + 1}: {survey_fixture[result][1]}.\n")
    assert result == 0


def test_select_starting_index_output_with_user_input_out_of_range(new_odyssey, universe_fixture,mocker, capsys):
    # Arrange
    survey_fixture = universe_fixture.galactic_survey
    user_input = len(survey_fixture) + 1
    mocker.patch('builtins.input', side_effect=[user_input])
    mocker.patch.object(new_odyssey, 'universe', universe_fixture)

    # Act
    result = new_odyssey.select_starting_index()
    captured = capsys.readouterr()

    # Assert
    assert captured.out.endswith(f"You're headed to Galaxy {result + 1}: {survey_fixture[result][1]}.\n")
    assert result == 0