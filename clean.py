#!/usr/bin/env python3
# clean.py — limpa __pycache__ e ficheiros PLY

import os
import shutil

for root, dirs, files in os.walk('.', topdown=False):
    for d in dirs:
        if d == '__pycache__':
            full_path = os.path.join(root, d)
            shutil.rmtree(full_path, ignore_errors=True)

for fname in ('parsetab.py', 'parser.out'):
    for path in [os.path.join(root, fname) for root,_,_ in os.walk('.')]:
        if os.path.isfile(path):
            os.remove(path)
