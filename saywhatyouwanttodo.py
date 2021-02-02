from math import e
import speech_recognition as sr
import readNews
import random
import requests
import json


def getData(word):
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/"+word
    content = requests.get(url)
    jsonf = json.loads(content.content)
    meaning = jsonf[0]["meanings"][0]["definitions"][0]["definition"]
    print("Word:", jsonf[0]["word"])
    print("Meaning:", meaning)
    print("Example:", jsonf[0]["meanings"][0]["definitions"][0]["example"])
    
    speakAndPrint('Meaning of {} is {}'.format(word,meaning))

# generates random number between 1 and 6
def genran(): 
    return (random.randint(1,6))


def speakAndPrint(s):
    print(s)
    readNews.speak(s)

speakAndPrint("Speak any of the following  :")    
speakAndPrint("1. 'roll dice' to Roll the Dice and give you a random number")
speakAndPrint("2. 'read news' to Read Random news")
speakAndPrint("3. speak a word to get its meaning")
r=sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source,duration=2)
    speakAndPrint("Speak now:")
    print("Say Something")
    data = r.listen(source, timeout=3)
    try:
        text = r.recognize_google(data,language="en-IN")
        print("You just spoke: " ,text)
        spoke="You spoke :"+text
        readNews.speak(spoke)
        text=text.lower()
        if(text=="roll dice"):
            number =genran()
            speakAndPrint("Number is {}".format(number))
        elif(text=="read news"):
            readNews.callnewsapi()
        else:
            getData(text)
    except e:
        speakAndPrint("Some Error in detecting voice")
        print(e)
        
       
