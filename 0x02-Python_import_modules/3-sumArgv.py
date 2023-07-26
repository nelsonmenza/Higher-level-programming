#!/usr/bin/python3
# A script to sum all arguments
import sys
if __name__ == "__main__":
    try:
        if len(sys.argv) > 0:  # Check if there are command line arguments
            sum_arg = 0  # Variable to store the sum of arguments
            # Iterate through the command line arguments
            for arg in range(1, len(sys.argv)):
                # Convert the argument to an integer
                arg_int = int(sys.argv[arg])
                sum_arg += arg_int  # Add the integer argument to the sum
        print(f"The result of summing the arguments is: {sum_arg}")
    except ValueError:
        print("Please enter correct characters that can be converted to integers.")
