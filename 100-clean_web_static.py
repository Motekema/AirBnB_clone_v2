#!/usr/bin/python3
'''It deletes out-of-date archives, using function do_clean'''

import os
from fabric.api import *

env.hosts = ['54.160.121.141', '100.26.243.32']


@runs_once
def do_clean(number=0):
    """It seletes out-of-date archives
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
