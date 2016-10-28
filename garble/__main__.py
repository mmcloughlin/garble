import argparse
import sys
import json

import garble


def run(opts):
    data = json.load(opts.input)
    garbled = garble.garble(data)
    json.dump(garbled, opts.output)


def create_argument_parser():
    parser = argparse.ArgumentParser(description='Garble your data')
    parser.add_argument('-i', '--input',
            type=argparse.FileType('r'),
            default=sys.stdin)
    parser.add_argument('-o', '--output',
            type=argparse.FileType('w'),
            default=sys.stdout)
    parser.set_defaults(func=run)

    return parser


def main(args=None):
    args = args or sys.argv[1:]
    parser = create_argument_parser()
    opts = parser.parse_args(args)
    return opts.func(opts)


if __name__ == '__main__':
    main()
