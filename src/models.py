from geopy import Point
from pydantic import BaseModel


class Location(BaseModel):
    coordinates: Point

    class Config:
        arbitrary_types_allowed = True


class City(Location):
    pass


class Earthquake(Location):
    title: str
    distance: int = 0
