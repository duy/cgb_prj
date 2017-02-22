# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:expandtab

# Copyright 2017 duy <duy@systemli.org>

# This file is part of cgb_prj.
#
# cgb_prj is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# cgb_prj is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with cgb_prj.  If not, see <http://www.gnu.org/licenses/>.
""""""

import logging
from lxml import etree as ET

HTML_WRAPPER = """<!DOCTYPE html>
<html>
  <head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  </head>
  <body>
  </body>
</html>"""

logger = logging.getLogger(__name__)


def create_html_page(content, title):
    html_page = ET.fromstring(HTML_WRAPPER)
    head, body = list(html_page)
    head.append(ET.fromstring(title))
    # remove trailing whitespaces
    content_str = "\n".join([line.rstrip() for line in
                             content.encode('utf-8').split('\n')])
    parser = ET.XMLParser(recover=True, encoding='utf-8')
    content_et = ET.fromstring(content_str, parser=parser)
    body.append(content_et)
    return ET.tostring(html_page, encoding='utf-8', pretty_print=True)
