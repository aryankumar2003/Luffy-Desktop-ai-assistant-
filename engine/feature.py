from playsound import playsound
import eel
from engine.config import ASSISTANT_NAME
import os
import re
from engine.command import speak
import pywhatkit as kit

#play assistant sound 
@eel.expose
def playAssistantSound():
    music_dir="www\\assets\\vendore\\texllate\\audio\\sound.mp3"
    playsound(music_dir)
    
def openCommand(query):
    query=query.replace(ASSISTANT_NAME, "")
    query=query.replace("open", "")
    query.lower()

    if query !="":
        speak("Opening"+ query)
        os.system('start'+query)
    else:
        speak("not found")
#giving youtube command
def PlayYoutube(query):
    search_term=extract_yt_term(query)
    speak("playing "+ search_term +"on Youtube")
    kit.playonyt(search_term)

def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match=re.search(pattern,command, re.IGNORECASE)
    return match.group(1) if match else None

#giving command of webbrowser
def Openwebbrowser(query):
    search_term=extract_wb_term(query)
    speak("opening "+ search_term +"on webbrowser")
    kit.openonwb(search_term)


def extract_wb_term(command):
    pattern = r'open\s+(.*?)\s+on\s+webbrowser'
    match=re.search(pattern,command, re.IGNORECASE)
    return match.group(1) if match else None