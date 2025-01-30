from src.odyssey import Odyssey

def test_start_game_output(mocker, capsys):
    # Arrange
    mocker.patch('builtins.input', side_effect=['engage'])
    new_odyssey = Odyssey()

    # Act
    new_odyssey.run_game()
    captured = capsys.readouterr()

    # Assert
    assert captured.out.startswith("I'm an odyssey!!!\n")

def test_run_game_advances_only_with_correct_user_input(mocker):
    # Arrange
    new_odyssey = Odyssey()
    mock_user_input = mocker.patch('builtins.input', side_effect=['not engage', 'still not engage', 'engage'])
    mock_construct_universe = mocker.patch.object(new_odyssey, 'construct_universe')

    # Act
    new_odyssey.run_game()

    # Assert
    assert mock_user_input.call_count == 3
    mock_construct_universe.assert_called_once()

def test_construct_universe_output(mocker, capsys):
    # Arrange
    new_odyssey = Odyssey()

    # Act
    new_odyssey.construct_universe()
    captured = capsys.readouterr()

    # Assert
    assert captured.out.endswith("what you've learned.\n")