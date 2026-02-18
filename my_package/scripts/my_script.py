""""""

import sys, os, re
from argparse import ArgumentParser

def options():
    if not sys.argv[1:]:
        sys.argv[1:] = ['--help']

    ap = ArgumentParser(prog="my-script", usage="")
    ap.add_argument('--my_param', required=False, type=int, default=1, help='')
    
    return ap.parse_args()

def run():
    args = options()
    print(f'Running with {sys.argv[1:]}')
    
    return args.my_param

if __name__ == '__main__':
    run()