from src.odyssey import Odyssey

def test_start_game_output(mocker, capsys):
    # Arrange
    mocker.patch('builtins.input', side_effect=['engage'])
    new_odyssey = Odyssey()

    # Act
    new_odyssey.start_game()
    captured = capsys.readouterr()

    # Assert
    assert captured.out.startswith("I'm an odyssey!!!\n")

def test_start_game_prompt_advances_only_with_correct_input(mocker):
    # Arrange
    new_odyssey = Odyssey()
    mock_user_input = mocker.patch('builtins.input', side_effect=['not engage', 'still not engage', 'engage'])
    mock_engage = mocker.patch.object(new_odyssey, 'engage')

    # Act
    new_odyssey.start_game()

    # Assert
    assert mock_user_input.call_count == 3
    mock_engage.assert_called_once()

def test_engage_output(mocker, capsys):
    # Arrange
    new_odyssey = Odyssey()
    mocker.patch('builtins.input', side_effect=['engage'])

    # Act
    new_odyssey.engage()
    captured = capsys.readouterr()

    # Assert
    assert captured.out.endswith("Engaging...\n")