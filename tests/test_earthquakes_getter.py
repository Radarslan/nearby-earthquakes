from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional

import requests
from pytest import MonkeyPatch

from src.earthquakes_getter import find_earthquakes
from src.earthquakes_getter import get_earthquake
from src.earthquakes_getter import get_earthquakes
from src.earthquakes_getter import parse_earthquakes
from src.models import Earthquake


def test_find_earthquakes(
    monkeypatch: MonkeyPatch,
    mock_get: Callable,
    earthquake_event: Dict[str, Any],
    coordinates: List[float],
    title: str,
) -> None:
    monkeypatch.setattr(requests, "get", mock_get)

    earth_quakes = find_earthquakes()
    assert_earth_quakes(earth_quakes, coordinates, title)


def assert_earth_quakes(
    earth_quakes: List[Earthquake], coordinates: List[float], title: str
) -> None:

    for earth_quake in earth_quakes:
        assert_earth_quake(earth_quake, coordinates, title)


def assert_earth_quake(
    earth_quake: Optional[Earthquake], coordinates: List[float], title: str
) -> None:
    assert isinstance(earth_quake, Earthquake)
    assert earth_quake.title == title
    assert earth_quake.coordinates.latitude in coordinates
    assert earth_quake.coordinates.longitude in coordinates


def test_get_earthquakes(
    monkeypatch: MonkeyPatch,
    mock_get: Callable,
    earthquake_events: Dict[str, Any],
) -> None:
    monkeypatch.setattr(requests, "get", mock_get)

    earth_quakes = get_earthquakes()

    assert earth_quakes == earthquake_events
    assert earth_quakes is earthquake_events


def test_parse_earthquakes(
    earthquake_events: Dict[str, Any],
    earthquake_event: Dict[str, Any],
    coordinates: List[float],
    title: str,
) -> None:
    earth_quakes = parse_earthquakes(earthquake_events)

    assert_earth_quakes(earth_quakes, coordinates, title)


def test_one_event_is_broken(earthquake_events: Dict[str, Any]) -> None:
    # if any event is broken
    # it is not added to the result
    event = earthquake_events["features"][0]
    event["geometry"] = None

    result_earth_quakes = parse_earthquakes(earthquake_events)

    assert len(earthquake_events) > len(result_earth_quakes)
    assert event in earthquake_events["features"]
    assert event not in result_earth_quakes


def test_get_earthquake(
    earthquake_event: Dict[str, Any], coordinates: List[float], title: str
) -> None:
    earth_quake = get_earthquake(earthquake_event)

    assert_earth_quake(earth_quake, coordinates, title)


def test_if_received_broken_event(earthquake_event: Dict[str, Any]) -> None:
    # if a 'broken' event is given
    # it returns None
    earthquake_event["geometry"]["coordinates"] = None
    earth_quake = get_earthquake(earthquake_event)
    assert earth_quake is None

    earthquake_event["geometry"] = None
    earth_quake = get_earthquake(earthquake_event)
    assert earth_quake is None

    earthquake_event["properties"]["title"] = None
    earth_quake = get_earthquake(earthquake_event)
    assert earth_quake is None

    earthquake_event["properties"] = None
    earth_quake = get_earthquake(earthquake_event)
    assert earth_quake is None
