#!/usr/bin/python3
'''Fabric script to generate .tgz archive meeting this requirements:
- All files in the folder web_static must be added.
- All archives must be stored in the folder versions (create if doesn't exist)
- Archive name - web_static_<year><month><day><hour><minute><second>.tgz
- return archive path if successful. Otherwise, it should return None
'''

from fabric.api import local
from datetime import datetime

from fabric.decorators import runs_once


@runs_once
def do_pack():
    '''generates .tgz archive from the contents of the web_static folder'''
    local("mkdir -p versions")
    path = ("versions/web_static_{}.tgz"
            .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    result = local("tar -cvzf {} web_static"
                   .format(path))

    if result.failed:
        return None
    return path
