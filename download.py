#! /usr/bin/env python

from urllib import urlretrieve
from datetime import datetime
from tempfile import gettempdir
from os.path import join
from sys import stdout
from argparse import ArgumentParser
from subprocess import call

_filename = 'meteo.jpg'

def download(path=join(gettempdir(), _filename)):
    urlretrieve(_url(), path)
    return path

def _url():
    return 'http://www.meteo.pl/um/metco/mgram_pict.php?ntype=0u&fdate='+_timestamp()+'&row=436&col=181&lang=pl'

def _timestamp():
    today = datetime.today()
    hour  = '00'
    return today.strftime('%Y%m%d') + hour


def parse_args():
    parser = ArgumentParser(description='Download meteogram')
    parser.add_argument('-d', action='count', dest='debug', help='debug; dd more debug')
    args = parser.parse_args()
    return args

def handle_debug(path, level):
    if level >= 1:
        print _url()
    if level >= 2:
        call(['open', path])

if __name__ == '__main__':
    args = parse_args()
    path = download()
    handle_debug(path=path, level=args.debug)
    stdout.write('{}\n'.format(path))
