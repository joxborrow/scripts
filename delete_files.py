#! /usr/bin/env python

import os
from optparse import OptionParser

# Parse all of the commandline options
parser = OptionParser()
parser.add_option("-d", "--directory", 
                  dest="root_dir",
                  type='string',
                  help="Root directory from which to delete all files.")

(options, args) = parser.parse_args()

# Verify that the directory exists


# Recurrsively delete all of the files
for root, dirs, files in os.walk('.'):
    for name in files:
        print(os.path.join(root, name))


