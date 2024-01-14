tes tar from web_static files and stores
it in the folder versions
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """packs the webstatic files"""
    try:
        if not os.path.exists('versions'):
            local('mkdir versions')
        local("tar -czvf versions/web_static_{}.tgz ./web_static/".
              format(datetime.now().strftime('%Y%m%d%H%M%S')))
    except Exception as e:
        return None
    return ("web_static_{}.tgz".
            format(datetime.now().strftime('%Y%m%d%H%M%S')))
