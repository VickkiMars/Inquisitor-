import os
import sys

abs_ = os.path.abspath(os.path.dirname(__file__))

if abs_ not in sys.path:
    sys.path.append(abs_)