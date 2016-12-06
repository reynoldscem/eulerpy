from functools import reduce
from itertools import count
import argparse
import os


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    return parser


def number_generator(max_num, conds=(3, 5)):
    for i in count():
        if i == max_num:
            break
        for cond in conds:
            if i % cond == 0:
                yield i
                continue

def main(args):
    with open(args.filename) as fd:
        data = int(fd.read().rstrip())

    answer = reduce(
        lambda x, y: x + y, number_generator(data)
    )
    print(answer)


if __name__ == '__main__':
    args = build_parser().parse_args()
    assert os.path.isfile(args.filename), 'Must provide a valid filename'
    main(args)
