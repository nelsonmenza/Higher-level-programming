#!/usr/bin/python3
# A script to sum all arguments
import sys
if __name__ == "__main__":

    for arg in range(1, len(sys.argv)):
        print(sys.argv[arg], end="")
    