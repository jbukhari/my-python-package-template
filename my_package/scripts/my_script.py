""""""

import sys, os, re
from argparse import ArgumentParser

def options():
    if not sys.argv[1:]:
        raise ValueError('Arguments supplied via sys.argv are required')

    ap = ArgumentParser(prog="my-script", usage="")
    ap.add_argument('--my_param', default='', help='')

    return ap.parse_args()

def run():
    args = options()
    print(f'Running with {sys.argv[1:]}')
    
    return args.my_param

if __name__ == '__main__':
    run()