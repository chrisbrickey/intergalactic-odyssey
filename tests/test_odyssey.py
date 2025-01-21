from odyssey import Odyssey

def test_launch_script(capsys):
    with open("../odyssey.py") as file:
        exec(file.read())

    captured = capsys.readouterr()
    assert captured.out == "I'm an odyssey!!!\n"


def test_odyssey_introduction(capsys):
    new_odyssey = Odyssey()
    captured = capsys.readouterr()
    assert captured.out == "I'm an odyssey!!!\n"