'''
Author: Jay Patil
Purpose: Learning Notifications using Python
'''

from plyer import notification
import requests
from bs4 import BeautifulSoup
import time
NoOfTimesNotified = 0



def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\\Covid19\\Covid19.ico",
        timeout = 20
    )


def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == '__main__':
    while True:
        # notifyMe("Jay", "Let's stop the spread of this virus together.")
        myHtmlData = getData("https://www.mohfw.gov.in/")
        # print(myHtmlData)
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())
        myDataStr = ""
        
        J = 1
        if J == 1:
            NoOfTimesNotified = NoOfTimesNotified + 1
            print(f"Notification Occured for {NoOfTimesNotified} Times.")
        if NoOfTimesNotified == (12*24):
            exit()
        for tr in soup.find_all('tbody')[0].find_all("tr"):
            myDataStr += tr.get_text()
            

        myDataStr = myDataStr[1:]
        itemList = myDataStr.split("\n\n")


        states = ["Delhi", "Karnataka", "Maharashtra", "Tamil Nadu"]
        for item in itemList[0:34]:
            dataList = item.split("\n")
            if dataList[1] in states:
                # print(dataList)
                nTitle = 'Covid-19 Cases'
                nText = f"{dataList[1]}\nTotal Cases: {dataList[2]}\n" \
                        f"Cured/Migrated : {dataList[3]}\nDeaths : {dataList[4]}"
                notifyMe(nTitle, nText)
                time.sleep(8)
        time.sleep(60)
