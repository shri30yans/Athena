import random
from modules.commands import commands
from modules.audio import listen, speak
from modules.googlecalender import authenticate_google
import config
import keyboard 

def startup():
    speak("Systems online. How can I help you, dude.")
    print("Systems online.")


def find_command(query_list):
    for cmd in commands:
        for possible_query in query_list:
            for command_triggers in cmd.triggers:
                # All the strings in each trigger list need to be present in order to be a match.
                if all(
                    x.lower() in possible_query.lower().split()
                    for x in command_triggers
                ):
                    print(f"Match found! {cmd.name}")
                    return cmd

def command_sequence():
    print("Triggered")
    query_list = listen()
    # Speech is detected.
    if query_list is not None:
        command = find_command(query_list)

        if command:
            if command.response:
                speak(random.choice(command.response))

            if command.function:
                # If the command action function does not have any attributes.
                if command.args is None:
                    command.function(query_list)
                # If the command action function has attributes.
                else:
                    command.function(query_list,command.args)
        else:
            speak("I couldn't understand what you said.")
            print("I couldn't understand what you said.")
        print("----------")


def key_trigger():
    while True:
        # The trigger key is pressed.
        if keyboard.is_pressed(config.trigger_key):
            command_sequence()

authenticate_google()
startup()
key_trigger()
