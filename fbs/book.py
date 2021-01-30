from selenium import webdriver
import yaml

class Book():
	'''
	Book: execute the booking requested by user
	-------------------------------------------
	Varaibles:
	main_window_handle: store the main window of the webdriver
	signin_window_handle: store the pop up window
	'''

	main_window_handle = None
	signin_window_handle = None
	driver = None
	date_to_book = None
	td = None

	# initiating Book instances
	def __init__(self, user, date_to_book, xpath_element):
		self.driver = user.driver
		self.date_to_book = date_to_book
		self.td = xpath_element
		with open('config.yaml') as file:
			self.config = yaml.load(file, Loader=yaml.FullLoader)

	def execute():

		# go to the booking page
		self.driver.get(self.config['config']['url'])

		# set current web window as main_window_handle
		while not self.main_window_handle:
			main_window_handle = driver.current_window_handle


		# select Football Pitch
		driver.find_element_by_xpath('/html/body/form/table[2]/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/select/option[3]').click()
		driver.find_element_by_xpath('/html/body/form/table[2]/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[4]/td[2]/font/select/option[2]').click()
		# input the date
		driver.find_element_by_xpath('/html/body/form/table[2]/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[5]/td[2]/font/input').click()
		driver.find_element_by_xpath('/html/body/form/table[2]/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[5]/td[2]/font/input').clear()
		driver.find_element_by_xpath('/html/body/form/table[2]/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[5]/td[2]/font/input').send_keys(self.date_to_book)
		# submit search
		driver.find_element_by_xpath('/html/body/form/table[2]/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[5]/td[4]/div/font/font/input').click()
		driver.find_element_by_xpath('/html/body/form/table[2]/tbody/tr[2]/td/table/tbody/tr[2]/td/table[2]/tbody/tr[2]/td/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[{td}]/td/div/a'.format(td=td)).click()

		# handle pop up window to confirm booking.
		while not self.signin_window_handle:
			for handle in self.driver.window_handles:
				if (handle != self.main_window_handle):
					self.signin_window_handle = handle
					break

		# switch to pop up window to confirm booking
		driver.switch_to.window(signin_window_handle)
		driver.find_element_by_xpath('/html/body/form/table/tbody/tr[11]/td/input[3]').click()

		# Return
		return True



