from bs4 import BeautifulSoup
from urllib.request import urlopen

corp = "Interveste"

def scrape( Data ) :
    Interveste_Tijdelijk = BeautifulSoup( urlopen('http://interveste.nl/woonruimte/tijdelijk-huren').read())
    Interveste_Antikraak = BeautifulSoup( urlopen('http://interveste.nl/woonruimte/antikraak').read())

    for niet_beschikbaar in Interveste_Tijdelijk.findAll("div", { "class": "grijstinten" }):
        niet_beschikbaar.decompose( )
    for niet_beschikbaar in Interveste_Antikraak.findAll("div", { "class": "grijstinten" }):
        niet_beschikbaar.decompose( )

    Int_Tdl_Aanbod = Interveste_Tijdelijk.findAll("div", { "class": "aanbod-frame" })
    Int_Ant_Aanbod = Interveste_Antikraak.findAll("div", { "class": "aanbod-frame" })

    for htmlEl in Int_Tdl_Aanbod :
        pushIntervesteAd( htmlEl, "T", Data )
 
    for htmlEl in Int_Ant_Aanbod :
        pushIntervesteAd( htmlEl, "A", Data )

def pushIntervesteAd( htmlEl, Type, Data ) :
        ad  = {
            "price"   : htmlEl.find( "div", { "class": "ribbon" } ).find( "span" ).getText(),
            "url"     : htmlEl.find( "a", { "class": "aspect" } )['href'],
            "corp"    : corp
        }

        htmlEl.find( "h2", { "class": "aanbod-blok" } ).find( "br" ).decompose()
        htmlEl.find( "h2", { "class": "aanbod-blok" } ).find( "span" ).decompose()
        ad["city"]    : htmlEl.find( "h2", { "class": "aanbod-blok" } ).getText()

        htmlEl.find( "h2", { "class": "aanbod-blok" } ).decompose()
        ad["title"] = htmlEl.find( "div", { "class": "aanbod-frame-content" } ).getText()

        Data.PushAd( ad, type )
