from matrix_client.client import MatrixClient, MatrixHttpApi

class Cmatrix:
  def __init__(self, _serverUrl, _username, _pass, _roomId):  
    self.matrixClient = MatrixClient(_serverUrl)
    self.token = self.matrixClient.login(username = _username, password = _pass)
    self.api = MatrixHttpApi(_serverUrl, token = self.token)
    self.roomId = _roomId

  def sendMessage(self, message):
    response = self.api.send_message(self.roomId, message)
    return response