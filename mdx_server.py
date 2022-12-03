# -*- coding: utf-8 -*-
# version: python 3.5

import threading
import re
import os
import sys

if sys.version_info < (3, 0, 0):
    import Tkinter as tk
    import tkFileDialog as filedialog
else:
    import tkinter as tk
    import tkinter.filedialog as filedialog

from wsgiref.simple_server import make_server
from file_util import *
from mdx_util import *
from mdict_query import IndexBuilder

config = {}

content_type_map = {
    'html': 'text/html; charset=utf-8',
    'js': 'application/x-javascript',
    'ico': 'image/x-icon',
    'css': 'text/css',
    'jpg': 'image/jpeg',
    'png': 'image/png',
    'gif': 'image/gif',
    'mp3': 'audio/mpeg',
    'mp4': 'audio/mp4',
    'wav': 'audio/wav',
    'spx': 'audio/ogg',
    'ogg': 'audio/ogg',
    'eot': 'font/opentype',
    'svg': 'text/xml',
    'ini': 'text/plain',
    'ttf': 'application/x-font-ttf',
    'woff': 'application/x-font-woff',
    'woff2': 'application/font-woff2',
}

try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
    #base_path = sys._MEIPASS
    base_path = os.path.dirname(sys.executable)
except Exception:
    base_path = os.path.abspath(".")
        
builder = None

def application(environ, start_response):
    path_info = environ['PATH_INFO'].encode('iso8859-1').decode('utf-8')
    print(path_info)

    if file_util_get_ext(path_info) in content_type_map:
        content_type = content_type_map.get(file_util_get_ext(path_info), 'text/html; charset=utf-8')
        start_response('200 OK', [('Content-Type', content_type)])
        return get_definition_mdd(path_info, builder)
    else:
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
        return get_definition_mdx(path_info[1:], builder)


# 新线程执行的代码
def loop():
    httpd = make_server('', config['port'], application)
    print(f"Serving HTTP on port {config['port']}...")
    httpd.serve_forever()


if __name__ == '__main__':
    with open('./config', 'r', encoding='utf-8') as f:
        for line in f:
            conf = line.strip()
            if conf != '':
                args = conf.split('=')
                if args[0] == 'port':
                    config['port'] = int(args[1])
                else:
                    conf_name = args.pop(0)
                    config[conf_name] = '='.join(args)

    if not os.path.exists(config['mdx']):
        print("Please specify a valid MDX/MDD file")
    else:
        builder = IndexBuilder(config['mdx'])
        t = threading.Thread(target=loop, args=())
        t.start()
