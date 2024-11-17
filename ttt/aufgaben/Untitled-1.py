import sys

print("sys.path")
for path in sys.path:
    print(path)

print("sys.builtin_module_names")
print(sys.builtin_module_names)

import os
print("os.getcwd")
cwd = os.getcwd()
print(cwd)