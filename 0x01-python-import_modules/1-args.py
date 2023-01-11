#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    numbArm = len(sys.argv) - 1
    if numbArm == 0:
        print("0 arguments.")
    elif numbArm == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(numbArm))
    for i in range(numbArm):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
