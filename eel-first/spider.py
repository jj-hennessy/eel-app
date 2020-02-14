import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import eel

@eel.expose
def validateLink(url):
    if(str(url).startswith('http')):
        return True
    else:
        return False

@eel.expose
def cleanLinkList(linkList):
    newList = list()
    for link in linkList:
        if(validateLink(link)):
            newList.append(link)

    return newList

eel.init('web', {
    '_js_result_timeout': 100000
})

@eel.expose
def getNumLinks(url):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # makes a list of URLs present on a given page
    tags = soup('a')
    urlList = list()
    for tag in tags:
        link = tag.get('href')
        urlList.append(link)

    newLinkList = cleanLinkList(urlList)

    allLinks = list()
    for url in newLinkList:
        try:
            # take in a link, then add
            html = urllib.request.urlopen(url, context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            newLinks = soup('a')
            for tag in newLinks:
                link = tag.get('href')
                if(validateLink(link)):
                    allLinks.append(link)
        except:
            print("An exception occurred")

    return len(allLinks)

eel.start('gui.html')
