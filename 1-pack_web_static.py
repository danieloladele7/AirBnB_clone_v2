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
    """
        generates a .tgz archine from contents of web_static
    """
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file_name = "versions/web_static_{}.tgz".format(time)
    try:
        local("mkdir -p ./versions")
        local("tar --create --verbose -z --file={} ./web_static"
              .format(file_name))
        return file_name
    except:
        return None
