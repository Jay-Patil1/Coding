# EXERCISE 9
# Akhbaar Padhke Sunaao

                    # SOLUTION

'''
Author: Jay Patil
Purpose: Learning Python
'''                    

import requests
import json
import time
def speak(str):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.SpVoice")

    speak.Speak(str)


if __name__ == '__main__':

    speak("News for today. Lets Begin.")
    url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=6ca312c53fb0435c9515ba2b63ae5853"
    news = requests.get(url).text
    news_dict = json.loads(news)
    # print(news_dict["articles"])
    arts = news_dict["articles"]

    for i in range(1,11):
        print(i)
        print(arts[i]['description'])
        speak(arts[i]['description'])
        time.sleep(2)
        if i>=11:
            break
        if i == 9:
            speak("So, the last news is..")
        if i < 9:
            speak("Moving on to the next news.")
    speak("Thanks for listening. Have a nice day.")
