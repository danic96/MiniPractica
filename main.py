#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Client web per www.udl.cat

@author: dcv4@alumnes.udl.cat
'''

import urllib2
from bs4 import BeautifulSoup


class Client(object):

    def get_web(self, page):
        '''baixarse la web'''
        f = urllib2.urlopen(page)
        html = f.read()
        f.close()
        return html

    def search_text(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        elements = soup.find_all("div", "dotd-title")
        resultats = []
        # print len(elements)
        for element in elements:
            title = element.text
        resultats.append(title)
        print resultats
        return title

    def main(self):
        web = self.get_web("https://www.packtpub.com/packt/offers/free-learning")
        # TODO: buscar el text
        resultat = self.search_text(web)
        # FIXME: impreimir resultat
        print resultat


if __name__ == "__main__":
    client = Client()
    client.main()
