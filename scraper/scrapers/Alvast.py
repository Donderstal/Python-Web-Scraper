from bs4 import BeautifulSoup
from urllib.request import urlopen

corp = "Alvast"

def scrape( Data ) :
    i = 0
    for i in range(10):
        i += 1
        Alvast_Page = BeautifulSoup( urlopen('https://alvast.nl/tijdelijke-woonruimte/?pidx=' + str(i) ).read(), "html" )
        activeButton = Alvast_Page.find("ul", { "id": "filter-paging"} ).find('li', { "class": "active" })

        if activeButton is None:
            break
        else:
            readAlvastPage( Alvast_Page, Data )

def readAlvastPage( Alvast_Page, Data ) :
    rows = Alvast_Page.findAll( "div", { "class": "wpb_row" } )
    for row in rows:
        cols = row.findAll( "div", { "class": "wpb_column" } )
        for htmlEl in cols:
            pushAlvastAd( htmlEl, "T", Data )

def pushAlvastAd( htmlEl, Type, Data ) :
    ad  = {
        "price"   : htmlEl.findAll("span")[0].getText(),
        "url"     : "https://alvast.nl/tijdelijke-woonruimte/" + htmlEl.find("a")["href"],
        "corp"    : corp,
        "city"    : htmlEl.find("div", { "class": "title"}).getText(),
        "title"   : htmlEl.find("div", { "class": "grid-short-description" }).getText()
    }

    Data.PushAd( ad, type )
