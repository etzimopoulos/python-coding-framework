class FileReader:
    def __init__(self, fileType):
        print("I am within file reader Constructor")
        self.file_type = fileType
    def read_file(self):
        print("Ingesting (reading) a " + self.file_type + " file")