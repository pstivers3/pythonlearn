#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()

environments = ["dev", "prod"]
applications = "agent" 

parser.add_argument('environment', help='The environment to perform the action in.')
parser.add_argument('-b', '--branch', help='The branch to release.')
parser.add_argument('stuff', help='Dummy var.')

def print_args(args):
    print('\nenvironment: ', args.environment)
    print('stuff: ', args.stuff)
    print('branch: ', args.branch, '\n')

print_args(parser.parse_args())

