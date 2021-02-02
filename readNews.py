import json
import time
import requests
import win32com.client as wcm
def speak(s):
    speaker=wcm.Dispatch("SAPI.SpVoice")
    speaker.speak(s)

def callnewsapi():   
    content=requests.get("http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=fc8af4f60db94185adb3dc7ec59ba417")
    jsonformat=json.loads(content.content)
    for i in jsonformat["articles"]:
        if(type(i["author"])==str):
            print(i["title"]+" by "+i["author"])
            s=i["title"]+" by "+i["author"]
        else:
            print(i["title"])
            s=i["title"]
        speak(s)
        time.sleep(2)
        
if __name__ == "__main__":
    callnewsapi()

