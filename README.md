# Assignment 3 - An Interactive Conversational Agent

This Project was developed by Sebi Unipan, Chinmay Gopal, Iwan Levin, Amritpal Aujla and Ali Ibrahim.
## Description

This Project aims to impersonate a psychiatrist in the form of an online chat-bot. More specifically, this online chat-bot needs to be able to offer real world advice and be able to hold a conversation with a real person. Our Chat-bot specializes in helping University students with mental health issues such as depression, loneliness and stress.

Our Team truly believes that anonymous online conversation with an intelligent chat-bot can aleviate mental stresses without the added expenses a real psychiatrist would require.

This conversational bot was developed entirely in Python using the Natural Language Processing library, Natural Language Toolkit(NLTK).

The program is made up of two classes: chatbot and main
>chatbot is the class that can has all the attributes of the chat bot and its methods

>main class is where a chatbot object gets created and is run to extract quotes from file as  
>well as running a loop to continuously ask the user for input with a loop in the class until  
>they enter an exit word  

## Installation

To be able to run the chat bot, you need several Python packages.
Open up command prompt and type the following:  

`pip install nltk`  

`pip install -U scikit-learn`  

`pip install googlemaps`  

`pip install wikipedia`  

`pip install tweepy`

You should then open up a Python interactive console (IDLE) and download all nltk packages by:

`import nltk`  

`nltk.download()`

A GUI should pop up, select 'all | All packages' and press download, afterwards close the GUI.

Afterwards, you may run the main.pyw file and the bot should work accordingly.
***NOTE: When running the main.pyw file, a delay of 10-15 seconds is normal to train the model in the sentiment file***

## New features

POS tagging: Using nltk's POS tagging based on stanford's toolkit, this feature takes a word and finds similar words based on context and grammar.
Some words just aren't available in the prewritten text for the chatbot's replies. This feature allows for words that aren't in the replies but are close enough to some aspect that the chatbot can reply to, so the chatbot assumes the user was talking about the new converted word and replies accordingly.

Example:  
You: crazy  
Calm Bot: Solution: if you are feeling sad, do something that makes you happy.

The word "crazy" is not available in our text file, but since it is close to the words sad and mad, the bot had a response for these similar words and was able to answer.

Spell check: Using PorterStemmer, simple spelling mistakes such as typing "anxieti" instead of "anxiety" can be corrected by removing suffixes from both the response and the reply when checking for similarities. This way a large number of spelling mistakes that involve the end of the word being mispelt or grammatically incorrect can be caught and replied to properly.

Example:  
You: depressioning  
Calm Bot: Depression can sometimes be overwhelming, just know that you are not alone.

It recognized the depressioning is the same as depression and responded correctly.

Sentiment: Using the sentiment analysis tutorial for Python from https://do.co/3tPTa2w I analysed the quotes we had
from A2 and categorized them using the sentiment model based on negative or positive sentiments and put them in according 
text files. After that it was implemented in the ChatBot's botResponse function to classify the sentiment of the user's input
and based on whether it was positive or negative, it would output the most similar quote to the user's input from the available
responses.

Example:  
You: i am unhappy  
*internally calm bot recognizes this as a negative sentiment statement*  
Calm Bot: I am here to help you get better.

Synonom Recognition: This was implememtned as the following. I created a list of adjectives that is common when talking to a psychiatrist, then used wordnet to create a 
list of synonoms for each potential adjective used. The bot will check the user input to see if it contains any of the potenital adjectives or any of their synonoms. Laslty
if there is a synonom found in the input, whichever potential adjective the synonom is linked to is added behind the scenes to the user input, so this way its similarity
score is increased when being compared to the quotes files.

Example:  
You: im feeling banal  
Calm bot: if you are feeling tired, drink lots of water and have a hearty meal.  
You : im feeling unenergized  
Calm bot: if you are feeling lazy, go workout.  
***NOTE: the words banal and unenergized are nowhere to be found in quotes files, but the bot recognizes the synonom and shoots a relavent response***  

## APIs Implemented
#### Twitter API:
Users can retrieve certain aspects of any Twitter user's account properties. By typing twitter related words such as 'twitter', 'tweet', or 'tweeted' will bring up the Twitter API menu. This menu will ask for a Twitter user's Twitter handle. After this, it retrieves the Twitter user's account info and displays options to the chat bot user on what info to display. The user can choose to display things like when the Twitter account was created, their most recent Tweet, their follower count, the number of Tweets the user's posted, and the user's verified status which returns false if they aren't verified.  

#### Wikipedia API:
Users can retrieve a summary about any topic available on Wikipedia by simply typing ***'wiki topic'*** or ***'wikipedia topic'***. Nothing much else to this API, it's pretty straight forward.

#### Google Geocode API:
Users can use this turn any address into a geocode (lat & longitude coordinate). They are also able to turn any *on-land* geocode back into its corresponding address. The geocode must be on-land as we cannot get addresses for a coordinate in the middle of an ocean. To access this ability the user can type keywords like 'address', 'geo', or 'map'.
