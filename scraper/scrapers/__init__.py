import scrapers.Interveste as Interveste
import scrapers.VPS as VPS
import scrapers.Vastgoedbeschermer as Vastgoedbeschermer

# Write 'master function' here
# Which will call all scrape functions in folder

def scrapeAll( Data ) : 
    Interveste.scrape( Data )
    Vastgoedbeschermer.scrape( Data )