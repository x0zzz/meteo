#! /usr/bin/env python

from urllib import urlretrieve
from datetime import datetime
from tempfile import gettempdir
from os.path import join
from sys import stdout

_filename = 'meteo.jpg'

def download(path=join(gettempdir(), _filename)):
    urlretrieve(_url(), path)
    return path

def _url():
    return 'http://www.meteo.pl/um/metco/mgram_pict.php?ntype=0u&fdate='+_today()+'06&row=436&col=181&lang=pl'

def _today():
    return datetime.today().strftime('%Y%m%d')

if __name__ == '__main__':
    stdout.write('{}\n'.format(download()))
