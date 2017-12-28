from variableload import *
from functions2load import *
from classes2load import *
from function_that_uses_class import *

if __name__== '__main__':
    print( 'In main' )
    # variables
    if 1:
        print( a, b )
    # functions
    if 1:
        c = 5
        d = 6
        print( add2numbers( c, d ) )
        print( mult2numbers( c, d ) )
    # classes
    if 1:
        mike = Human('Mike',29)
        mike.print_features()
        austin = Human('Austin','lab')
        austin.print_features()
    # function with class
    if 1:
        function_with_class1()
        function_with_class2()
