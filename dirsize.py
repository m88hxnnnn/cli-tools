#!/usr/bin/env python3
# disk usage of top dirs
import os
for d in os.listdir("."):
    if os.path.isdir(d): print(d)
