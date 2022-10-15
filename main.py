# made by versionDefect. Heavily inspired by code from https://github.com/TidOS/Shift2CalDAV
# The logic of the signin process (especially the Q&A 2FA) and a short little 12 hour -> 24 hour converter I found on geeksforgeeks
# https://www.geeksforgeeks.org/python-program-convert-time-12-hour-24-hour-format/
# but the rest is my code.


import configparser
import time

import undetected_chromedriver as uc
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os.path
# GOOGLE SHIT
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# alot of libraries. esp for my first python project lol.

config = configparser.ConfigParser()
creds = None
SCOPES = ['https://www.googleapis.com/auth/calendar']
options = uc.ChromeOptions()
options.add_argument("--password-store=basic")

options.add_experimental_option(
    "prefs",
    {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
    },
)


# This is to set up the settings for chrome
# The settings make it so


# Some code I found on GFG.
# https://www.geeksforgeeks.org/python-program-convert-time-12-hour-24-hour-format/
def convert24(str1):
    # Checking if last two elements of time
    # is AM and first two elements are 12
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00:00 AM"

    # remove the AM
    elif str1[-2:] == "AM":
        return str1

    # Checking if last two elements of time
    # is PM and first two elements are 12
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1

    else:
        # add 12 to hours and remove PM
        return str(int(str1[:2]) + 12) + str1[2:8]


browser = uc.Chrome(use_subprocess=True, options=options)

config.read('creds.cfg')
storeAddress = config['secrets']['storeAddy']
# This grabs all of your information.

# navigate to a website
browser.get('http://mytime.target.com')
try:
    element_present = EC.presence_of_element_located((By.ID, 'loginID'))
    WebDriverWait(browser, 10).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load or login failed?")
time.sleep(1    )
# sometimes it goes too fast. sleep for 1 second here
print("entering username and password...")
username = browser.find_element(By.ID, 'loginID')
password = browser.find_element(By.ID, 'password')
# This finds the login and the password box
username.click()
username.send_keys(config['secrets']['employeeID'])
username.send_keys(Keys.TAB)
username.click()
password.send_keys(config['secrets']['password'])
password.click()

# This sends the Username and the password from the config file to the inputs

# password.send_keys(Keys.RETURN)
loginButton = browser.find_element(By.ID, 'submit-button')
loginButton.submit()
time.sleep(1.5)
print("selecting Q+A button...")
# choose to answer security questions


while "quickly verify" not in browser.page_source:
    browser.save_screenshot('ss.png')
    time.sleep(0.3)
# Not the best way to do this. Probably change it later. 

browser.find_element(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "jss156", " " ))]').click()
# this took me so fucking long for no reason
# I was using the chrome one and it sucked compared to a simple Chrome extension

while "answer question" not in browser.page_source:
    time.sleep(0.3)

qIn = browser.find_element(By.ID, 'q-input')
# Finds the question input

if config['questions']['q1Key'] in browser.page_source:
    qIn.send_keys(config['questions']['q1Ans'])
elif config['questions']['q2Key'] in browser.page_source:
    qIn.send_keys(config['questions']['q2Ans'])
else:
    qIn.send_keys(config['questions']['q3Ans'])
# since none of the others matched it must be this answer
browser.find_element(By.ID, 'submit-button').click()

while "View Timecard" not in browser.page_source:
    time.sleep(0.3)

browser.get('http://mytime.target.com/schedule')

time.sleep(2)
startTimeLoc = '//*[@id="0"]/li/div/div[3]/div[1]/a/div/div[1]/p'
endTimeLoc = '//*[@id="0"]/li/div/div[3]/div[1]/a/div/div[3]/p'
positionLoc = '//*[@id="0"]/li/div/div[3]/div[1]/a/div/div[4]/div/p'
# this is the location of the times.
time.sleep(2)

# ------------------------------ GCAL SETUP -------------------------------------------
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())
service = build('calendar', 'v3', credentials=creds)
############################################################################################


############################################################################################
# this is to scan to delete all current events in order to make sure it is always updated

for i in range(int(config['options']['range'])):
    if i >= 1:
        print("Going to the next week!")
        browser.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div[1]/div[3]/button').click()
        #This takse us to the next week
        time.sleep(3)

    # this is to find the start and the end of the week.
    date = browser.find_element(By.ID, '0').get_attribute("outerHTML")
    startYear = date[46:50]
    startMonth = date[51:53]
    startDay = date[54:56]


    date = browser.find_element(By.ID, '6').get_attribute("outerHTML")
    endYear = date[46:50]
    endMonth = date[51:53]
    endDay = date[54:56]
    # this is to set up the start and the end times of the search to make sure we don't go too far since we don't need to. we're going week by week.
    sTime = startYear + "-" + startMonth + "-" + startDay + "T" + "00:00:00" + config['options']['timeOffset']
    eTime = endYear + "-" + endMonth + "-" + endDay + "T" + "23:59:00" + config['options']['timeOffset']

    events_result = service.events().list(calendarId='primary', timeMin=sTime, timeMax=eTime,
                                          singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    # This puts the events into a list and the for loop goes thru the items scheduled for the week
    # if something matches the label that you chose in the config text then it will delete it to later add it again to ensure your calendar is always upto date

    for event in events:
        if event['summary'] == config['options']['nameOfEvent']:
            print("Deleting Event!")
            eventId = event['id']
            service.events().delete(calendarId='primary', eventId=eventId).execute()
            print("Deleted! ")



    for x in range(7):
        strX = str(x)
        shiftStart = "no"
        shiftEnd = "no"
        # It would freak out if you tried to output an empty string.

        xNum = str(x)
        # String manipulation. myTime only changes on number to see the start vs the end time.
        checkDate1 = startTimeLoc[0:9] + xNum + startTimeLoc[10:48]
        checkDate2 = endTimeLoc[0:9] + xNum + endTimeLoc[10:48]
        checkPos = positionLoc[0:9] + xNum + positionLoc[10:52]
        # I thought I was a jenius for this
        for shiftStart in browser.find_elements(By.XPATH, checkDate1):
            for shiftEnd in browser.find_elements(By.XPATH, checkDate2):
                for JobTitle in browser.find_elements(By.XPATH, checkPos):
                    jTitle = JobTitle.text

                    desc = 'You are being requested to work a shift of ' + JobTitle.text + ' at Target Corperation'
                    date = browser.find_element(By.ID, x).get_attribute("outerHTML")
                    year = date[46:50]
                    month = date[51:53]
                    day = date[54:56]

                    sTime = year + "-" + month + "-" + day + "T" + convert24(shiftStart.text)[0:4] + ":00" + \
                            config['options'][
                                'timeOffset']
                    eTime = year + "-" + month + "-" + day + "T" + convert24(shiftEnd.text)[0:4] + ":00" + \
                            config['options'][
                                'timeOffset']
                    # Start times and the end times for that shift.
                    event = {
                        'summary': config['options']['nameOfEvent'],
                        'location': config['secrets']['storeAddy'],
                        'description': desc,
                        'colorId': 11,
                        'start': {
                            'dateTime': sTime
                        },
                        'end': {
                            'dateTime': eTime,
                        },
                        'reminders': {
                            'useDefault': False,
                            'overrides': [
                                {'method': 'popup', 'minutes': 45},
                            ],
                        },
                    }
                    # this sends the event to google, and You will know its sucessfull by seeing "Event Created:" in the console.
                    event = service.events().insert(calendarId='primary', body=event).execute()
                    print('Event created: %s' % (event.get('htmlLink')))
time.sleep(4)
