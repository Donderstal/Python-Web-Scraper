from bs4 import BeautifulSoup
from urllib.request import urlopen

def scrapeInterveste( ) :
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
 
    for elements in Int_Ant_Aanbod :
        Lokatie = elements.find("h2", { "class": "aanbod-blok" }).getText()
        Prijs   = elements.find("div", { "class": "ribbon" }).getText()
        Url     = elements.find("a", { "class": "aspect" })['href']

def scrapeCamelot( ) :
    Camelot = BeautifulSoup( urlopen('https://nl.cameloteurope.com/properties/rooms/Nederland').read())
    Camelot_Aanbod = Camelot.findAll("li", { "itemtype" : "https://schema.org/RealEstateAgent" } )
    print(Camelot_Aanbod)

scrapeCamelot()