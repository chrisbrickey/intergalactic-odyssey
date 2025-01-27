from odyssey import Odyssey

def test_odyssey_start_game(capsys):
    new_odyssey = Odyssey()
    new_odyssey.start_game()
    captured = capsys.readouterr()
    assert captured.out == "I'm an odyssey!!!\n"