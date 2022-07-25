import logging
import logging.config

class FileReader:
    logging.config.fileConfig("resources/configs/logging.conf")
    logger = logging.getLogger("Ingest")
    def __init__(self, fileType):
        self.logger.info("I am within file reader Constructor")
        self.file_type = fileType
    def read_file(self):
        self.logger.debug("Ingesting (reading) a " + self.file_type + " file")