#! /usr/bin/python
#################################################################################################
# Author: Nicholas Fisher
# Date: March 4th 2024
# Description of Script
# This script implements a directory listener module that recursively lists all files in all 
# directories starting from the current directory. The list_files function uses os.walk to 
# traverse all directories and collect file paths, which are then returned as a list of strings. 
# The run function calls list_files with the current directory and returns the list of files as a 
# string. To use the code, simply import the module and call the run function. For example:
# import dirlistener
# result = dirlistener.run()
# print(result)
# This will print a string containing the names of all files in all directories starting from the current directory.
#################################################################################################
import os

def list_files(directory):
    """
    Recursively lists all files in a directory.

    Args:
        directory (str): The directory to start listing files from.

    Returns:
        list: A list of strings, where each string is a file path.
    """
    files = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.join(dirpath, filename))
    return files

def run(**args):
    """
    This function lists all files in all directories starting from the current directory.

    Args:
        **args: Arbitrary keyword arguments (not used in this function).

    Returns:
        str: A string containing the names of all files in all directories.
    """
    print("[*] In dirlistener module.")
    files = list_files(".")
    return str(files)
