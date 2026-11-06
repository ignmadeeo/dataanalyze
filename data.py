import numpy
import time

y = 0

x = numpy.random.uniform(0.0, 40, 20)
while True:
    x = numpy.random.uniform(0.0, 40, 1)
    y += 1
    print(y, x)
    time.sleep(0.2)
    if y == 20:
        break