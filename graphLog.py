import matplotlib.pyplot as plt
import json


with open("log.json") as logJson:
     log = json.loads(logJson.read())['log']

things = int(input("Quantos elementos?\n"))
plt.plot([int(x['time'].replace("-","").replace(":", "").replace(" ","")) for x in log][-things:], [(100 - x['value']*(100/1023)) for x in log][-things:])
plt.show()
