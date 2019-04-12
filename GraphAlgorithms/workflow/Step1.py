# coding=utf-8
# Startup.  The Montage modules are pretty much self-contained
# but this script needs a few extra utilities.

import os
import sys
import shutil

from MontagePy.main    import *
from MontagePy.archive import *

from IPython.display import Image


# These are the parameters defining the mosaic we want to make.

location  = "M 17"
size      = 1.0
dataset   = "2MASS J"
workdir   = "Messier017"

