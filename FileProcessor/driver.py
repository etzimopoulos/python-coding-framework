import ingest
import persist

print("This is my driver program\n")

class DriverProgram:
    def my_function(self):
        print("Inside my function")

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('This is the main method\n')
    print_hi('PyCharm\n')
    driver = DriverProgram()
    driver.my_function()

    # Create Class instances
    reader = ingest.FileReader()
    writer = persist.PersistData()

    # Call instances' functions
    reader.read_file()
    writer.store_data()
