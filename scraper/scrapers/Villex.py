from bs4 import BeautifulSoup
from urllib.request import urlopen

corp = "Villex"

def scrape( Data ) :
    Tijdelijk_Huren_Doc = BeautifulSoup( urlopen('https://www.villex.nl/zoek/uitgebreid/type+1/kenmerken+2/90+per+pagina').read(), "html" )
    Tijdelijk_Huren_Ads = Tijdelijk_Huren_Doc.findAll( "div", { "class": "fourcol" } )

    Antikraak_Huren_Doc = BeautifulSoup( urlopen('https://www.villex.nl/zoek/uitgebreid/type+1/kenmerken+1/90+per+pagina').read(), "html" )
    Antikraak_Huren_Ads = Antikraak_Huren_Doc.findAll( "div", { "class": "fourcol" } )

    for htmlEl in Tijdelijk_Huren_Ads:
        pushVillexAd( htmlEl, "T", Data )

    for htmlEl in Antikraak_Huren_Ads:
        pushVillexAd( htmlEl, "A", Data )

def pushVillexAd( htmlEl, Type, Data ) :
    adresDiv = htmlEl.find("div", {"class": "recent_adres"})
    button = htmlEl.find("div", { "class": "recent_kleurknop-groen" })

    if button is None:
        button = htmlEl.find("div", { "class": "recent_kleurknop-blauw" })

    ad  = {
        "price"   : htmlEl.find("tr").find("td", {"class": "recent_detailtekst"}).getText(),
        "url"     : "https://www.villex.nl" + htmlEl.find("div", {"class": "recent_objectbutton"}).find("a")["href"],
        "corp"    : corp,
        "city"    : adresDiv.find("div").getText(),
        "title"   : adresDiv.find("strong").getText() + ", " + button.getText()
    }

    print( button.getText() )

    Data.PushAd( ad, type )
