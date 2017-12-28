# even if main load classes, you still need to import it here
from classes2load import *

def function_with_class1():
    molly = Human('Molly', 29 )
    molly.print_features()

def function_with_class2():
    matt = Human('Matt', 29 )
    matt.print_features()
