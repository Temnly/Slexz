import requests


def general():

 value = input("What do you want to download?")
 download_ask = input("\nPLEASE NOTE: You have to type in the file extension as well.\n\nAs what do you want to save it? ")
 r = requests.get(value)

 with open('/Users/tim/Downloads/' + download_ask, 'wb') as f:
    f.write(r.content)


 print("\nDownloaded!")