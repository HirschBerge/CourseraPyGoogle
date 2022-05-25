#!/usr/bin/env python3

import subprocess
import sys

fil = sys.argv[1]


def renameJane():
    with open(fil, "r") as f:
        lines = f.readlines()
        line1 = [x.strip() for x in lines]
        line2 = [i.replace("jane", "jdoe") for i in line1]
        [[subprocess.run(['mv', x, y]) for x in line1] for y in line2]


renameJane()
