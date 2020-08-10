# JASON FILES
import json
from plyer import notification
import requests
import time


def getData(url):
    r = requests.get(url)
    return r.text


def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "D:\Covid19\Covid19.ico",
        timeout = 20
    )


while True:
    Covid19J = getData("https://api.covid19india.org/states_daily.json")
    Data = json.loads(Covid19J)
    # print(type(Data))
    a = Data["states_daily"]
    # print(type(a))
    # SD = a
    # for SD in a:
    #     print(SD)
    # LD = SD["mh"]
    # print(LD)

    if __name__ == '__main__':
        def GetData():
            a = Data["states_daily"]
            for SD in a:
                MD = SD["mh"]
                # print(MD)
                Save.append(MD)


        Save = []
        GetData()
        # print(Save)
        # print(len(Save))
        s = {"": Save[213:]}
        print(s)
        a = s[""]
        nTitle = "Maharashtra Covid-19 Cases"
        nText = f"Yesterday Details\n" \
                f"Confirmed : {a[0]}\n" \
                f"Recovered : {a[1]}\n" \
                f"Deaths : {a[2]}"
        notifyMe(nTitle, nText)
        time.sleep(5)
    time.sleep(60*60*24)
