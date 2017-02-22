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

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from scrapy.utils.project import get_project_settings
from os import makedirs
from os.path import join, isdir
from cgb_prj import html_util

# settings = get_project_settings()


class CgbSpider(scrapy.Spider):
    # settings = get_project_settings()
    name = "cgb"
    # allowed_domains = [settings.get('DOMAIN')]
    # start_urls = [settings.get('URL')]


    def __init__(self, start_urls=[], content_xpath="",  *args, **kwargs):
        super(CgbSpider, self).__init__(*args, **kwargs)
        self.settings = get_project_settings()
        if 'start_urls' in kwargs:
            self.start_urls = kwargs.pop('start_urls').split(',')
        elif start_urls:
            self.start_urls = start_urls
        else:
            self.start_urls = [self.settings.get('URL')]
        self.content_xpath = content_xpath
        self.logger.debug('self.start_urls %s', self.start_urls)
        if not isdir(self.settings.get('HTML_PATH')):
            makedirs(self.settings.get('HTML_PATH'))

    # def start_requests(self):
    #     self.logger.debug('Starting request to url %s', self.start_urls)
    #     for url in self.start_urls:
    #         self.logger.debug('Starting request to url %s', url)
    #         yield self.make_requests_from_url(url)
    #     # if there is loggin
    #     # return [scrapy.FormRequest(self.start_url,
    #     #                            formdata={'user': self.settings.get('USER'), 'pass': self.settings.get('PW')},
    #     #                            callback=self.parse)]

    def parse(self, response):
        self.logger.debug('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Parsing response %s', response)
        content = response.xpath(self.settings.get('XPATH_CONTENT')).extract_first()
        title = response.selector.xpath(self.settings.get('XPATH_TITLE')).extract_first()
        page = response.url.split("/")[-1]
        filepath = join(self.settings.get('HTML_PATH'), page)
        html = html_util.create_html_page(content, title)
        with open(filepath, 'w') as f:
            f.write(html)
        self.logger.info('Saved file %s' % filepath)

    # if the pages have internal links to follow
        extractor = LinkExtractor(allow_domains=self.allowed_domains)
        links = extractor.extract_links(response)
        for link in links:
            yield Request(
                response.urljoin(link),
                callback=self.parse,
        )
    # if the pages have a "next" link"
        next_page = response.xpath(self.settings.get('XPATH_NEXT')).extract_first()
        self.logger.debug('Next page %s.', next_page)
        if next_page:
            yield Request(
                response.urljoin(next_page),
                callback=self.parse,
            )
        else:
            self.logger.debug('No next page.')
