import sys

# in py3, unichr doesn't exist, so we will just alias it to chr
if int(sys.version[0]) > 2:
    unichr = chr

class Spark(object):
    def __init__(self):
        """
        """
        self.vbars = [' '] + [unichr(int(0x2581 + i)) for i in range(8)]
        tmp = [unichr(int(0x2588 + i)) for i in range(8)]
        tmp.reverse()
        self.hbars = [' '] + tmp

    def dump(self):
        print('vbar')
        for i, b in enumerate(self.vbars):
            print(i, b)
        print('hbar')
        for i, b in enumerate(self.hbars):
            print(i, b)

    def scale(self, data, mx_val=8):
        """
        Scale the data between integer values 0-8
        """
        mx = max(data)
        mn = min(data)
        k = mx_val/(mx-mn)
        b = -k*mn

        ret = [int(k*d+b) for d in data]
        return ret,mx,mn

    def bar(self, data, blocks):
        """
        Draw bar, given the data and block arrays
        """
        ret = []
        data ,_,_= self.scale(data, len(blocks)-1)
        for d in data:
            ret.append(blocks[d])
        return u''.join(ret)

    def vbar(self, data):
        return self.bar(data, self.vbars)

    def hbar(self, data):
        return self.bar(data, self.hbars)
