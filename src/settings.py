from decouple import config

NUMBER_OF_EVENTS = config("NUMBER_OF_EVENTS", default=10, cast=int)
LAST_MONTH_EVENTS_URL = config(
    "LAST_MONTH_EVENTS_URL",
    (
        "https://earthquake.usgs.gov/earthquakes"
        "/feed/v1.0/summary/all_month.geojson"
    ),
)
REQUESTS_TIMEOUT = config("REQUESTS_TIMEOUT", default=20, cast=int)
