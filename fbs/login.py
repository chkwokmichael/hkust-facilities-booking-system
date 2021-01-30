from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
import yaml

class login:
	'''
	login: create new webdriver and login with the corresponding longin details
	---------------------------------------------------------------------------
	Variables:
	- username: login user name
	- password: login password
	---------------------------------------------------------------------------
	Methods:
	- catch_resonse(): to catch the web response. Ensure the user account is successfully logged in
	- execute(): execute the login with the username and password
	'''

	username = ''
	password =''


	def __init__(self, username, password):
		with open('config.yaml') as file:
			self.config = yaml.load(file, Loader=yaml.FullLoader)
		self.username = username
		self.password = password

	def catch_response(self):
		'''
		catch_response(): to catch web response. To ensure the functino is executed successfully.
		'''
		try:
		    r = requests.head(self.config['config']['url'])
		    print(r.status_code)
		except requests.ConnectionError:
		    print("failed to connect")

		if r.status_code == 302:
			return True
		else:
			return False

	def execute(self):
		# self.driver = webdriver.Chrome(self.config['config']['chrome_driver_binary'])
		self.driver = webdriver.Chrome(ChromeDriverManager().install())

		# go the HKUST fbs site
		self.driver.get(self.config['config']['url'])

		# input username and password
		username_xpath = '/html/body/table/tbody/tr[2]/td/form/table[2]/tbody[2]/tr[1]/td[2]/div/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr/td[2]/font/input'
		password_xpath = '/html/body/table/tbody/tr[2]/td/form/table[2]/tbody[2]/tr[1]/td[2]/div/table/tbody/tr[3]/td/font/input'
		self.driver.find_element_by_xpath(username_xpath).send_keys(self.username)
		self.driver.find_element_by_xpath(password_xpath).send_keys(self.password)

		# ADDITIONAL step 27/09/2020: ask user to pass the captcha authentication manually.
		print('Please Do the Authentication Manually.')

		# Return true if logged in successfully.
		if self.catch_response():
			return True
		else:
			return False

