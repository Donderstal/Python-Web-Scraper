class DataClass: 
    Data = {
        "Antikraak": [],
        "TijdelijkeHuur": []
    }

    def PushAd( self, ad, type ):
        type == "A" if self.Data["Antikraak"].append( ad ) else self.Data["TijdelijkeHuur"].append( ad )