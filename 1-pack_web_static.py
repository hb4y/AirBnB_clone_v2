#!/usr/bin/python3
"""
Fabric script for the do_pack function that generates a .tgz archive from the
contents of the web_static folder.
"""
from fabric.api import local
from datetime import datetime


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
