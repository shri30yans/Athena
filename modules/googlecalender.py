# from __future__ import print_function

from datetime import date, timedelta, datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pytz

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]
MONTHS = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december",
]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAY_EXTENTIONS = ["st","nd","rd", "th"]


def authenticate_google():
    """
    Authenticates the Google Calender API and creates a "token.json" file.
    The file "token.json" stores the user's access and refresh tokens, and is
    created automatically when the authorization flow completes for the first
    time.
    """
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # Let the user loggin if credentials do not exist or are invalid.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    service = build("calendar", "v3", credentials=creds)
    return service

def get_events(day, service):
    '''
    Returns a list of all the events on a particular day.

    Args:
        day (datetime.date): Date to return events for
        service (googleapiclient.discovery.Resource): Google Calender connection
    
    '''
    date = datetime.combine(day, datetime.min.time())
    end_date = datetime.combine(day, datetime.max.time())
    utc = pytz.UTC
    date = date.astimezone(utc)
    end_date = end_date.astimezone(utc)

    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=date.isoformat(),
            timeMax=end_date.isoformat(),
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )

    events = events_result.get("items", [])
    print(events)
    return events


def get_date(query_list):
    '''
    Returns a datetime.date object from a list of text.

    Args:
        query_list (list): List of possible variations of speech to text.

    Tests:
        Current date: 2021-12-19

        >>> get_date(['September 9th', 'September ninth', 'September 9th', 'Septe 9th', 'Sep 9th'])
        2022-09-09
        Since September is over, shows date for next september
        
        >>> get_date(['Tuesday', 'Tues day'])
        2021-12-21
        Shows date for upcoming tuesday

         >>> get_date(['today'])
        2021-12-19
        Shows today's date
    '''

    today = date.today()
    day, day_of_week, month = None, None, None
    year = today.year

    for text in query_list:
        text = text.lower()
        if "today" in text:
            return today
        else:
            for word in text.split():
                if word in MONTHS:
                    month = MONTHS.index(word) + 1
                elif word in DAYS:
                    day_of_week = DAYS.index(word)
                elif word.isdigit():
                    day = int(word)
                else:
                    for ext in DAY_EXTENTIONS:
                        extention_pos = word.find(ext)

                        # If the extention is not at the beginning.
                        if extention_pos != 0:
                            try:
                                day = int(word[: extention_pos])

                            except ValueError:
                                # Not a Date.
                                pass

    # If the text mentions a month before the current month set the year to next year.
    if (month is not None) and (month < today.month):
        year = year + 1

    # If a month was not found but a day was given, set month to current or next month depending on that day.
    if (month is None) and (day is not None):
        if day < today.day:
            month = today.month + 1
        else:
            month = today.month

    # Only a day of the week was given.
    if (month is None) and (day is None) and (day_of_week is not None):
        current_day_of_week = today.weekday()
        difference = day_of_week - current_day_of_week

        # if "next" is found in the text, add 7 days to current date.
        if "next" in text:
            difference += 7

        # If that day of the week is over, set day to next week.
        if difference < 0:
            difference += 7

        return today + timedelta(difference)

    if day is None:
        return today
    else:
        return date(month=month, day=day, year=year)

