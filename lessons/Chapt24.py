# Variable scope = where variable visible & accessible
# Scope resolution = priority order (LEGB)Local->Enclosed->Global->Built-in

from math import e

def func1():
    print(e)

e = 3

func1()