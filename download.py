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
    return 'http://www.meteo.pl/um/metco/mgram_pict.php?ntype=0u&fdate='+_timestamp()+'&row=436&col=181&lang=pl'

def _timestamp():
    today = datetime.today()
    hour  = '00' if today.hour < 12 else '12'
    return today.strftime('%Y%m%d') + hour

if __name__ == '__main__':
    stdout.write('{}\n'.format(download()))
