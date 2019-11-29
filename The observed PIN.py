

My solution:

import itertools

def get_pins(observed):
    #matrix ... reloaded :))
    close = {
        '1': ['2','4'],
        '2': ['1','3','5'],        
        '3': ['2','6'],
        '4': ['1','5','7'],
        '5': ['2','4','6','8'],
        '6': ['3','5', '9'],
        '7': ['4','8'],
        '8': ['5','7','9','0'],
        '9': ['6','8'],
        '0': ['8'],    
    }
    
    arr_list = [ [nr] + close[nr] for nr in observed]
    #print(observed)
    #print(arr_list)
    pin_list = [''.join(item) for item in list(itertools.product(*arr_list))]
    #print(pin_list)
    
    return pin_list



Best practice + Clever:
from itertools import product

ADJACENTS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')

def get_pins(observed):
    return [''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))]