#!/usr/bin/env python3

import os
import sys
from pathlib import Path

# Checks the origin directory of given symlink
# Unlinks the symlink, and relinks it with the newest
# File in the origin directory
def relink(file : Path):
	if not file.is_symlink():
		print('Error: ' + str(file) + ' is not a symlink.')
		return

	origin_dir = file.resolve().parent

	newest_file = sorted(
		(file for file in origin_dir.iterdir()),
		key=lambda x: x.stat().st_mtime)[-1]

	file.unlink()
	file.symlink_to(newest_file)

	print('Symlinked ' + str(file) + ' to ' + str(newest_file))

def main():
	if len(sys.argv) < 2:
		print('Error: expected one argument: symlink path')
		exit(1)

	symlink = Path(sys.argv[1])

	relink(symlink)

if __name__ == '__main__':
	main()
