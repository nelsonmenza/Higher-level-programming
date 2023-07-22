#!/usr/bin/python3

# This script reads the contents of a file named "fileEasyPrint.txt" located in the directory "0x02-Python-import_modules/modules/".
# It then prints the contents of the file to the console.

# Open the file "fileEasyPrint.txt" in read mode and assign it to the variable easy_print.
easy_print = open("0x02-Python-import_modules/modules/fileEasyPrint.txt")

# Read the contents of the file and print them to the console.
print(easy_print.read())
