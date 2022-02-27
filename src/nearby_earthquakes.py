"""
TODO:
* read input - args parse +
* validate input - must be valid longitude and latitude +
* get earthquakes for a month
    * requests with retries and notification to try later
    * exceptions for not 200 response
    * authentication and/or authorisation?
* find 10 with the shortest distance to the given city
    * how to find distance using long and lat
    * how to find the shortest distance
    * how to find 10 of them and get unique only

* print result
    * format like
    title || distance
    title || distance
    title || distance
    example:
    M 1.3 - 2km SSE of Contoocook, New Hampshire || 331
    M 1.3 - 2km ENE of Belmont, Virginia || 354
    M 2.4 - 83km ESE of Nantucket, Massachusetts || 406


!!!!!!!!!!
*TODO: WRITE TESTS
!!!!!!!!!!!!!!

"""

from src.arguments_parser import get_city_coordinates
from src.business_logic import get_closest_earthquakes
from src.earthquakes_getter import find_earthquakes
from src.formatted_output import print_ten_closest_earthquakes

if __name__ == "__main__":
    city_coordinates = get_city_coordinates()
    earthquakes = find_earthquakes()
    earthquakes = get_closest_earthquakes(city_coordinates, earthquakes)
    print_ten_closest_earthquakes(earthquakes)
