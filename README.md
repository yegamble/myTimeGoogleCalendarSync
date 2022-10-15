# myGoogleCalendar
This is to port over my shifts from Target into my personal Google Calendar.

# **READ THIS BEFORE COMPILING**. 

Hello all! I am using the Google Calendar API for this. If you would like to use this code. You MUST be a Google Cloud developer (its free) and get a google Auth Key. 


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

I'm trying to tinker with headless mode. Would be really convenient. 
