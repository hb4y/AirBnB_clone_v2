#!/usr/bin/python3
"""
Fabric script that contents the "do_clean" function and controls the whole
process.
"""
from fabric.api import *
from datetime import datetime
from fabric.operations import run, put, sudo
import os

env.user = 'ubuntu'
env.hosts = ['1240-web-01', '1240-web-02']
ctrl_path = None


def do_pack():
    """
    Function that generates a .tgz archive from the contents of the web_static
    folder of the AirBnB Clone repo
    """
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file_name = "versions/web_static_{}.tgz".format(time)
    try:
        local("mkdir -p ./versions")
        local("tar -zcvf {} ./web_static".format(file_name))
        return file_name
    except:
        return None


def do_deploy(archive_path):
    """
    Function that distributes an archive to the web servers.

    Args:
        archive_path (str): The file for distribution.

    Returns:
        False if something goes wrong
        True if everything is ok
    """
    if os.path.isfile(archive_path) is False:
        return False
    try:
        archive = archive_path.split("/")[-1]
        path = "/data/web_static/releases"
        put("{}".format(archive_path), "/tmp/{}".format(archive))
        folder = archive.split(".")
        run("mkdir -p {}/{}/".format(path, folder[0]))
        new_archive = '.'.join(folder)
        run("tar -xzf /tmp/{} -C {}/{}/"
            .format(new_archive, path, folder[0]))
        run("rm /tmp/{}".format(archive))
        run("mv {}/{}/web_static/* {}/{}/"
            .format(path, folder[0], path, folder[0]))
        run("rm -rf {}/{}/web_static".format(path, folder[0]))
        run("rm -rf /data/web_static/current")
        run("ln -sf {}/{} /data/web_static/current"
            .format(path, folder[0]))
        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """
    This function creates and distributes an archive to the web servers, using
    the function deploy and importing the do_pack and do_deploy modules.

    Returns:
        True if process runs succesfully
        False if something goes wrong
    """
    global ctrl_path

    if ctrl_path is None:
        ctrl_path = do_pack()
    if ctrl_path is None:
        return False
    return do_deploy(ctrl_path)


def do_clean(number=0):
    """
    Function that deletes out-of-date archives.

    Args:
        number (int): Amount of files that to have to remain in the directory.
    """
    if number == '0':
        number = 1
    else:
        number = int(number)

    """ local erase compressed files in the dir """
    local("ls -1v versions/web* | head -n -{} | xargs rm -rf".format(number))

    """ remote erase the dirs """
    run("ls -dv1 /data/web_static/releases/web* | \
        head -n -{} | xargs rm -rf".format(number))
