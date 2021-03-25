import os
import sys

test_path = os.path.dirname(os.path.abspath(__file__))
base_path = os.path.dirname(test_path)
sys.path.append(test_path)
sys.path.append(base_path)
