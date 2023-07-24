#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Print the name of the program
    print("Command-Line Argument Analyzer")

    # Print the name of the program (sys.argv[0])
    print("This is the name of the program:", sys.argv[0])

    # Print the total number of elements in sys.argv (program name + arguments)
    print("Number of elements including the name of the program:", len(sys.argv))

    # Print the number of elements excluding the name of the program (arguments only)
    print("Number of elements excluding the name of the program:", len(sys.argv) - 1)

    # Check if there are additional arguments (excluding the program name)
    if len(sys.argv) > 1:
        # If there are additional arguments, print them with their corresponding index
        print("Command-line arguments:")
        for arg in range(1, len(sys.argv)):
            print(f"{arg}: {sys.argv[arg]}")
    else:
        # If no additional arguments are provided, print a message indicating so
        print("No additional command-line arguments provided.")
