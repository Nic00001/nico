# publisher
import paho.mqtt.client as mqtt
import json
from datetime import datetime
from time import time, sleep

file2= 'C:\\Users\\User1\\Desktop\\Py\\Json_text.json'

client = mqtt.Client()
'''client.connect('192.168.55.105', 9999)'''
client.connect('127.0.0.1',9999)

while True:
#sleep(60 - time() % 60) 
    v={}
    with open (file2, 'r') as f2:
      
        dt2= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        jb= json.loads(f2.read()) 
        v['Timestamp']=dt2
        v['voltage']= (jb['data']['voltage'])
        v['current']= (jb['data']['current'])
        v['power']= (jb['data']['apower'])
        d=json.dumps(v)   
        pass
    
    client.publish("Nico2topic/test",(d))   
    
    sleep(60)
    
