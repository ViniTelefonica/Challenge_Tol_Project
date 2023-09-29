from cameraSim import simulator
from jsonMaker import jsonMaker

names = simulator(detecting=True)

jsonMaker(names)