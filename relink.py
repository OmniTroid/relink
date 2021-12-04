import os
import sys
from pathlib import Path

# Checks the origin directory of given symlink
# Unlinks the symlink, and relinks it with the newest
# File in the directory
def relink(file : Path):
	pass

def main():
	if len(sys.argv) < 2:
		print('Error: expected one argument: symlink path')
		exit(1)

	symlink = sys.argv[1]

	relink(symlink)

if __name__ == '__main__':
	main()
