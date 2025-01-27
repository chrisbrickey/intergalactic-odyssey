from main import main
from odyssey import Odyssey

def test_launch_script_output(capsys):
    main()

    # Alternative way to launch a script in pytest:
    # with open("../main.py") as file:
    #     exec(file.read())

    captured = capsys.readouterr()
    assert captured.out == "I'm an odyssey!!!\n"

def test_launch_script_creates_odyssey_instance():
    Odyssey.clear_instance_count()
    main()
    assert Odyssey.get_instance_count() == 1