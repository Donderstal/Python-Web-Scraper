from bs4 import BeautifulSoup
from urllib.request import urlopen

def scrape( ) :
    Interveste_Tijdelijk = BeautifulSoup( urlopen('http://interveste.nl/woonruimte/tijdelijk-huren').read())
    Interveste_Antikraak = BeautifulSoup( urlopen('http://interveste.nl/woonruimte/antikraak').read())

    for niet_beschikbaar in Interveste_Tijdelijk.findAll("div", { "class": "grijstinten" }):
        niet_beschikbaar.decompose( )
    for niet_beschikbaar in Interveste_Antikraak.findAll("div", { "class": "grijstinten" }):
        niet_beschikbaar.decompose( )

    Int_Tdl_Aanbod = Interveste_Tijdelijk.findAll("div", { "class": "aanbod-frame" })
    Int_Ant_Aanbod = Interveste_Antikraak.findAll("div", { "class": "aanbod-frame" })

    for elements in Int_Tdl_Aanbod :
        Lokatie = elements.find("h2", { "class": "aanbod-blok" }).getText()
        Prijs   = elements.find("div", { "class": "ribbon" }).getText()
        Url     = elements.find("a", { "class": "aspect" })['href']
        print(Lokatie, Prijs, Url)
 
    for elements in Int_Ant_Aanbod :
        Lokatie = elements.find("h2", { "class": "aanbod-blok" }).getText()
        Prijs   = elements.find("div", { "class": "ribbon" }).getText()
        Url     = elements.find("a", { "class": "aspect" })['href']
        print(Lokatie, Prijs, Url)
