'''
Author: Jay Patil
Purpose: Learning Notifications using Python
'''

import json
import requests
import time
from plyer import notification
NoOfTimesNotified = 0

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\Covid19\Covid19.ico",
        timeout = 10
    )


def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == '__main__':
    while True:
        d = getData("https://api.covid19india.org/state_district_wise.json")
        Data = json.loads(d)
        a = Data["Maharashtra"]
        # print(type(Data)
        # print(Data.keys())
        # print(type(a))
        # print(a.keys())
        b = a["districtData"]
        # print(b.keys())
        Sangli = b["Sangli"]
        # print(Sangli)

        J = 1
        if J == 1:
            NoOfTimesNotified = NoOfTimesNotified + 1
            print(f"Notification Occured for {NoOfTimesNotified} Times.")
        if J == 12*24:
            exit()

        A = Sangli["active"]
        C = Sangli["confirmed"]
        D = Sangli["deceased"]
        R = Sangli["recovered"]
        nTitle = "Sangli Covid-19 Cases"
        nText = f"Confirmed : {C}\n" \
                f"Active : {A}\n" \
                f"Recovered : {R}\n" \
                f"Deaths : {D}"
        notifyMe(nTitle, nText)
        time.sleep(60*5)
