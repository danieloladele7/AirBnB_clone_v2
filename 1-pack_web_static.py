#!/usr/bin/python3
'''Fabric script to generate .tgz archive meeting this requirements:
- All files in the folder web_static must be added.
- All archives must be stored in the folder versions (create if doesn't exist)
- Archive name - web_static_<year><month><day><hour><minute><second>.tgz
- return archive path if successful. Otherwise, it should return None
'''

import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
