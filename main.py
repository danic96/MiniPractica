#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Client web per www.udl.cat

@author: dcv4@alumnes.udl.cat
'''

import urllib2
from bs4 import BeautifulSoup as bs

url = "https://www.packtpub.com/packt/offers/free-learning/"


class Client(object):
    """classe per obrir la pagina, buscar el text i imprimirlo."""

    def get_web(self, page):
        """Baixarse la web."""
        """Comprovar que no hi ha errors al demanar el codi HTML"""
        try:
            f = urllib2.urlopen(page)
        except urllib2.HTTPError as e:
            print "Error " + str(e.code)
            return None

        html = f.read()
        f.close()
        return html

    def search_text(self, html):
        """Buscar el text dins del codi html."""
        soup = bs(html, 'html.parser')
        elements = soup.find_all("div", "dotd-title")
        titles = []
        for element in elements:
            title = element.text
            # Com que el text extret de la paguina web conte salts de linea i
            # espais cal eliminarlos
            title = title.replace('\n', '').replace('\t', '')
            titles.append(title)
        return titles

    def print_resultat(self, resultats):
        """Imprimim el resultat."""
        if len(resultats) == 0:
            print "No s'ha trobat cap coincidencia!!!"
        else:
            for resultat in resultats:
                print resultat

    def main(self):
        """Seguir."""
        web = self.get_web(url)
        if web is not None:
            resultat = self.search_text(web)
            self.print_resultat(resultat)


if __name__ == "__main__":
    client = Client()
    client.main()
