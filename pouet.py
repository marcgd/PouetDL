#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import urllib
from bs4 import BeautifulSoup
from config import download
from db import Db
from platforms import platforms


class Pouet(object):

    prods = []
    prods_fail = []

    root_url = 'http://www.pouet.net/'
    res_url  = root_url+'prodlist.php?platform[]=%s&order=added&page=%s'
    info_url = root_url+'prod.php?which=%s'


    def __init__(self):
        self.db = Db(True)


    def get(self, platform=None, num_pages=1):
        if not platform:
            print '\n[Choose a platform] \n\n %s' % platforms
            self.db.disconnect()
            return False

        self.platform = platform[0]
        self.local_path = '%s/down/%s/' % (os.getcwd(), self.platform.replace('/', '_'))

        self.check_dest_dir()
        print '\nLooking for %s productions!' % self.platform
        self.fetch_result_list(num_pages)
        if self.prods_fail:
            print 'Failed to download %i prods: \n )_:' % len(self.prods_fail)
        self.db.disconnect()


    def fetch_result_list(self, num_pages):
        for page in range(1, int(num_pages)+1):
            print '\n[Page: %i]' % page
            self.call_pouet(self.res_url % (self.platform, str(page)))
            self.parse_result_list()
        print '\n[Got %i New prods] \n' % len(self.prods)


    def check_dest_dir(self):
        if not os.path.exists(self.local_path):
            os.makedirs(self.local_path)


    def call_pouet(self, url):
        print 'Fetching: %s' % url
        self.p_results = urllib.urlopen(url).read()


    def download_prod(self, url):
        filename = self.local_path + url.split('/')[-1]
        print 'Downloading %s \n   |-> %s' % (url, filename)
        try:
            urllib.urlretrieve(url, filename)
            self.prod['downloaded'] = '1'
        except Exception:
            print 'Download failed!: %s' % url
            self.prods_fail.append(self.prod)


    def parse_prod_info(self):
        print '---\n>> New production! %s' % self.prod['name']
        soup = BeautifulSoup(self.p_results, 'html.parser')
        image = soup.find("td", id="screenshot")
        if len(image) == 2:
            self.prod['image'] = image.img["src"].strip()
        self.prod['dw_link'] = self.parse_dw_link(soup.find("a", id="mainDownloadLink")["href"])


    def parse_result_list(self):
        soup = BeautifulSoup(self.p_results, 'html.parser')
        p_prods = soup.find("table", id="pouetbox_prodlist").find_all('tr', attrs={'class': None})

        for p_prod in p_prods:
            details = p_prod.find_all("td")
            if not details[0].attrs.get('class'):
                prod_id = int(details[0].select('.prod')[0].a["href"].split('=')[-1])
                link = self.info_url % str(prod_id)
                if self.db.get_prod_by_id(prod_id):
                    print '* You already have %s' % link
                    continue
                self.prod = self.build_prod(prod_id, link, details, self.platform)
                self.call_pouet(self.info_url % self.prod['id'])
                self.parse_prod_info()
                if download:
                    self.download_prod(self.prod.get("dw_link"))
                self.db.insert_prod(self.prod)
                self.prods.append(self.prod)
            else:
                pass


    @staticmethod
    def parse_dw_link(link):
        return link.replace('scene.org/view', 'scene.org/get')


    @staticmethod
    def build_prod(prod_id, link, details, platform):
        return {
            "id"        : prod_id,
            "link"      : link,
            "name"      : details[0].select('.prod')[0].get_text().strip(),
            "ptype"     : details[0].select('.typeiconlist')[0].get_text().strip(),
            "platform"  : platform,
            "group"     : details[1].get_text().strip(),
            "party"     : details[2].get_text().strip(),
            "date"      : details[3].get_text().strip(),
            "upvotes"   : details[5].get_text().strip(),
            "pigvotes"  : details[6].get_text().strip(),
            "downvotes" : details[7].get_text().strip(),
            "average"   : details[8].get_text().strip()
        }


if __name__ == '__main__':

    pouet = Pouet()

    sel_platforms = [p for p in platforms if sys.argv[-1].lower() in p.lower()]

    pouet.get(platform=sel_platforms, num_pages=1)
