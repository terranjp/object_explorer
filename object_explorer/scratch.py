import numpy as np
import inspect
from main import main

import pint
from pint.quantity import _Quantity


ur = pint.UnitRegistry()
Q_ = ur.Quantity

unit = 1 * ur['ft']

arr = np.arange(0, 10, 0.2)


c = Q_(arr, 'ft')





def getCompUnits(quantity: _Quantity) -> []:

    reg = quantity._REGISTRY




    return set(reg.get_compatible_units(quantity.u))


# print(list(c.compatible_units()))


units = getCompUnits(c)

ur.default_system = 'US'
print(getCompUnits(c))


ur.default_system = 'cgs'
print(getCompUnits(c))

ur.default_system = 'mks'
print(getCompUnits(c))

ur.default_system = 'imperial'
print(getCompUnits(c))


def setup_data(data):

    frame = inspect.currentframe()
    var_id = id(data)

    for name in frame.f_back.f_locals.keys():

        try:
            if id(eval(name)) == var_id:
                return name
        except:
            pass




