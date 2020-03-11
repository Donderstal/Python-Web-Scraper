import re
import string

def getCleanString( inputString ) :
    returnValue = re.sub( "[^a-zA-Z0-9-_ .,:;/]+", "", inputString )
    return returnValue