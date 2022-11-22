from microbit import *
import random

class Intensity:

    def __init__(self):
        self._intensity = random.randrange(10)
        self._tick = 0
        self._direction = 1;
        r = random.randrange(3)
        if r == 0:
            self.fn = lambda t, i: t % 2 == 0
        elif r == 1:
            self.fn = lambda t, i: t % 3 == 0
        else:
            self.fn = lambda t, i: t % 4 == 0
    
    def intensity(self):
        self._update_intensity()
        self._tick += 1
        return self._intensity

    def _update_intensity(self):
        if self.fn(self._tick, self._intensity):
            self._update_direction()
            self._intensity += self._direction

    def _update_direction(self):
        if self._intensity <= 0:
            self._direction = 1
        if self._intensity >= 9:
            self._direction = -1

dict = {}
dict[(0, 0)] = Intensity()
dict[(1, 1)] = Intensity()
dict[(4, 1)] = Intensity()
dict[(2, 2)] = Intensity()
dict[(0, 3)] = Intensity()
dict[(3, 0)] = Intensity()
dict[(3, 3)] = Intensity()

while True:
    for k in dict.keys():
        display.set_pixel(k[0], k[1], dict[k].intensity())
    sleep(50)