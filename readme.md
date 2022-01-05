# Athena

## The challenge:
In today's world, the modern student faces many distractions. It becomes tough to concentrate on our academics and focus on our work.
These distractions shorten our attention span, pushes our boundaries to procrastinate and maneuver us to indulge in other activities that hold us back from fulfilling our academic potential.

This is especially true given the current pandemic, where we study online and 
find ourselves surrounded by thousands of distractions.
This pulls one's attention away from the task at hand and diminishes our productivity. 

What we require is a dedicated schedule to ensure that one stays on 
track and to make sure our responsibilities as a student aren't neglected. 

## Solution:
Athena, a voice activated digital assistant named after the Greek goddess of knowledge, aims to solve this by guiding the student to focus on key goals, by ensuring that students follow their schedules without distractions by constantly reminding them of due tasks, upcoming events and the deadlines for projects.
It also maximises productivity by being able to perform multiple tasks at once through voice commands.
Athena also connects to the students Google Calendar to keep track of a student’s predefined schedule.

<!--
## Approach:
Athena uses voice queries to answer questions, schedule events, answer basic questions, create to-do lists and perform actions by sending requests to a set of Internet services.
It is also capable of setting alarms and reminders, music playback, entertainment and searching the internet.
It allows users to perform hands-free interaction with one's computer through voice activated commands, such as opening an application or a website verbally.

## Project objectives:
Creating a simple voice assistant that recognises basic commands (English).
Creating a GUI for users to interact with Athena.
Integrating Google Calendar with Athena to keep track of the user's events.
Using other API's such as Wikipedia to perform other functions.
Verbally issuing reminders about upcoming tasks and deadlines.

## Course taken:
Setting up an efficient voice to text system.
Making the bot recognise basic voice commands.
Being able to output verbally by converting text to speech.
Using Google Calendar API to keep track of events and creating new ones.
Integrating other API's to fetch information 
-->


### Set up Athena
1. Install all depedencies: (Ubuntu)
```
sudo pip3 install -r requirements.txt
```
2. Setup requirements.py
### Setting up Google Calender
For this step you would require a Google Cloud Platform Account.
1. [Create a project and enable the Google Calender API.](https://developers.google.com/workspace/guides/create-project)
2. [Create credentials.](https://developers.google.com/workspace/guides/create-credentials) 
    1. [Set up a OAuth consent screen.](https://developers.google.com/workspace/guides/create-credentials#configure_the_oauth_consent_screen). Add Test users by typing the email of the account has Google Calender setup. Upto 100 Test users can be added.
    2. [Create Desktop Application credentials.](https://developers.google.com/workspace/guides/create-credentials#desktop). 
    3. Download the credentials file and rename it to `credentials.json`. Put it in the root directory.


### PyAudio troubleshooting
First run your IDE or CMD as Administrator and run the following:
1. `pip install pipwin`
2. `pipwin install pyaudio`



