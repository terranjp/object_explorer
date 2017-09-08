import numpy as np
import pint


class Person:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position
        self.arr1 = np.arange(0, 1000, 1)


ur = pint.UnitRegistry()
Quantity = ur.Quantity


unit = 1 * ur['ft']
unit2 = Quantity('1 ft')
unit_array = np.arange(0, 3, 0.5) * ur['m']
person = Person('tarren', 32, 'engineer')
d = [1, "two"]
my_list = list(range(1,10))
arr = np.arange(0, 10, 1)

example_dict = dict(unit=unit,
                    unit_array=unit_array,
                    arr=arr)

