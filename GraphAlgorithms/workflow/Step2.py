# coding=utf-8
# We create and move into subdirectories in this notebook
# but we want to come back to the original startup directory
# whenever we restart the processing.

import os
import sys
import shutil


workdir   = "Messier017"



try:
    home
except:
    home = os.getcwd()

os.chdir(home)

print("Startup folder: " + home)


# Clean out any old copy of the work tree, then remake it
# and the set of the subdirectories we will need.

try:
    shutil.rmtree(workdir)
except:
    print("                Can't delete work tree; probably doesn't exist yet", flush=True)

print("Work directory: " + workdir, flush=True)

os.makedirs(workdir)

os.chdir(workdir)

os.makedirs("raw")
os.makedirs("projected")
os.makedirs("diffs")
os.makedirs("corrected")