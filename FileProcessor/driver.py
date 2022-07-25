import ingest
import persist
import logging
import logging.config

print("This is my driver program\n")

class DriverProgram:
    logging.config.fileConfig("resources/configs/logging.conf")
    def __init__(self,fileType):
        logging.debug("I am within the constructor")
        self.file_type = fileType
    def my_function(self):
        logging.debug("Inside my_function. Initiating processing of a "+self.file_type+" file")
        # Create Class instances
        reader = ingest.FileReader(self.file_type)
        writer = persist.PersistData("postgres")

        # Call instances' functions
        reader.read_file()
        writer.store_data()


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('This is the main method\n')
    print_hi('PyCharm\n')
    driver = DriverProgram("csv")
    driver.my_function()


