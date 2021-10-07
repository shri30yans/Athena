from modules.commands import commands
import random
from modules.audio import listen, speak
import config


def boot():
    speak("Booting")

def how_can_I_help():
    speak("How can I help you, sir.")

def find_command(query_list):
    for cmd in commands:
        for possible_query in query_list:
            for command_triggers in cmd.triggers:
                if all(x.lower() in possible_query.lower().split() for x in command_triggers):
                    print(f"Match found! {cmd.name}")
                    return cmd


def run_forever():
    while True:
        query_list = listen()
        if query_list is not None:
            if any(prefix.replace(" ","").lower() in x.replace(" ","").lower() for x in query_list for prefix in config.possible_prefix_list):
                command = find_command(query_list)
                if command:

                    if command.response:
                        speak(random.choice(command.response))

                    if command.function:
                        if command.args is None:
                            command.function()
                        else:
                            command.function(command.args)
                        #command.function(query_list,command.args)
                else:
                    # A Command was not detected but the prefix was in the sentence
                    speak("Sorry I didn't understand what you said.")   
                print("------")


boot()
how_can_I_help()
run_forever()
