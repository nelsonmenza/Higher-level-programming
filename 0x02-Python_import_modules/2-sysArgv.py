#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    arguments = len(argv)
    # Print the name of the program
    print("Command-Line Argument Analyzer")
    # Print the total number of elements in argv (program name + arguments)
    print("Number of Arguments including the name of the program:", arguments)
    # Print the number of elements excluding the name of the program (arguments only)
    arg_count = arguments - 1
    print("Number of arguments excluding the name of the program:", arg_count)
    # Check if there are additional arguments (excluding the program name)
    if arg_count > 0:
        # If there are additional arguments, print them with their corresponding index
        print("Command-line arguments:")
        for arg in range(1, arguments):
            print(f"{arg}: {argv[arg]}")
    else:
        # If no additional arguments are provided, print a message indicating so
        print("No additional command-line arguments provided.")
