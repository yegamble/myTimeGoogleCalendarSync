# myGoogleCalendar

You can authenticate by using the 2FA authenticator code

A simple program to copy my shifts from Target myTime to Google Calendar. 

Hello all! I am using the Google Calendar API for this. If you would like to use this code. You MUST be a Google Cloud developer (its free) and get a Google Auth Key. 

# How does this work?

This code will authenticate you, save your token, and call the WFM API which allows this script to be ran multiple times whilst keeping the same token.

To ensure your shifts are always the most recent onces, on every run it is going to verify any previous shifts added and change them if needed. This makes sure that if a time or a workcentre changes, You're still good to go. 


# **READ THIS BEFORE COMPILING**. 



Goto [console.cloud.google.com](https://console.cloud.google.com/)

https://youtu.be/c2b2yUNWFzI?t=225 this is a great video explaining the setting up the OAuth for Google Calendar. Watch till ~10 minutes 

Once you create your OAuth, click download JSON. Drop it into the main directory of your working directory.

Rename the file **"credentials.json"**

# I dropped in the API, now what? 
I'm glad you asked. Now goto the config_file.py file in the main directory and change the info in there to match your Target information. Such as your TM ID, and password.
Also add your Pushover API Key to get notifications when a shift is added or modified
There is a flag "Headless" which allows you to run this code in the background or on something like a Server.

In V1 this script would require significantly more amounts of information but now will automatically lookup a store's information and autofill as needed. 
This was done to have less configuration but also to make it more dynamic since ODTM's will soon be able to work at multiple stores. 

Now that everything is setup. run ```pip install -r requirements.txt``` and it will install all the requirements needed!
Give it a shot and compile it. 

If it fails. Try to add chromedriver to your windows path. 

# Why is it asking for my Google?

Since we are using the Google Calendar API we need to go thru google to get the required tokens to use those APIs.

# IS THIS A WIRUS?

You will see this screen

![2022-10-15 02_17_20-Sign in - Google Accounts](https://user-images.githubusercontent.com/37282503/195978955-6b12cbca-b991-4bfa-ae2e-4012f044bb0c.png)

All this is saying is that the application that you made is still in testing mode. Google has not verified verifcation is if you want to make this a widespread thing where random users will use this. You're more than welcome to verify it thru google but you're wasting your time. Hit continue. 

And you're done!

In theory your Google Calendar is getting filled with your target shifts. 



This program is fully supported in headless mode! If you want to run this program in headless mode change the headless button in the config and you're all set! 
