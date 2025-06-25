import my_modules.utils as utils  # namespacing
from my_modules.utils import printer
# a file
from main_analysis import headlines

print(headlines)


utils.printer("15 minutes to coffee!")

printer("I exist outside of my namespace")

square = utils.Shape("square")
print(square)
print("From app.py")
print(__name__)
print(__file__)
print(__doc__)

# Refactor
# open()


