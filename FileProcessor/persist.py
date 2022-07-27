import logging.config
import configparser
import psycopg2

class PersistData:
    logging.config.fileConfig("resources/configs/logging.conf")
    logger = logging.getLogger("Persist")
    config = configparser.ConfigParser()
    config.read("resources/fileprocessor.ini")

    def __init__(self,dbType):
        self.logger.debug("I am within the file storage constructor")
        self.db_type = dbType
    def store_data(self):
        #var1 = 100 / 0
        try:
            target_table = self.config.get("DATABASE_CONFIGS","PG_TABLE")
            self.logger.debug("This is the target table"+target_table)
            self.logger.debug("Now storing data to a " + self.db_type + " database")
        except Exception as exp:
            self.logger.error("An error has occured: " + str(exp))