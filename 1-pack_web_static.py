#!/usr/bin/python3
'''Fabric script to generate .tgz archive meeting this requirements:
- All files in the folder web_static must be added.
- All archives must be stored in the folder versions (create if doesn't exist)
- Archive name - web_static_<year><month><day><hour><minute><second>.tgz
- return archive path if successful. Otherwise, it should return None
'''

from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    try:
        local("mkdir -p versions")
        now = datetime.now()
        file_name = "web_static_{}{}{}{}{}{}.tgz".format(now.year,
                                                         now.month,
                                                         now.day,
                                                         now.hour,
                                                         now.minute,
                                                         now.second)
        path = "versions/{}".format(file_name)
        local("tar -cvzf {} web_static".format(path))
        return path
    except Exception:
        return None
