# myGoogleCalendar


NOTE: AD OF 6/2/2023 TARGET HAS DISABLED LOGGING IN WITH A SECURITY QUESTION. 
You are more than welcome to fork this and figure out your own custom way to use this code. 


A simple program to copy my shifts from Target myTime to Google Calendar. 

Hello all! I am using the Google Calendar API for this. If you would like to use this code. You MUST be a Google Cloud developer (its free) and get a google Auth Key. 

# How does this work?

As far as I know, Target does not and has not released APIs into the public to grab a TMs schedule. So in order to do this, we will emulate a user looking at their schedule, Grab all the data we need. and throw it to the Google Calendar API. From there its done! 

To ensure your shifts are always the most recent onces, on every run it is going to verify any previous shifts added and change them if needed. This makes sure that if a time or a workcentre changes, You're still good to go. 


# **READ THIS BEFORE COMPILING**. 



Goto [console.cloud.google.com](https://console.cloud.google.com/)

https://youtu.be/c2b2yUNWFzI?t=225 this is a great video explaining the setting up the OAuth for Google Calendar. Watch till ~10 minutes 

Once you create your OAuth, click download JSON. Drop it into the main directory of your working directory.

Rename the file **"credentials.json"**

# I dropped in the API, now what? 
I'm glad you asked. Now goto the config.cfg file in the main directory and change the info in there to match your Target information. Such as your TM ID, and passcode.

This application will also add the address of your target into your google calendar (helps with traffic predictions). Change that aswell. 

As you all know, Target requires some form of authorization in order to continue to see your information, the Q&A section is super easy to automate for this exact reason.

You will see QKey and QAns (3 questions). qKey is the KEYword that it will search for. 
Such as 
qKey = restaurant
qAns = McDonalds
etc. Make sure you choose a word that isnt going to be seen in the source code ( Like the word "color" )

Name of the event is what Google Calendar is going to input the event as. I know some people here have multiple jobs so I didn't wat to do with work. The default is "Target". You can change this as you wish.

Time Offset. This part is a bit annoying, the best advice I can give is to look up your city and put your offset there. For example google "minneapolis time offset". You see -05:00

THIS IS IMPORTANT. Do NOT forget to put the 0 first! If you do -5:00 instead of -05:00 the code will NOT work. 

Now that everything is setup. run ```pip install -r requirements.txt``` and it will install all the requirements needed! (surprisingly a very little amount) 

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
