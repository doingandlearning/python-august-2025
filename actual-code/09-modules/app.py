"""
This is a doc string
"""

import utils as ut
from utils import Shape, default_shape, printer as p
from random import randint
# from utils import *   # while possible, avoid!



print(randint(1,20))
p("hahaha")
def printer():
    print("Lalalalalala")

circle = ut.Shape("circle")
print(circle)

print(ut.default_shape)

ut.printer("This is fun!!")

parallelogram = Shape("parallelogram")
print(parallelogram)

print("This is from app.py")
print(__name__)
print(__doc__)
print(__file__)
print("-" * 25)

import sys
print(sys.path)

import os
print(os.cpu_count())

from datetime import datetime

# print(datetime.date.today())
print(datetime.now())

import time

start = time.time()

total = 0
for i in range(10000000):
    total += i

print(total)
print(time.time() - start)
