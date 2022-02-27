from geopy import Point

from src.arguments_parser import get_city
from src.models import City
from tests.utils import random_float
from tests.utils import random_string


def test_get_city() -> None:
    latitude = random_float()
    longitude = random_float()
    coordinates = Point(latitude, longitude)

    city = get_city(str(latitude), str(longitude))

    assert isinstance(city, City)
    assert city.coordinates == coordinates

    # Longitudes should range from -180 to 180.
    # If value is out of these boundaries, it will be normalized. See
    # https://github.com/geopy/geopy/blob/master/geopy/point.py#L77
    latitude = random_float()
    longitude = random_float(190, 360)
    coordinates = Point(latitude, longitude)

    city = get_city(str(latitude), str(longitude))

    assert isinstance(city, City)
    assert city.coordinates == coordinates


def test_if_coordinates_are_invalid() -> None:
    # if one of coordinates is invalid
    # it returns None
    latitude = random_float(-360, -190)
    longitude = random_float(190, 360)

    city = get_city(str(latitude), str(longitude))

    assert city is None
    latitude = random_float(-360, -190)
    longitude = random_float()

    city = get_city(str(latitude), str(longitude))

    assert city is None

    city = get_city(random_string(), random_string())

    assert city is None
