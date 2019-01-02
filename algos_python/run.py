# -*- coding: utf-8 -*-

"""Main module."""

from assignOne import CountInversions
from assignOne.Invertor import Invertor

import argparse
import os, sys


def parse_arguments():
    parser = argparse.ArgumentParser(description="Assignment response")
    parser.add_argument('-i', '--ipath', type=str, help="input file path")
    parser.add_argument('-o', '--opath', type=str, help="output file path")
    return parser.parse_args()


def resolve_path(path):
    if os.path.isabs(path):
        return path
    else:
        cwd = os.getcwd()
        return os.path.join(cwd, path)


def invert_count(filepath, output_filepath):
    """

    :param filepath: str, input filepath
    :param output_filepath: str, output filepath
    :return: None
    """

    filepath = resolve_path(filepath)
    output_filepath = resolve_path(output_filepath)

    invertor = Invertor(filepath, output_filepath)
    sorted_tup = CountInversions.my_sort(invertor.unsorted_list)
    invertor.set_sorted_list(sorted_tup[0])
    invertor.set_inversions(sorted_tup[1])
    invertor.write_sorted_list()


def main(arguments):
    invert_count(arguments.ipath, arguments.opath)


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    arguments = parse_arguments()
    main(arguments)
