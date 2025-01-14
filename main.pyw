from chatbot.chatbot import ChatBot
from chatbot.spellcheck import SpellCheck
from chatbot.TwitterAPI import Twitter
from chatbot import WikipediaAPI
from chatbot.GeocodingAPI import Geocode
import PySimpleGUI as sg
import sys
import subprocess
import os


# Define the window's contents
sg.theme('Dark2')
layout = [[sg.MLine(key='-ML1-'+sg.WRITE_ONLY_KEY, size=(80,10))],
          [sg.Text('Your Input')],
          [sg.InputText(key='i', size=(40, 2))],
          [sg.Button('SUBMIT', bind_return_key=True), sg.Button('EXIT')]]

def __main__():

    # Create the window
    window = sg.Window('Calm Bot', layout, default_element_size=(50, 3),finalize=True)
    cb = ChatBot() 
    sc = SpellCheck()
    tw = Twitter()
    g = Geocode()
    window['-ML1-' + sg.WRITE_ONLY_KEY].print("Calm Bot: Hello, my name is Calm Bot and I'm here to help you!")
    cb.extractQuotes('posQuotes.txt') #we establish the posQuotes in the object
    cb.extractQuotes('negQuotes.txt') #we establish the negQuotes in the object
    exitWords = ['bye', 'quit', 'exit', 'see ya', 'good bye'] #Exit the chat bot with common salutations

    exitError = sc.errorHandlingArray(exitWords) # correcting for errors
    while(True):    #run a loop to keep prompting the user for input
        event, values = window.read()
        print("You: "+ values['i'])
        userInput = (values['i'])
        window.FindElement('i').Update('')
        window['-ML1-' + sg.WRITE_ONLY_KEY].print("You: "+userInput, end='\n')
        if event == sg.WIN_CLOSED or event == 'EXIT':
            break
        if sc.errorHandlingArray(userInput.lower()) in exitError: #allows for words like "exiting" or "exited" to work, as well as many other cases
            window['-ML1-' + sg.WRITE_ONLY_KEY].print("Calm Bot: It was really nice talking to you!", end='\n')
            print("Calm Bot: It was really nice talking to you!")
            break
        else:
            if cb.helloMessage(userInput) != None:  #if hello returns nothing, output a quote
                out=("Calm Bot: " + cb.helloMessage(userInput))
                window['-ML1-' + sg.WRITE_ONLY_KEY].print(out, end='\n')
                #look for twitter words in input
            elif 'twitter' in userInput or 'tweeted' in userInput or 'tweet' in userInput or '@' in userInput:
                #if user enters a twitter handle, start twitter menu
                if '@' in userInput:
                    #retrieve user name
                    tw.setUserName(userInput)
                    #print prompt
                    window['-ML1-' + sg.WRITE_ONLY_KEY].print("What would you like to know about this user?", end='\n')
                    prompt = """1 - When their account was created
2 - Their most recent tweet
3 - Their follower count
4 - Number of tweets they've posted
5 - If the user is verified
0 - Exit Twitter Menu"""
                    print(prompt)
                    window['-ML1-' + sg.WRITE_ONLY_KEY].print(prompt, end='\n')
                    #ask what user wants to see about this twitter user
                    while(True):
                        event, values = window.read()
                        userInput = values['i']
                        window['-ML1-' + sg.WRITE_ONLY_KEY].print("You: " + userInput, end='\n')
                        print("You: " + userInput)
                        if userInput == '0':
                            break
                        elif event == sg.WIN_CLOSED or event == 'EXIT':
                            window.close()
                            sys.exit()
                        else:
                            window['-ML1-' + sg.WRITE_ONLY_KEY].print("Calm Bot: " + str(tw.action(userInput)), end='\n')
                            window.FindElement('i').Update('')
                    window['-ML1-' + sg.WRITE_ONLY_KEY].print("Calm Bot: Exited Twitter menu, what else can I help with?", end='\n')
                    window.FindElement('i').Update('')
                    continue
                #initial prompt if no handle is entered
                out=("Calm Bot: Enter the Twitter handle of the user you're interested in (include the @)")
                print(out)
                window['-ML1-' + sg.WRITE_ONLY_KEY].print(out, end='\n')
                #look for wiki words
            elif 'wiki' in userInput or 'wikipedia' in userInput:
                #print out the summary for the topic
                window['-ML1-' + sg.WRITE_ONLY_KEY].print("Calm Bot: " + summarize(userInput), end = '\n')
                print("Calm Bot: " + summarize(userInput))
            elif 'address' in userInput or 'geo' in userInput or 'map' in userInput:
                #ask user for address or geocode, entering one will convert into the other
                window['-ML1-' + sg.WRITE_ONLY_KEY].print("Calm Bot: Enter an address to get its geocode (lat & long). Alternatively, you can enter a geocode to get the address", end = '\n')
                event, values = window.read()
                userInput = values['i']
                window['-ML1-' + sg.WRITE_ONLY_KEY].print("You: " + userInput, end='\n')
                print("You: " + userInput)
                #check if userInput has any letters in it, so we know if user inputs lat and long or address
                lower = userInput.lower()
                if lower.islower():
                    # displays lat and long
                    lat,long = g.convert(userInput)
                    window['-ML1-' + sg.WRITE_ONLY_KEY].print("Calm Bot: Lat: " + str(lat) + " Long: " + str(long), end='\n')
                    window.FindElement('i').Update('')
                else:
                    #displays address of lat and long
                    coords = userInput.split(' ')
                    print(coords)
                    window['-ML1-' + sg.WRITE_ONLY_KEY].print("Calm Bot: " + g.reverseConvert(coords[0],coords[1]), end='\n')
                    window.FindElement('i').Update('')
            else:
                out = ("Calm Bot: " + cb.botResponse(userInput))
                print(out)
                window['-ML1-' + sg.WRITE_ONLY_KEY].print(out, end='\n')
                # See if user wants to quit or window was closed
                if event == sg.WINDOW_CLOSED or event == 'EXIT':
                    break

    window.close()
    sys.exit()
    
__main__()
