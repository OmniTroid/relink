#!/usr/bin/env python3

import os
import sys
from pathlib import Path

sys.path.append('.')

import relink

# Runs relink on all symlinks in given directory
def relink_all(dir_ : Path):
	if not dir_.is_dir():
		print('Error: ' + str(dir_) + ' is not a directory.')
		return

	files = [file for file in dir_.iterdir() if file.is_symlink()]

	for file in files:
		relink.relink(file)

def main():
	if len(sys.argv) < 2:
		print('Error: expected one argument: directory')
		exit(1)

	relink_all(Path(sys.argv[1]))

if __name__ == '__main__':
	main()
