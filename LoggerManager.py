
import logging


class NewLogger:

	def __init__(self, source,log_name):
		self.source =source
		logger = logging.getLogger(source)
		logging.basicConfig(format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', filename=log_name, filemode='w', level=logging.DEBUG)
		logger.info( ' : Starting new task: ')

	


