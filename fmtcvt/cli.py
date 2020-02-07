import argparse

from .core import convert


def main():
    parser = argparse.ArgumentParser("Convert Structured Text Files")
    parser.add_argument("-i", "--in-path")
    parser.add_argument("-o", "--out-path")
    args = parser.parse_args()

    convert(args.in_path, args.out_path)
