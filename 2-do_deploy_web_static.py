#!/usr/bin/python3
"""
Fabric script for the function deploy that distributes an archive to the web
servers.
"""
from fabric.api import *
from fabric.operations import run, put, sudo
import os
env.hosts = ['1146-web-01', '1146-web-02']


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
