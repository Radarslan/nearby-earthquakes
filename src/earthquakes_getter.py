"""
probably the task could have been solved using the following API call
url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
params = {
    "format": "geojson",
    "eventtype": "earthquake"
    "latitude": 40.730610,
    "longitude": -73.935242,
    "limit": 10,
    "maxradius": 180
}
response = requests.get(url=url, params=params)
but I have not checked if it returns the closest ones or not
"""

from typing import Any
from typing import Dict
from typing import List
from typing import Optional

import requests
from geopy import Point
from requests.exceptions import HTTPError
from requests.exceptions import Timeout
from retry import retry

from src.models import Earthquake
from src.settings import LAST_MONTH_EVENTS_URL
from src.settings import REQUESTS_TIMEOUT


def find_earthquakes() -> List[Earthquake]:
    print("trying to get all earthquakes that happened during last 30 days")
    events = get_earthquakes()
    earthquakes = parse_earthquakes(events)
    return earthquakes


@retry((HTTPError, Timeout), tries=5, delay=4, backoff=2)
def get_earthquakes() -> Dict[str, Any]:
    response = requests.get(
        url=LAST_MONTH_EVENTS_URL, timeout=REQUESTS_TIMEOUT
    )
    response.raise_for_status()
    return response.json()


def parse_earthquakes(events: Dict[str, Any]) -> List[Earthquake]:
    earthquakes = []

    for event in events.get("features", []):
        earthquake = get_earthquake(event)
        if earthquake is not None:
            earthquakes.append(earthquake)
    return earthquakes


def get_earthquake(event: Dict[str, Any]) -> Optional[Earthquake]:
    properties = event.get("properties", None)
    geometry = event.get("geometry", None)
    title = None
    coordinates = None
    if properties is not None:
        title = properties.get("title", None)
    if geometry is not None:
        coordinates = geometry.get("coordinates", None)

    if title is not None and coordinates is not None:
        return Earthquake(
            title=title,
            coordinates=Point(
                latitude=coordinates[1], longitude=coordinates[0]
            ),
        )

    return None
