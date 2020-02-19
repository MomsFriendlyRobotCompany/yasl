#!/usr/bin/env python

from __future__ import print_function, division
import yasl
import argparse

parser = argparse.ArgumentParser(
    description=yasl.__doc__.encode('utf-8'),
    # formatter_class=argparse.RawDescriptionHelpFormatter
    )
parser.add_argument("data",nargs=argparse.REMAINDER,help="Input data to plot")
parser.add_argument("--horizontal", "-r", action="store_true", help="Draw horizontal bars")
parser.add_argument("--version", "-v", action="store_true", help="Prints version number and exits")

args = parser.parse_args()

if args.version:
    print(yasl.__version__)
    exit(0)

sp = yasl.Spark()

try:
    for i, d in enumerate(args.data):
        args.data[i] = float(d)
except Exception as e:
    print('ERROR on input data:', e)
    exit(1)

# print(args.data)

if args.horizontal:
    print(sp.hbar(args.data))
else:
    print(sp.vbar(args.data))
