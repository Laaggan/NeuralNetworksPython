import numpy

# fixme: This does not work
def HeavisideFunction(x):
    result = numpy.zeros(x.__len__())
    for xi, i in enumerate(x):
        if xi < 0:
            result[i] = 0
        else:
            result[i] = 1
    return result