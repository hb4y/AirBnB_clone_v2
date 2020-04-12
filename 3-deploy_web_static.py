#!/usr/bin/python3
"""
Fabric script that contents the "deploy" function and controls the whole
process.
"""
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy
from fabric.api import *
from fabric.operations import run, put, sudo
import os
env.hosts = ['1240-web-01', '1240-web-02']
ctrl_path = None

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
