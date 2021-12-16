# Audio assistant
A simple Audio assistant

### Setting up Google Calender
For this step you would require a Google Cloud Platform Account.
1. [Create a project and enable the Google Calender API.](https://developers.google.com/workspace/guides/create-project)
2. [Create credentials.](https://developers.google.com/workspace/guides/create-credentials) 
    1. [Set up a OAuth consent screen.](https://developers.google.com/workspace/guides/create-credentials#configure_the_oauth_consent_screen). Add Test users by typing the email of the account has Google Calender setup. Upto 100 Test users can be added.
    2. [Create Desktop Application credentials.](https://developers.google.com/workspace/guides/create-credentials#desktop). 
    3. Download the credentials file and rename it to `credentials.json`. Put it in the root directory.


### PyAudio troubleshooting
First run your IDE or CMD as Administrator and run the following:
- `pip install pipwin`
- `pipwin install pyaudio`



