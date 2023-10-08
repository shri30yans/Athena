<!-- PROJECT LOGO -->
<h3 align="center">Athena</h3>
This project is a work in progress. Currently, it has the ability to recognize basic voice commands and execute them.

## The challenge:
In today's world, the modern student faces many distractions. It becomes tough to concentrate on our academics and focus on our work.
These distractions shorten our attention span, push our boundaries to procrastinate and maneuver us to indulge in other activities that hold us back from fulfilling our academic potential.

This is especially true given the current pandemic, where we study online and find ourselves surrounded by thousands of distractions.
This pulls one's attention away from the task at hand and diminishes productivity. 

What we require is a dedicated schedule to ensure that one stays on 
track and to make sure our responsibilities as a student aren't neglected. 

## Solution:
Athena, a voice-activated digital assistant named after the Greek goddess of knowledge, aims to solve this by guiding the students to focus on key goals, ensuring students follow their schedules without distractions by constantly reminding them of due tasks, upcoming events, and the deadlines for projects.
It also maximizes productivity by being able to perform multiple tasks at once through voice commands.
Athena also connects to the student's Google Calendar to keep track of a student’s predefined schedule.

<!--
## Approach:
Athena uses voice queries to answer questions, schedule events, answer basic questions, create to-do lists, and perform actions by sending requests to a set of Internet services.
It is also capable of setting alarms and reminders, music playback, entertainment, and searching the internet.
It allows users to perform hands-free interaction with their computer through voice-activated commands, such as opening an application or a website verbally.

## Project objectives:
Creating a simple voice assistant that recognizes basic commands (English).
Creating a GUI for users to interact with Athena.
Integrating Google Calendar with Athena to keep track of the user's events.
Using other APIs such as Wikipedia to perform other functions.
Verbally issuing reminders about upcoming tasks and deadlines.

## Course taken:
Setting up an efficient voice-to-text system.
Making the bot recognize basic voice commands.
Being able to output verbally by converting text to speech.
Using Google Calendar API to keep track of events and create new ones.
Integrating other APIs to fetch information 
-->



### Set up Athena
1. Install all dependencies: (Ubuntu)
```
sudo pip3 install -r requirements.txt
```
2. Setup requirements.py
### Setting up Google Calendar
For this step, you would require a Google Cloud Platform Account.
1. [Create a project and enable the Google Calendar API.](https://developers.google.com/workspace/guides/create-project)
2. [Create credentials.](https://developers.google.com/workspace/guides/create-credentials) 
    1. [Set up an OAuth consent screen.](https://developers.google.com/workspace/guides/create-credentials#configure_the_oauth_consent_screen). Add Test users by typing the email of the account that has Google Calender setup. Up to 100 Test users can be added.
    2. [Create Desktop Application credentials.](https://developers.google.com/workspace/guides/create-credentials#desktop). 
    3. Download the credentials file and rename it to `credentials.json`. Put it in the root directory.


### PyAudio troubleshooting
Run your IDE or CMD as Administrator and run the following:
1. `pip install pipwin`
2. `pipwin install pyaudio`



