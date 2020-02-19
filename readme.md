# Yet Another Sparkline (yasl)

[![Actions Status](https://github.com/MomsFriendlyRobotCompany/yasl/workflows/CheckPackage/badge.svg)](https://github.com/MomsFriendlyRobotCompany/yasl/actions)
![GitHub](https://img.shields.io/github/license/MomsFriendlyRobotCompany/yasl)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/yasl)
![PyPI](https://img.shields.io/pypi/v/yasl)


Why? Well, it is actually really easy to do this and I wanted some different
controls that the other programs didn't have. Also, I like the MIT license.

## Usage

You can run it from the command line:

```bash
  kevin@dalek psl $ sparkbar.py  1 2 3E+0 4
   ▂▅█
  kevin@dalek psl $ sparkbar.py -z 1 2 3E+0 4
   ▎▋█
  kevin@dalek psl $ sparkbar.py 1 2 3 4 3 2 1 0 3 5
  ▁▃▄▆▄▃▁ ▄█
```

Or call it from a python program:

```python
  #!/usr/bin/env python

  from math import sin, pi
  from yasl import Spark

  if __name__ == "__main__":
      sp = Spark()
      data = [0,3,6,8.5,7,5,2,8,-8,1]

      print(u'max: {:.2f} min: {:.2f} [{}]'.format(max(data),min(data),sp.vbar(data)))

      data = []
      for i in range(36):
          data.append((sin(4*pi*i/36)))

      print(u'max: {:.2f} min: {:.2f} [{}]'.format(max(data),min(data),sp.hbar(data)))

      sp.dump()
```

```bash
  kevin@dalek psl $ python3 example.py
  max: 8.50 min: -8.00 [▃▅▆█▇▆▄▇ ▄]
  max: 0.98 min: -0.98 [▌▋▊▉██▉▊▋▌▎▏    ▏▎▍▋▊▉▉█▉▊▋▌▎▏    ▏▎]
```

# MIT License

**Copyright (c) 2017 Kevin J. Walchko**

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
