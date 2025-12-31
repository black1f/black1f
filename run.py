#!/usr/bin/env python3
import sys
import os

# Go to home directory
os.chdir(os.path.expanduser('~'))
sys.path.insert(0, '.')

try:
    import ss
    ss.main()
except:
    # Run original ss.py
    exec(open('/storage/emulated/0/CP/ss.py').read())
