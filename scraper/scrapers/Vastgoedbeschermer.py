from bs4 import BeautifulSoup
from urllib.request import urlopen

corp = "Vastgoedbeschermer"

def scrape( Data ) :
    Doc = BeautifulSoup( urlopen('https://vastgoedbeschermer.nl/ruimte/woonruimte/').read(), "html" )
    allAds = Doc.findAll( "section", { "class": "status-1" } )

    for htmlEl in allAds:
        url = 'https://vastgoedbeschermer.nl/' + htmlEl.find("h2").find("a")["href"]
        ProductDoc = BeautifulSoup( urlopen(url).read(), "html" )
        typeOfContract = ProductDoc.find( "div", { "class": "container-if" }).find( "aside", { "id": "object-features" } ).find( "tr", {"class": "contract"} ).find("span").getText()

        print( ProductDoc.find( "div", { "class": "container-if" }).find( "aside", { "id": "object-features" } ).find( "tr", {"class": "contract"} ).find("span").getText() )

        if "Bruikleen" in typeOfContract:
            pushVastgoedAd( htmlEl, "A", Data, url )
        else:
            pushVastgoedAd( htmlEl, "T", Data, url )

def pushVastgoedAd( htmlEl, Type, Data, url ) :
        ad  = {
            "price"   : htmlEl.find("ul").find("span", {"class": "tooltip-title"}).getText(),
            "url"     : url,
            "corp"    : corp,
            "city"    : htmlEl.find("h2").find("a").getText(),
            "title"   : htmlEl.find("p", {"class": "lead-in"}).getText() + htmlEl.find("h2").find("a").getText()
        }

        Data.PushAd( ad, type )
