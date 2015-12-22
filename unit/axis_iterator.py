from __future__ import print_function
from pyplot import axis_iterator
import numpy

for index, axis in zip(range(9), axis_iterator(3,3, show_in_between=True)):
    image = numpy.array((100,100,3), dtype=numpy.float)
    image[:,:, int(index / 3)] = 1
    image[:,:, int(index % 3)] = 1
    axis.imshow(image)