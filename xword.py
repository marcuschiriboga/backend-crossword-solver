#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

__author__ = "marcus, thanks joe, jt"

# YOUR HELPER FUNCTION GOES HERE
import sys
import argparse


def create_parser():
    """Creates an argument parser object."""
    """ to watch(dir), file extension to filter on(ext),
    polling interval(int) and magic text(magic)"""
    parser = argparse.ArgumentParser()
    parser.add_argument('word',
                        help='enter a partial word to look for complete words,'
                        'use _ as wild cards')
    parser.add_argument(
        'word_length', help="the size of word your looking for")
    return parser


def sorter(word, known_char, word_length):
    """ build the list with potential matches"""
    if len(word) != word_length:
        return False
    for n, c in known_char:
        if word[n] != c:
            return False
    return True


def main(args):
    parser = create_parser()
    if not args:
        parser.print_usage()
        sys.exit(1)
    parsed_args = parser.parse_args(args)
    test_word = parsed_args.word
    word_length = int(parsed_args.word_length)
    known_char = [(i, c) for i, c in enumerate(test_word) if c != "_"]
    with open('dictionary.txt') as f:
        words = f.read().split()
        filtered_words = [word for word in words if sorter(
            word, known_char, word_length)]
        print(filtered_words)


if __name__ == '__main__':
    main(sys.argv[1:])
