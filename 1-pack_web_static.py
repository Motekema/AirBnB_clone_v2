#!/usr/bin/python3
'''Fabric script generate .tgz archive'''

from fabric.api import local
from datetime import datetime

from fabric.decorators import runs_once

@runs_once
def do_pack():
    '''generates .tgz archive from contents of web_static folder'''
    try:
        local("mkdir -p versions")
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        path = "versions/web_static_{}.tgz".format(timestamp)
        local("tar -cvzf {} web_static".format(path))
        return path
    except:
        return None
