from random import randint
from typing import Any
from typing import Callable
from typing import Dict
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


@pytest.fixture
def earthquake_event() -> Dict[str, Any]:
    return {
        "type": "Feature",
        "properties": {
            "mag": 0.35,
            "place": "6km NW of The Geysers, CA",
            "time": 1645732764220,
            "updated": 1645732860573,
            "tz": None,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage"
            "/nc73697401",
            "detail": "https://earthquake.usgs.gov/earthquakes/"
            "feed/v1.0/detail"
            "/nc73697401.geojson",
            "felt": None,
            "cdi": None,
            "mmi": None,
            "alert": None,
            "status": "automatic",
            "tsunami": 0,
            "sig": 2,
            "net": "nc",
            "code": "73697401",
            "ids": ",nc73697401,",
            "sources": ",nc,",
            "types": ",nearby-cities,origin,phase-data,",
            "nst": 8,
            "dmin": 0.007005,
            "rms": 0.02,
            "gap": 147,
            "magType": "md",
            "type": "earthquake",
            "title": "M 0.4 - 6km NW of The Geysers, CA",
        },
        "geometry": {
            "type": "Point",
            "coordinates": [-122.8013306, 38.8218346, 3.16],
        },
        "id": "nc73697401",
    }


@pytest.fixture
def coordinates(earthquake_event: Dict[str, Any]) -> List[float]:
    return earthquake_event.get("geometry", {}).get("coordinates", [])


@pytest.fixture
def title(earthquake_event: Dict[str, Any]) -> str:
    return earthquake_event.get("properties", {}).get("title", "")


@pytest.fixture
def earthquake_events(earthquake_event: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "type": "FeatureCollection",
        "metadata": {
            "generated": 1645724106000,
            "url": "https://earthquake.usgs.gov/fdsnws/event/1/query"
            "?latitude=40.730610"
            "&longitude=-73.935242"
            "&limit=10"
            "&maxradius=180"
            "&format=geojson",
            "title": "USGS Earthquakes",
            "status": 200,
            "api": "1.13.3",
            "limit": 10,
            "offset": 1,
            "count": 10,
        },
        "features": [earthquake_event] * randint(10, 25),
    }


@pytest.fixture
def mock_get(earthquake_events: Dict[str, Any]) -> Callable:
    class MockResponse:
        @staticmethod
        def json() -> Dict[str, Any]:
            return earthquake_events

        @staticmethod
        def raise_for_status() -> None:
            pass

    def mock_get(*args: tuple, **kwargs: dict) -> MockResponse:
        return MockResponse()

    return mock_get
