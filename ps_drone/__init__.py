import sys

if sys.version_info[0] < 3: # Python 2
    from .ps_drone2 import *
else: # Python 3
    from .ps_drone3 import *

    