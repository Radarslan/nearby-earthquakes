from random import choice
from random import uniform
from string import ascii_lowercase
from string import digits


def random_string(length: int = 7) -> str:
    alpha_num = ascii_lowercase + digits
    result = ""
    for i in range(length):
        result += choice(alpha_num)
    return result


def random_float(start: int = -90, end: int = 90) -> float:
    return uniform(start, end)
