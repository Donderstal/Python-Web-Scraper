from bs4 import BeautifulSoup
from urllib.request import urlopen

def scrapeCamelot( ) :
    Camelot = BeautifulSoup( urlopen('https://nl.cameloteurope.com/properties/rooms/Nederland').read())
    Camelot_Aanbod = Camelot.findAll("li", { "itemtype" : "https://schema.org/RealEstateAgent" } )
    print(Camelot_Aanbod)