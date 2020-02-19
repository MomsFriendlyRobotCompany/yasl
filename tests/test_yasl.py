from __future__ import print_function, division
from math import sin, pi
from yasl import Spark

def test_vbar():
    sp = Spark()
    data = [0,3,6,8.5,7,5,2,8,-8,1]

    print(u'max: {:.2f} min: {:.2f} [{}]'.format(max(data),min(data),sp.vbar(data)))

    assert True

def test_hbar():
    sp = Spark()
    data = []
    for i in range(36):
        data.append((sin(4*pi*i/36)))

    print(u'max: {:.2f} min: {:.2f} [{}]'.format(max(data),min(data),sp.hbar(data)))

    assert True

def test_unicode():
    sp = Spark()
    sp.dump()

    assert True
