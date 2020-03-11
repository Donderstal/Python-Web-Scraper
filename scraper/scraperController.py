import sys
import scrapers
import scraperHelper as util
import scrapedData

Data = scrapedData.DataClass()
scrapers.scrapeAll( Data )

for City in Data.Data["Antikraak"] :
    for key, value in City.items() :
        City[key] = util.getCleanString( value )

print(Data.Data)

# How do we want to receive our structured data?
# We might want to render it in a webpage or email
# this makes json an easy format.

# We can judge a housing ad's relevance on the following factors:
# 1. Location
# 2. Price
# 3. Title
# 4. Picture ( ? )
# 5. Type ( antikraak of tijdelijk huren )

# Next to that, we also want the following info te be accessible for us:
# 6. URL to specific ad on website
# 7. Which housing corporation is posting the ad
# 8. Description ( ? )

# JSON : {
# 
#   Antikraak : {
#       City1 : {
#           Title: string
#           Price: string
#           Link: string
#           Picture: ( ? )
#           Corporation : string
#       },
#       City2: ...
#   },
# 
#   TijdelijkHuur : {
#       City1 : {
#           Title: string
#           Price: string
#           Link: string
#           Picture: ( ? )
#           Corporation : string
#       },
#       City2: ...
#   }
# 
# }