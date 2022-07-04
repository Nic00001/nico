# subscriber2
import datetime 
import paho.mqtt.client as mqtt


current_time = datetime.datetime.now()
a = current_time.strftime("%H_%M")

file='C:\\Users\\User1\\Desktop\\Py\\Testlogs\\'+a+'.txt'

client = mqtt.Client()
client.connect('192.168.55.105', 9999)
'''client.connect('127.0.0.1', 9999)'''

def on_connect(client, userdata, flags, rc):
    print("Connected to a broker!")
    client.subscribe("Nicotopic/test")
  

def on_message(client, userdata, message):
    print({message.payload.decode()})
    d=message.payload.decode()
    
    current_time = datetime.datetime.now()
    a = current_time.strftime("%H_%M")
    file='C:\\Users\\User1\\Desktop\\Py\\TestLogs\\'+a+'.txt'
    with open(file, 'a') as f:
        f.write(d+"\n")
        pass
          
while True:
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever() 
    current_time = datetime.datetime.now()
    a = current_time.strftime("%H_%M")
    file='C:\\Users\\User1\\Desktop\\Py\\TestLogs'+a+'.txt'
    with open(file,'w')as f:
        pass