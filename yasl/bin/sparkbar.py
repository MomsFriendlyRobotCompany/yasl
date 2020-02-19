#!/usr/bin/env python3

import yasl
import argparse

def main():

    desc = """
    Draw bar graphs from input data. By default, it draws a vertical bar
    chart, but you can also draw a horizontal bar chart if you want.
    """

    parser = argparse.ArgumentParser(
        description=desc,
        # formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument("data",nargs=argparse.REMAINDER,help="Input data to plot")
    parser.add_argument("--horizontal", "-z", action="store_true", help="Draw horizontal bars")
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
        print(f'ERROR on input data: {e}')
        exit(1)

    if args.horizontal:
        print(sp.hbar(args.data))
    else:
        print(sp.vbar(args.data))
