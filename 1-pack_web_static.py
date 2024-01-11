#!/usr/bin/python3
"creates tar from web_static files"
from fabric.api import *
from datetime import datetime
import os


def do_pack():
    try:
        if not os.path.exists('versions'):
            local('mkdir versions')
        local("tar -czvf versions/web_static_{}.tgz ./web_static/*".
              format(datetime.now().strftime('%Y%m%d%H%M%S')))

    except Exception:
        return None
    return ("web_static_{}".format(datetime.now().strftime('%Y%m%d%H%M%S')))
