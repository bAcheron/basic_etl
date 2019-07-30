import inspect, os, csv
import pyodbc
import logging
from LoggerManager import NewLogger

class NewDatabaseManager:


	def __init__(self,server_name,database,logger_file_name=''):
		self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server_name+';DATABASE='+database+'')
		self.database = database
		self.logger_file_name=logger_file_name
		self.database_logger = NewLogger('DatabaseManager',self.logger_file_name)
		self.cursor = self.conn.cursor()
		
		
	def select_data(self,sql_string):
		logging.info('get_sql_data run on ' + self.database)	
		table_data = self.cursor.execute(sql_string)
		table_data =  self.cursor.fetchall()
		return table_data
		
	def insert_sql_data(self,sql_string,data):
		try:
			logging.info('insert_sql_data run on: ' + self.database)
			cursor = self.conn.cursor()
			cursor.execute(sql_string,data)
			cursor.commit()
			return 0
		except pyodbc.Error as ex:
			logging.error('insert_sql_data run on: ' + self.database + 'for query: '+str(ex))
			return 1
		
	




	
	def run_sql_data(SqlString):
		try:
			logging.info('run_sql_data run on ' + self.database)
			cursor = self.p_conn.cursor()
			cursor.execute(SqlString)
			cursor.commit()
		except pyodbc.Error as ex:
			logging.error('get_sql_data run on ' + self.database)
			return -1


