import serial.tools.list_ports
import serial
import time
import datetime
import json

AVports =[comport.device for comport in serial.tools.list_ports.comports()]
print(str(AVports))
index = int(input("escolhe"))
ser = serial.Serial(AVports[index], 9600, timeout=1)
time.sleep(3)

while True:
    try:
        ser.write(b'u')
        moist = int(ser.readline())
        ser.write(b'l')
        light = int(ser.readline())
    except:
        continue
    with open("log.json", "r+") as resultsFile:
        try:
            log = json.loads(resultsFile.read())
        except:
            log = {
                'log':[]
            }
        log['log'].append({
        'value': moist,
        'light': light,
        'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
        wr = json.dumps(log)
        resultsFile.seek(0)
        resultsFile.truncate()
        resultsFile.write(wr)
        resultsFile.seek(0)
        time.sleep(60)
