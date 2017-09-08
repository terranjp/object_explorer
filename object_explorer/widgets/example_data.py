import numpy as np
import pint

class Person:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position
        self.arr1 = np.arange(0, 1000, 1)


ur = pint.UnitRegistry()
quantity = ur.Quantity

unit = 1 * ur['ft']

unit_array = np.arange(0, 2, 1) * ur['ft']

person = Person('tarren', 32, 'engineer')

d = [1, "two"]

my_list = list(range(1,10))
arr = np.arange(0, 10, 1)

example_dict = dict(unit=unit,
                    unit_array=unit_array)

