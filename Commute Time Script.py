import datetime
import googlemaps
import requests

import config

def getCommuteTime():
    origin = config.origin # Origin Address
    destination = config.destination # Destination Address
    
    maps = googlemaps.Client(key = config.API_Key)
    
    dir = maps.directions(origin, destination,alternatives=True,departure_time = datetime.datetime.now(), mode="driving", traffic_model="best_guess")

    legs = dict()

    for i in dir:
        legs.setdefault(i["summary"])
        legs[i["summary"]] = i["legs"][0]["duration"]["text"]

    result_list = []
    for key, value in legs.items():
        result_list.append(' '.join([key,':',value, "\n"]))

    message = ''.join(result_list)
    return message

def sendTxt(msg):
    chatId = config.chatId   # Your Telegram chat id
    botToken = config.botToken   # Telegram bot token

    requests.get(f"https://api.telegram.org/bot{botToken}/sendMessage?chat_id={chatId}&text={msg}")


def main():
    cTime = getCommuteTime()

    msg = f"Current ETA to destination is: \n{cTime}"
    sendTxt(msg)

if __name__ == "__main__":
    main()