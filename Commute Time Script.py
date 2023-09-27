import datetime
import googlemaps
import requests

import config

def getCommuteTime():
    origin = config.origin # Origin Address
    destination = config.destination # Destination Address

    maps = googlemaps.Client(key = config.API_Key)

    dir = maps.directions(origin, destination)
    leg = dir[0]['legs'][0]
    commuteTime = leg['duration']['text']

    return commuteTime

def sendTxt(msg):
    chatId = config.chatId   # Your Telegram chat id
    botToken = config.botToken   # Telegram bot token

    requests.get(f"https://api.telegram.org/bot{botToken}/sendMessage?chat_id={chatId}&text={msg}")


def main():
    cTime = getCommuteTime()

    msg = f"Current ETA to destination is: {cTime}. "
    sendTxt(msg)

if __name__ == "__main__":
    main()