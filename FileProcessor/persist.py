class PersistData:
    def __init__(self,dbType):
        print("I am within the file storage constructor")
        self.db_type = dbType
    def store_data(self):
        print("Now storing data to a " + self.db_type + " database")