import pytest
from src.universe import Universe
from src.scene import Scene


@pytest.fixture(autouse=True)
def new_universe():
    # Setup
    new_universe = Universe()

    yield new_universe

    # Teardown
    new_universe.value = None


def test_attributes_on_creation(new_universe):
    # .scenes
    assert hasattr(new_universe, 'scenes')
    scenes = new_universe.scenes
    assert len(scenes) > 0

    # TODO: make more pythonic by using 'all'
    for element in scenes:
        assert(type(element) == Scene)

    # .galactic_survey
    assert hasattr(new_universe, 'galactic_survey')
    survey = new_universe.galactic_survey
    assert len(survey) == 2
    assert len(survey[0]) == 2
    assert type(survey[0][0]) == int
    assert type(survey[0][1]) == str