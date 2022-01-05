# relink

A very simple Python utility that takes a symlink and relinks it with the newest file (mtime) in the target directory.

Example:

```
# ls -lh /data/symlinks/
symlink_a -> /data/files/a/v1

# ls -lh /data/files/a/
v1, mtime 1641394976
v2, mtime 1641394977

# relink /data/symlinks/symlink_a

# ls -lh /data/symlinks/
symlink_a -> /data/files/a/v2
```
