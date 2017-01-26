import urllib2
#from BeautifulSoup import BeautifulSoup
# or if you're using BeautifulSoup4:
from bs4 import BeautifulSoup

page = urllib2.urlopen('http://pugs.tumblr.com/').read()

soup = BeautifulSoup(page, "lxml")
soup.prettify()

pugs = soup.findAll(attrs={'class' : 'photo'})
print pugs[0]['src']
