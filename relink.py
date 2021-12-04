import os
from pathlib import File


# Checks the origin directory of given symlink
# Unlinks the symlink, and relinks it with the newest
# File in the directory
def relink(file : File):
	pass

def main():
	if len(os.args) < 2:
		print('Error: expected one argument: symlink path')
		exit(1)

	symlink = os.args[1]

	relink(symlink)

if __name__ == '__main__':
	main()
