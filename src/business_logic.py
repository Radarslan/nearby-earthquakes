from typing import List

from geopy import distance

from src.models import City
from src.models import Earthquake
from src.settings import NUMBER_OF_EVENTS


def get_closest_earthquakes(
    city: City, earthquakes: List[Earthquake]
) -> List[Earthquake]:
    print("getting distances")
    earthquakes = get_earthquakes_with_distances(city, earthquakes)
    print(f"filtering {NUMBER_OF_EVENTS} closest earthquakes")
    return get_ten_closest_earthquakes(earthquakes)


def get_earthquakes_with_distances(
    city: City, earthquakes: List[Earthquake]
) -> List[Earthquake]:
    for earthquake in earthquakes:
        earthquake.distance = round(
            distance.distance(city.coordinates, earthquake.coordinates).km
        )
    return sorted(earthquakes, key=lambda earthquake: earthquake.distance)


def get_ten_closest_earthquakes(
    earthquakes: List[Earthquake],
) -> List[Earthquake]:
    unique_coordinates = set()
    result: List[Earthquake] = []
    for earthquake in earthquakes:
        coordinates = tuple(earthquake.coordinates)
        if coordinates not in unique_coordinates:
            result.append(earthquake)
            unique_coordinates.add(coordinates)
        if len(result) == NUMBER_OF_EVENTS:
            return result

    return result
