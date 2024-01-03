#! /usr/bin/env python


import os
from optparse import OptionParser

# Parse all of the command line options
parser = OptionParser()
parser.add_option("-d", "--directory", 
                  dest="root_dir",
                  type='string',
                  help="Root directory from which to delete all files.")
parser.add_option("-r", "--dry-run",
                  action = "store_true",
                  default = False,
                  help = "Prints all file names to the console, instead of deleting them.",
                  dest="dry_run")

(options, args) = parser.parse_args()

# Verify that the directory exists
if not os.path.isdir(options.root_dir):
    raise Exception("Not a valid directory")

# Execute file printing or file deletions
if (options.dry_run == True):
    # Print all of the files that will be deleted
    for root, dirs, files in os.walk(options.root_dir):
        for name in files:
            print(os.path.join(root, name))
else:
    # Delete the files from the root directory
    for root, dirs, files in os.walk(options.root_dir):
        for name in files:
            os.remove(os.path.join(root, name))

    print(f"All files deleted from {options.root_dir}")



