import ps_drone2
import ps_drone3

import sys

if sys.version_info[0] < 3:
    ps_drone = ps_drone2
else:
    ps_drone = ps_drone3