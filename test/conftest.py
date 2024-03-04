import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(file), os.pardir))

sys.path.insert(0, parent_dir)
