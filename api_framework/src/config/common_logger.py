import logging

class CommonLogger():

  def logger(self, loglevel):
      #level = logging.DEBUG,

     logger = logging.getLogger()
     logger.setLevel(loglevel)
     logging.basicConfig(filename="C:\\Users\\saurabhd\\PycharmProjects\\API_Automation_Practice\\api_framework\\src\\utilities\\app.log",
                                filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

     return logger
# logging.debug("This is debug message")
# logging.info("This is debug message")
# logging.warning("This is debug message")
# logging.error("This is debug message")
# logging.critical("This is debug message")