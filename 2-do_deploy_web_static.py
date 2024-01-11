#!/usr/bin/python3
'''
fabric script to distribute an archive to web servers
----NEEDS TO REVISIT SCRIPT
'''

import os
from datetime import datetime
from fabric.api import env, local, put, run, runs_once


env.hosts = ['3.238.119.65', '3.236.150.166']


@runs_once
def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder.
    Returns:
        If the archive is successfully created - the path of the archive.
        Otherwise - None.
    """
    try:
        if not os.path.isdir("versions"):
            os.mkdir("versions")
        cur_time = datetime.now()
        output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            cur_time.year,
            cur_time.month,
            cur_time.day,
            cur_time.hour,
            cur_time.minute,
            cur_time.second
        )
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))
        archive_size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, archive_size))
        return output
    except Exception:
        return None


def do_deploy(archive_path):
    """Deploys the static files to the host servers.
    Args:
        archive_path (str): The path to the archived static files.
    Returns:
        True if successful, False otherwise.
    """
    if not os.path.exists(archive_path):
        return False
    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        print('New version deployed!')
        return True
    except Exception:
        return False
