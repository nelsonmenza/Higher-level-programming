#!/usr/bin/python3
# A script to sum all arguments
from sys import argv
if __name__ == "__main__":
    try:
        arguments = len(argv)
        if arguments > 1:  # Check if there are command line arguments
            sum_arg = 0  # Variable to store the sum of arguments
            # Iterate through the command line arguments
            for arg in range(1, arguments):
                # Convert the argument to an integer
                arg_int = int(argv[arg])
                sum_arg += arg_int  # Add the integer argument to the sum
            print(f"The result of summing the arguments is: {sum_arg}")
        else:
            print("No command line arguments provided.")
    except ValueError as e:
        print(f"Invalid argument: {e}")
