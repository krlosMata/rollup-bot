import requests

class CrollupApi:
  def __init__(self, _baseUrl):
    self.url = _baseUrl    

  def getState(self):
    url = self.url + "/state"
    return requests.get(url).json()

  def getAccount(self, _id):
    url = self.url + "/accounts/" + str(_id) 
    return requests.get(url).json()