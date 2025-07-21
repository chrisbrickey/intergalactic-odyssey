# Intergalactic Odyssey
Intergalactic Odyssey is command line game. 
The user explores multiple galaxies, where they encounter issues that require problem-solving to survive and win.

I created this game to brush up on Python. 
I am using test-driven development and experimenting with AI agents to write tests.

## To run the game
* Activate environment
* From top-level directory: `python3 src/main.py`

## To run the test suite
* `pytest`

If you receive ModuleNotFoundError, confirm that the directory is included in your python path:
`export PYTHONPATH=$PYTHONPATH:$PWD`

## Technology & Dependencies
* Python 3.13.0
* Pytest 8.3.4
* Pytest-mock 3.14.0