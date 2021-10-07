from modules.actions import *

class Command:
    def __init__(self,name,triggers:list,args = None, response = None, function = None):
        self.name = name
        # Triggers attribute has sub elements.
        # All the strings in these elements need to be present in order to be a match
        self.triggers = triggers
        self.response = response
        self.function = function
        self.args = args

commands = [
                Command(
                    name = "Hi",
                    triggers =  [["hi"],["hello"],["hai"]],
                    response = ['Hello! What do you want to do today?']),
                Command(
                    name = "Time",
                    triggers = [["time"],["what","is","time"]],
                    function = tell_time),
                Command(
                    name = "Day",
                    triggers = [["day"],["what","is","day"]],
                    function = tell_day),
                Command(
                    name = "Date",
                    triggers = [["date"],["what","is","date"]],
                    function = tell_date),
                Command(
                    name = "Music",
                    triggers = [["play","music"]],
                    function = play_music),
                Command(
                    name = "Open youtube",
                    triggers = [["open","youtube"]],
                    response = ['Opening youtube'],
                    function = open_website,
                    args = "https://www.youtube.com/" ),
                Command(
                    name = "Open wikipedia",
                    triggers = [["open","wikipedia"]],
                    response = ['Opening wikipedia'],
                    function = open_website,
                    args = "https://www.wikipedia.com/" ),
                Command(
                    name = "Open reddit",
                    triggers = [["open","reddit"]],
                    response = ['Opening reddit'],
                    function = open_website,
                    args = "https://www.reddit.com/" ),
                Command(    
                    name = "Open netflix",
                    triggers = [["open","netflix"]],
                    response = ['Opening netflix'],
                    function = open_website,
                    args = "https://www.netflix.com/" ),
                Command(
                    name = "Open google",
                    triggers = [["open","google"]],
                    response = ['Opening google'],
                    function = open_website,
                    args = "https://www.google.com/" ),
                Command(
                    name = "Open prime",
                    triggers = [["open","prime"],["open","prime","video"]],
                    response = ['Opening prime'],
                    function = open_website,
                    args = "https://www.primevideo.com/" ),
                Command(
                    name = "Open stackoverflow",
                    triggers = [["open","stackoverflow"]],
                    response = ['Opening stackoverflow. Happy Coding!'],
                    function = open_website,args = "https://stackoverflow.com/" ),
                Command(
                    name = "Open github",
                    triggers = [["open","github"]],
                    response = ['Opening Github.'],
                    function = open_website,args = "https://github.com/shri30yans" ),
                Command(
                    name = "Exit",
                    triggers = [["exit"],["quit"]],
                    response = ['Bye.'],
                    function = exit),
            
            ]