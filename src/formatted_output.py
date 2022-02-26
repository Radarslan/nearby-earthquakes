from typing import List

from src.models import Earthquake
from src.settings import NUMBER_OF_EVENTS


def print_ten_closest_earthquakes(earthquakes: List[Earthquake]) -> None:
    print(f"\n{NUMBER_OF_EVENTS} closest earthquakes result:\n")
    for earthquake in earthquakes:
        print(f"{earthquake.title} || {earthquake.distance}")
