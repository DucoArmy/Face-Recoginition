import threading
import asyncio
import requests
class NetworkManager:
    def __init__(self, names, url="http://localhost:8000"):
        self.data = []
        self.url = url
        for item in names:
            self.data.append([item, 100])

        threading.Timer(5, self.timeProgress).start()

    def timeProgress(self):
        for item in self.data:
            item[1] -= 5
    
    def postData(self, path, json):
        try:
            print(asyncio.run(self.send("post", path, json)))
        except:
            pass

    async def send(self, method, path, json):
        return requests.post(self.url + path, json=json)
