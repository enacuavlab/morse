import importlib
import os
import sys

# test if pprzlink module can be found
if importlib.util.find_spec("pprzlink") is None:
    # if not found but PAPARAZZI_HOME is defined,
    # load pprzlink from paparazzi installed version
    PPRZ_HOME = os.getenv("PAPARAZZI_HOME")
    if PPRZ_HOME is not None:
        # append pprzlink to sys path
        sys.path.append(PPRZ_HOME + "/var/lib/python")

