import sys
from typing import Optional
from typing import Tuple

from geopy import Point

from src.models import City


def get_city_coordinates() -> City:
    while True:
        latitude, longitude = parse_arguments()
        city = get_city(latitude, longitude)
        if city is None:
            check_exit()
        else:
            return city


def parse_arguments() -> Tuple[str, str]:
    latitude = input("enter the city's latitude: ")
    longitude = input("enter the city's longitude: ")
    return latitude, longitude


def get_city(latitude: str, longitude: str) -> Optional[City]:
    """
    Signed degrees format (DDD.dddddd)
    Precede South latitudes and West longitudes with a minus sign.
    Latitudes range from -90 to 90.
    Longitudes range from -180 to 180. If value is out of these boundaries,
    it will be normalized. See
    https://github.com/geopy/geopy/blob/master/geopy/point.py#L77
    41.25 and -120.9762
    -31.96 and 115.84
    90 and 0 (North Pole)
    """
    city = None
    try:
        lat = float(latitude)
        lon = float(longitude)

        coordinates = Point(lat, lon)
        city = City(coordinates=coordinates)
    except Exception:
        print("provided latitude and/or longitude are invalid\n")
        print(
            "the latitude must be a number between -90 and 90\n"
            "and\n"
            "the longitude should be a number between -180 and 180"
        )

    return city


def check_exit() -> None:
    answer = input("do you want to retry? (y/n): ").lower().strip()
    if answer != "y":
        sys.exit("\nprogram terminated by user")
