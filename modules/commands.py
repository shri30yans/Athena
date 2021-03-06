from modules.actions import *


class Command:
    def __init__(self, name, triggers: list, args=None, response=None, function=None):
        self.name = name
        self.triggers = triggers
        self.response = response
        self.function = function
        self.args = args


commands = [
    Command(
        name="Get schedule",
        triggers=[["what","do","i","have"], ["schedule"], ["events","have"]],
        function=get_schedule,
    ),
    Command(
        name="Photo",
        triggers=[["take","photo"],["camera"]],
        function=camera,
    ),
    Command(
        name="Hi",
        triggers=[["hi"], ["hello"], ["hai"]],
        response=["Hello! What do would you like me to do?"],
    ),
    Command(
        name="Time",
        triggers=[["time"], ["what", "is", "time"]],
        function=tell_time
    ),
    Command(
        name="Day",
        triggers=[["what", "is", "day"]],
        function=tell_day),
    Command(
        name="Date",
        triggers=[["date"], ["what", "is", "date"]],
        function=tell_date
    ),
    Command(
        name="Music",
        triggers=[["play", "music"]],
        function=play_music
    ),
    Command(
        name="Open youtube",
        triggers=[["open", "youtube"]],
        response=["Opening youtube"],
        function=open_website,
        args="https://www.youtube.com/",
    ),
    Command(
        name="Open wikipedia",
        triggers=[["open", "wikipedia"]],
        response=["Opening wikipedia"],
        function=open_website,
        args="https://www.wikipedia.com/",
    ),
    Command(
        name="Open reddit",
        triggers=[["open", "reddit"]],
        response=["Opening reddit"],
        function=open_website,
        args="https://www.reddit.com/",
    ),
    Command(
        name="Open netflix",
        triggers=[["open", "netflix"]],
        response=["Opening netflix"],
        function=open_website,
        args="https://www.netflix.com/",
    ),
    Command(
        name="Open google",
        triggers=[["open", "google"]],
        response=["Opening google"],
        function=open_website,
        args="https://www.google.com/",
    ),
    Command(
        name="Open prime",
        triggers=[["open", "prime"], ["open", "prime", "video"], ["open","amazon", "prime", "video"]],
        response=["Opening prime"],
        function=open_website,
        args="https://www.primevideo.com/",
    ),
    Command(
        name="Open stackoverflow",
        triggers=[["open", "stackoverflow"]],
        response=["Opening stackoverflow. Happy Coding!"],
        function=open_website,
        args="https://stackoverflow.com/",
    ),
    Command(
        name="Open github",
        triggers=[["open", "github"]],
        response=["Opening Github."],
        function=open_website,
        args="https://github.com/shri30yans",
    ),
    Command(
        name="Open NCERT",
        triggers=[["open", "ncert"]],
        response=["Opening ncert website."],
        function=open_website,
        args="https://cbseacademic.nic.in/index.html",
    ),
    Command(
        name="Open my website",
        triggers=[["open", "my","website"]],
        response=["Opening your website."],
        function=open_website,
        args="https://shri30yans.github.io/",
    ),
    Command(
        name="Exit", triggers=[["exit"], ["quit"]], response=["Bye."], function=exit
    ),
]
