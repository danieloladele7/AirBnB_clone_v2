#!/usr/bin/python3
'''Fabric script to generate .tgz archive meeting this requirements:
- All files in the folder web_static must be added.
- All archives must be stored in the folder versions (create if doesn't exist)
- Archive name - web_static_<year><month><day><hour><minute><second>.tgz
- return archive path if successful. Otherwise, it should return None
'''

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None
