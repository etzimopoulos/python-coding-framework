import logging
import logging.config

class PersistData:
    logging.config.fileConfig("resources/configs/logging.conf")
    logger = logging.getLogger("Persist")
    def __init__(self,dbType):
        self.logger.debug("I am within the file storage constructor")
        self.db_type = dbType
    def store_data(self):
        #var1 = 100 / 0
        try:
            self.logger.debug("Now storing data to a " + self.db_type + " database")
            var1 = 100/0
        except Exception as exp:
            self.logger.error("An error has occured: " + str(exp))