import json

def readJson(arxiu):
  with open(str(arxiu)) as conf_file:
    variable = json.load(conf_file)
  return variable

def writeJson(variable, arxiu):
  with open(str(arxiu), 'w+') as conf_file:
    json.dump(variable,conf_file)