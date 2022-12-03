# -*- coding: utf-8 -*-
# version: python 3.5

import sys
import re
from file_util import *

injection_js = r'''document.querySelectorAll('a').forEach(ele => {
  ele.onclick = (e) => {
    const href = ele.getAttribute('href')
    const audioFormat = /\.(wav|mp3|aac|flac|ogg)$/
    if (audioFormat.test(href)) {
      e.preventDefault()
      new Audio(href).play()
    }
  }
})'''

def get_definition_mdx(word, builder):
    """根据关键字得到MDX词典的解释"""
    content = builder.mdx_lookup(word)
    if len(content) < 1:
        return "It seems that there is no such word"
    pattern = re.compile(r"@@@LINK=([\w\s]*)")
    rst = pattern.match(content[0])
    if rst is not None:
        link = rst.group(1).strip()
        content = builder.mdx_lookup(link)
    str_content = ""
    if len(content) > 0:
        for c in content:
            str_content += c.replace("\r\n","").replace("entry:/","")

    injection = []
    injection_html = ''
    output_html = ''

    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        # base_path = sys._MEIPASS
        base_path = os.path.dirname(sys.executable)
    except Exception:
        base_path = os.path.abspath(".")
            
    resource_path = os.path.join(base_path, 'mdx')

    file_util_get_files(resource_path, injection)

    for p in injection:
        if file_util_is_ext(p, 'html'):
            injection_html += file_util_read_text(p)

    output_html = str_content + injection_html
    output_html = output_html.replace('sound://', '')
    output_html = output_html + f'<script>{injection_js}</script>'
    return [output_html.encode('utf-8')]

def get_definition_mdd(word, builder):
    """根据关键字得到MDX词典的媒体"""
    word = word.replace("/","\\")
    content = builder.mdd_lookup(word)
    if len(content) > 0:
        return [content[0]]
    else:
        return []
