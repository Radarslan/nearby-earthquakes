from decouple import config

NUMBER_OF_EVENTS = config("NUMBER_OF_EVENTS", default=10, cast=int)
