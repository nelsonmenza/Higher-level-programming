#!/usr/bin/python3
import sys

if __name__ == "__main__":
    print("This is the name of the program:", sys.argv[0])
    print("Number of elements including the name of the program:", len(sys.argv))
    print("Number of elements excluding the name of the program:", len(sys.argv) - 1)

    # Check if there are additional arguments (excluding the program name)
    if len(sys.argv) > 1:
        print("Command-line arguments:")
        for arg in range(1, len(sys.argv)):
            print(f"{arg}: {sys.argv[arg]}")
    else:
        print("No additional command-line arguments provided.")
