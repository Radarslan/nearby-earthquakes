from typing import Callable
from typing import List

from src.business_logic import get_closest_earthquakes
from src.business_logic import get_earthquakes_with_distances
from src.business_logic import get_ten_closest_earthquakes
from src.models import City
from src.models import Earthquake
from src.settings import NUMBER_OF_EVENTS


def test_get_closest_earthquakes(
    city: City, earthquake: Callable, earthquakes: List[Earthquake]
) -> None:
    earth_quake = earthquake()

    earthquakes = get_closest_earthquakes(city, earthquakes)

    for event in earthquakes:
        assert event.distance > 0
        assert earth_quake.distance <= event.distance

        earth_quake = event

    assert len(earthquakes) == NUMBER_OF_EVENTS


def test_get_earthquakes_with_distances(
    city: City, earthquake: Callable, earthquakes: List[Earthquake]
) -> None:
    earth_quake = earthquake()

    earthquakes = get_earthquakes_with_distances(city, earthquakes)

    for event in earthquakes:
        assert event.distance > 0
        assert earth_quake.distance <= event.distance

        earth_quake = event


def test_get_ten_closest_earthquakes(
    earthquake: Callable,
    earthquakes_with_distance: List[Earthquake],
) -> None:
    duplicates = 3
    earth_quake = earthquake()
    earth_quake.distance = 1
    earthquakes = [earth_quake] * duplicates + earthquakes_with_distance

    earthquakes = get_ten_closest_earthquakes(earthquakes)

    assert earthquakes.count(earth_quake) == 1
    assert len(earthquakes) == NUMBER_OF_EVENTS

    # if the list of earthquakes is less than NUMBER_OF_EVENTS
    # it returns less than NUMBER_OF_EVENTS events
    another_number_of_events = 7
    earthquakes = [earth_quake] * duplicates + earthquakes[
        :another_number_of_events
    ]

    earthquakes = get_ten_closest_earthquakes(earthquakes)

    assert earthquakes.count(earth_quake) == 1
    assert len(earthquakes) == another_number_of_events
