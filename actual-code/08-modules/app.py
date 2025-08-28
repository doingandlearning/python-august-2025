import utils as u
from utils import printer as p
import os
import matplotlib

# import numpy as np   - aliasing the module
# import pandas as pd

u.printer(f"Hi from main.py! __name__ == {__name__}") # namespacing
new_shape = u.Shape("square")


print(os.cpu_count())

# Cmd-shift-P
# Ctrl-shift-P

print(dir(matplotlib))