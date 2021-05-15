#! /usr/bin/env python

import os
from optparse import OptionParser

# Parse all of the commandline options
parser = OptionParser()
parser.add_option("-d", "--directory", 
                  dest="root_dir",
                  type='string',
                  help="Root directory from which to delete all files.")
parser.add_option("-dr", "--dry-run",
                  action = "store_true",
                  default = False,
                  help = "Prints all file names to the console, instead of deleteing them.",
                  dest="dry_run")

(options, args) = parser.parse_args()

# Verify that the directory exists

if (options.dry_run == True):
    # Print all of the files that will be deleted
    for root, dirs, files in os.walk('.'):
        for name in files:
            print(os.path.join(root, name))
else:
    print("Files deleting ...")



