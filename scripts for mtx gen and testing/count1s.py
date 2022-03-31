import sys
import numpy as np

def main():
    me, fname = sys.argv

    f = open(fname, "r")

    count = 0

    for line in f:
        if int(line) == 1:
            count += 1

    print(count)

if __name__ == "__main__":
    main()