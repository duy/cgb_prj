#!/usr/bin/env python
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

import argparse
import logging
import os
# os.environ.setdefault('SCRAPY_SETTINGS_MODULE', 'cgb_prj.settings')
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging

from cgb_prj.spiders import cgb

# logger = logging.getLogger(__name__)


def main():
    os.environ['SCRAPY_SETTINGS_MODULE'] = 'cgb_prj.settings'
    settings = get_project_settings()
    logging.basicConfig(level=settings.get('LOG_LEVEL'),
                        format=settings.get('LOG_FORMAT'),
                        datefmt=settings.get('LOG_DATEFORMAT'))
    parser = argparse.ArgumentParser()
    parser.add_argument('-d',
                        '--debug',
                        help='Set logging level to debug',
                        action='store_true')
    configure_logging()
    # process = CrawlerProcess(get_project_settings())
    process = CrawlerProcess(settings)
    process.crawl('cgb')
    process.start()
    process.stop()


if __name__ == '__main__':
    main()
