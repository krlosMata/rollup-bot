
import time, sys 
from pathlib import Path
from matrixUtils import Cmatrix
from rollupApi import CrollupApi
from utils import *

## Global variablesç
TIMEOUT = 3 * 60
lastBatchSynched = 0

## Path configuration file
configPath = Path.cwd().joinpath("config.json")

## Load configuration file
config = readJson(configPath)

## Load Matrix client
serverUrlMatrix = config["matrix"]["server"]
userMatrix = config["matrix"]["user"]
passMatrix = config["matrix"]["pass"]
roomMatrix = config["matrix"]["roomId"]
matrixClient = Cmatrix(serverUrlMatrix, userMatrix, passMatrix, roomMatrix)

## Load rollup client
urlRollup = config["rollup"]["url"]
lastAccount = config["rollup"]["lastAccount"]
rollupClient = CrollupApi("https://zkrollup.iden3.net")

while True:
  try:
    infoTime = "TIME: {}\n".format(time.strftime("%d/%m/%Y - %H:%M:%S"))
    message = infoTime

    # Check if query has been done correctly
    try:
      lastBatch = rollupClient.getState()['rollupSynch']['lastBatchSynched']
    except:
      message += "MESSAGE: Not possible to get rollup state"
      matrixClient.sendMessage(message)
      sys.exit()

    # Check if batch has increased correctly
    if ( lastBatch < lastBatchSynched ):
      message += "MESSAGE: Last batch has not been increased properly"
      matrixClient.sendMessage(message)
      sys.exit()
    else:
      lastBatchSynched = lastBatch

    # Check if a new account has been added
    try:
      rollupClient.getAccount(lastAccount + 1)
      message += "MESSAGE: new account has been added\n"
      message += "TOTAL ACCOUNTS: " + str(lastAccount + 1)
      lastAccount = lastAccount + 1
      matrixClient.sendMessage(message)
    except:
      doNothing = True

  except Exception as e: 
    line = sys.exc_info()[-1].tb_lineno
    print('Exception in line: {}\n {}'.format(line,e), flush = True)
  time.sleep(TIMEOUT)