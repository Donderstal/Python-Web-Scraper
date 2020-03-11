import scrapers.Alvast as Alvast
import scrapers.Interveste as Interveste
import scrapers.VPS as VPS
import scrapers.Vastgoedbeschermer as Vastgoedbeschermer
import scrapers.Villex as Villex

# Write 'master function' here
# Which will call all scrape functions in folder

def scrapeAll( Data ) : 
    Alvast.scrape( Data )
    Interveste.scrape( Data )
    Vastgoedbeschermer.scrape( Data )
    Villex.scrape( Data )