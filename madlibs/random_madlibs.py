"""this program will select from a random madlib from a folder
and present to the user. """

import random

from sample import code, haunted_house, zombie

x = random.choice([code, haunted_house, zombie])
x.madlib()
