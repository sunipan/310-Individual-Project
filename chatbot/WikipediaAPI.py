import wikipedia

def summarize(userInput):
    words = userInput.split(' ')
    length = len(words)
    topic = ""
    counter = 0
    for i in range(length):
        if 'wiki' == words[i] or 'wikipedia' == words[i]:
        #this piece of code allows multiple word topics (eg. "The Civil War")
            if counter < length - 1:
                counter = i + 1
        if counter < length:
            topic += words[counter] + " "
            counter += 1
    return wikipedia.summary(topic, sentences = 5)

