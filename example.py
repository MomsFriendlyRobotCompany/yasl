#!/usr/bin/env python

from __future__ import print_function, division
from math import sin, pi
from yasl import Spark

if __name__ == "__main__":
    sp = Spark()
    data = [0,3,6,8.5,7,5,2,8,-8,1]
    # print(sp.vbar(data))
    print(u'max: {:.2f} min: {:.2f} [{}]'.format(max(data),min(data),sp.vbar(data)))

    data = []
    for i in range(36):
        data.append((sin(4*pi*i/36)))
    # print(data)
    print(u'max: {:.2f} min: {:.2f} [{}]'.format(max(data),min(data),sp.hbar(data)))

    # sp.dump()
