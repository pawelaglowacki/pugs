# -*- coding: utf-8 -*-
import urllib2
import random
from bs4 import BeautifulSoup

def index(): return dict(message="hello")

def pugs():

    pugs = []

    while(len(pugs) is 0):
        try:
            day = random.randint(1,30)
            month =random.randint(1,12)
            pugs_url = "http://pugs.tumblr.com/day/2016/{}/{}".format(month, day)
            page = urllib2.urlopen(pugs_url).read()

            soup = BeautifulSoup(page)
            soup.prettify()

            pugs = pugs + soup.findAll(attrs={'class' : 'photo'})
        except:
            pass

    pug = random.sample(pugs, 1)[0]["src"]
    return locals()
