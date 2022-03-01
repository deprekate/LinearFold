#!/usr/bin/env python3
import sys
import fileinput
import argparse
from argparse import RawTextHelpFormatter

import LinearFold as lf



if __name__ == '__main__':
	usage = '%s [-opt1, [-opt2, ...]] infile' % __file__
	parser = argparse.ArgumentParser(description='', formatter_class=RawTextHelpFormatter, usage=usage)
	parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
	args = parser.parse_args()

	for line in args.infile:
		print(lf.fold(line))
