#!/usr/bin/env python3

import os

modules = [
        "requests"
        ]

for module in modules:
    os.system(f"python3 -m pip install {module}")
