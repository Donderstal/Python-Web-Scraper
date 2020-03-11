from bs4 import BeautifulSoup
from urllib.request import urlopen

corp = "VPS"

def scrape( Data ) :
    VPS = BeautifulSoup( urlopen('https://www.vps-nl.com/leegstandbeheer/antikraak/aanbod').read(), "html" )
    contentWrapper = VPS.find( "div", { "class": "vps-properties" } )
    allAds = contentWrapper.findAll("div", { "class": "border-bottom" })

    for element in allAds:
        typeOfAd = element.findAll( "div", { "class": "detail-block"} ).find("div", { "class": "no-wrap" }).getText()
        
        if "woning" in typeOfAd:
            continue
        else: 
            element.decompose( )

    """ for htmlEl in Int_Tdl_Aanbod :
        pushVPSAd( htmlEl, "T", Data )
 
    for htmlEl in Int_Ant_Aanbod :
        pushVPSAd( htmlEl, "A", Data ) """

def pushVPSAd( htmlEl, Type, Data ) :
        ad  = {
            "price"   : "",
            "url"     : "",
            "corp"    : corp,
            "city"    : "",
            "title"   : ""
        }

        Data.PushAd( ad, type )
