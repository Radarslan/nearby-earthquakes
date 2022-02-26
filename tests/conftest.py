from random import randint
from typing import Callable
from typing import List

import pytest
from geopy import Point

from src.models import City
from src.models import Earthquake
from tests.utils import random_float
from tests.utils import random_string


@pytest.fixture
def city() -> City:
    return City(
        coordinates=Point(latitude=random_float(), longitude=random_float())
    )


@pytest.fixture
def earthquake() -> Callable:
    def get_earthquake() -> Earthquake:
        return Earthquake(
            title=random_string(),
            coordinates=Point(
                latitude=random_float(), longitude=random_float()
            ),
        )

    return get_earthquake


@pytest.fixture
def earthquakes(earthquake: Callable) -> List[Earthquake]:
    return [earthquake() for _ in range(randint(25, 100))]


@pytest.fixture
def earthquakes_with_distance(
    earthquakes: List[Earthquake],
) -> List[Earthquake]:
    for earth_quake in earthquakes:
        earth_quake.distance = randint(1, 20000)
    return earthquakes
