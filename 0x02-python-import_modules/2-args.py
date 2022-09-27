#!/usr/bin/python3
if __name__ == "__main__":
    import sys

argCount = len(sys.argv) - 1
if argCount == 0:
   print("0 arguments.")
elif argCount == 1:
   print("1 argument")
else:
   print("{} argumetns:".format(argCount))
for i in range(1, len(sys.argv)):
   print("{}: {}".format(i, sys.argv[i]))
