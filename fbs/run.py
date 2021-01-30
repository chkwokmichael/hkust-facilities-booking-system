import login as Login
import book as Book
from selenium import webdriver
import datetime
import yaml
import pytz
import time

# load configurations from confure.yaml
with open('config.yaml') as file:
	config = yaml.load(file, Loader=yaml.FullLoader)

# ask user to input booking details
try:
	date_to_book = input('Please input the date you want to book (dd/mm/yyyy): ')
	time_to_book = input("Please input the start time (hour in 24-hours format, e.g. '19'): ")
	duration_to_book = int(input ('Plesae input how many hours do you want to book: '))
except ValueError:
	print('ValueError. Please try again')

users_detail = []
login_detail = {}

# get login info from user
# each user can only reserve one hour, so number of logins needed = no. of hours they want to book
for i in range(duration_to_book):
	username = input('Please input your username ('+str(i+1)+'): ')
	password = input('Please input your password ('+str(i+1)+'): ')
	users_detail.append((username, password))

# login
for i in range(duration_to_book):

	username, password = users_detail[i] # get user login details from users_detail

	print('loging in as ' + username)

	login_detail[i] = [Login.login(username, password)] # create login instance login function from Login module.
	login_detail[i].append(login_detail[i][0].execute())

# ADDITIONAL features at 27/09/2020:
# ask users to pass the authentication
time.sleep(30)

print('Successfully logged into all users.\n')
print('Waiting for the booking time...\n')

# execution
booked = False

booking_hour = config['config']['booking_hour']

# calculate the xpath_element
xpath_elements = {}

# get the xpath_elements to use
for i in range(duration_to_book):
	xpath_elements[i] = (int(time_to_book)-7)*2+1+(i*2)

# get the date of execution
start_day = datetime.datetime.today().day

booking_time = datetime.datetime.now(pytz.timezone('Hongkong')).replace(day=start_day,hour=int(booking_hour[:2]),minute=0,second=0, microsecond=0)

last_refresh = datetime.datetime.now(pytz.timezone('Hongkong'))

while not booked:
	
	# get the curent time
	time_now = datetime.datetime.now(pytz.timezone('Hongkong'))
	# get the time different from now to execution time
	time_diff = divmod((time_now-last_refresh).total_seconds(), 60)[0]

	# if current time is later then execution time, then book
	if time_now > booking_time:
		for i in range(duration_to_book):
			Book.book(login_detail[i], date_to_book, xpath_elements[i]).execute()
		booked = True

	# if time difference between current time and last refresh time is more than 10 mins, refresh the page to prevent auto logout
	elif time_diff >= 10:
		for i in range(duration_to_book):
			login_detail[i][0].driver.refresh()
		last_refresh = time_now
		print('refreshed')

print('Your booking request is successful... Please check your email for the confirmation.\n')
print('Until next time, bye~')




