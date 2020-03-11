class DataClass: 
    Data = {
        "Antikraak": [],
        "TijdelijkeHuur": []
    }

    def PushCity( self, city ):
        self.Data["Antikraak"].append( city )
        print( self.Data )