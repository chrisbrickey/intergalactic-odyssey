from src.main import main
from src.odyssey import Odyssey

def test_launch_script_output(mocker, capsys):
    # Arrange
    mocker.patch('builtins.input', side_effect=['engage', '1'])

    # Act
    main()
    captured = capsys.readouterr()

    # Assert
    assert captured.out.startswith("I'm an odyssey!!!\n")

def test_launch_script_creates_odyssey_instance(mocker):
    # Arrange
    Odyssey.clear_instance_count()
    mocker.patch('builtins.input', side_effect=['engage', '1'])

    # Act
    main()

    # Assert
    assert Odyssey.get_instance_count() == 1