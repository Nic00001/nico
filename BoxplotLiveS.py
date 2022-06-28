<<<<<<< HEAD
#BoxplotLiveS
import json
from datetime import datetime
from statistics import mean

import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import json
from statistics import mean
import os

import matplotlib.pyplot as plt
from datetime import datetime


datef=[]
powerf=[]
datef2=[]

def Monday():
#Path to Monday
            
    path= r'Z:\Project1_Logs\Monday'
    #path= r'C:\Users\User1\Desktop\Project_1\Project1_Logs\Tuesday'
    
    os.chdir(path)

    date_data=[]
    date_data2=[]
    logList = []
    power_data=[]
    sum_power=[]
    for file2 in os.listdir():
        
        with open(file2,'r')as f2:
            d=(f2.read())
            k=d.count('Power')


        with open(file2,'r') as f:

            for jsonObj in f:
                dict_Log = json.loads(jsonObj)
                logList.append(dict_Log)

        
            for data in logList:
                power_data.append(data["Power"])
                pass
            
            pass
            
        x2=(power_data[-k+1:])    #correct
        meanx= mean(x2)

        date=file2.replace('.txt', '')
        date_data2.append(date)
        date2= datetime.strptime(date, '%d_%m_%Y')
        dateF= (date2.strftime('%A'))
        
        format_x = "{:.2f}".format(meanx)
        sum_power.append(float(format_x))
        
        date_data.append(dateF)
        pass
    

    return date_data, sum_power, date_data2

def Tuesday():
    #Path to Monday
            
    path= r'Z:\Project1_Logs\Tuesday'
    #path= r'C:\Users\User1\Desktop\Project_1\Project1_Logs\Tuesday'
    
    os.chdir(path)

    date_data=[]
    date_data2=[]
    logList = []
    power_data=[]
    sum_power=[]
    for file2 in os.listdir():
        
        with open(file2,'r')as f2:
            d=(f2.read())
            k=d.count('Power')


        with open(file2,'r') as f:

            for jsonObj in f:
                dict_Log = json.loads(jsonObj)
                logList.append(dict_Log)

        
            for data in logList:
                power_data.append(data["Power"])
                pass
            
            pass
            
        x2=(power_data[-k+1:])    #correct
        meanx= mean(x2)

        date=file2.replace('.txt', '')
        date_data2.append(date)
        date2= datetime.strptime(date, '%d_%m_%Y')
        dateF= (date2.strftime('%A'))
        
        format_x = "{:.2f}".format(meanx)
        sum_power.append(float(format_x))
        
        date_data.append(dateF)
        pass
    

    return date_data, sum_power, date_data2


def Wednesday():
    #Path to Monday
            
    path= r'Z:\Project1_Logs\Wednesday'
    #path= r'C:\Users\User1\Desktop\Project_1\Project1_Logs\Tuesday'
    
    os.chdir(path)

    date_data=[]
    date_data2=[]
    logList = []
    power_data=[]
    sum_power=[]
    for file2 in os.listdir():
        
        with open(file2,'r')as f2:
            d=(f2.read())
            k=d.count('Power')


        with open(file2,'r') as f:

            for jsonObj in f:
                dict_Log = json.loads(jsonObj)
                logList.append(dict_Log)

        
            for data in logList:
                power_data.append(data["Power"])
                pass
            
            pass
            
        x2=(power_data[-k+1:])    #correct
        meanx= mean(x2)

        date=file2.replace('.txt', '')
        date_data2.append(date)
        date2= datetime.strptime(date, '%d_%m_%Y')
        dateF= (date2.strftime('%A'))
        
        format_x = "{:.2f}".format(meanx)
        sum_power.append(float(format_x))
        
        date_data.append(dateF)
        pass
    

    return date_data, sum_power, date_data2


def Thursday():
    #Path to Monday
            
    path= r'Z:\Project1_Logs\Thursday'
    #path= r'C:\Users\User1\Desktop\Project_1\Project1_Logs\Tuesday'
    
    os.chdir(path)

    date_data=[]
    date_data2=[]
    logList = []
    power_data=[]
    sum_power=[]
    for file2 in os.listdir():
        
        with open(file2,'r')as f2:
            d=(f2.read())
            k=d.count('Power')


        with open(file2,'r') as f:

            for jsonObj in f:
                dict_Log = json.loads(jsonObj)
                logList.append(dict_Log)

        
            for data in logList:
                power_data.append(data["Power"])
                pass
            
            pass
            
        x2=(power_data[-k+1:])    #correct
        meanx= mean(x2)
        
        date=file2.replace('.txt', '')
        date_data2.append(date)
        date2= datetime.strptime(date, '%d_%m_%Y')
        dateF= (date2.strftime('%A'))
        
        format_x = "{:.2f}".format(meanx)
        sum_power.append(float(format_x))
        
        date_data.append(dateF)
        pass
    

    return date_data, sum_power, date_data2


def Friday():
    #Path to Monday
            
    path= r'Z:\Project1_Logs\Friday'
    #path= r'C:\Users\User1\Desktop\Project_1\Project1_Logs\Tuesday'
    
    os.chdir(path)

    date_data=[]
    date_data2=[]
    logList = []
    power_data=[]
    sum_power=[]
    for file2 in os.listdir():
        
        with open(file2,'r')as f2:
            d=(f2.read())
            k=d.count('Power')


        with open(file2,'r') as f:

            for jsonObj in f:
                dict_Log = json.loads(jsonObj)
                logList.append(dict_Log)

        
            for data in logList:
                power_data.append(data["Power"])
                pass
            
            pass
            
        x2=(power_data[-k+1:])    #correct
        meanx= mean(x2)

        date=file2.replace('.txt', '')
        date_data2.append(date)
        date2= datetime.strptime(date, '%d_%m_%Y')
        dateF= (date2.strftime('%A'))
        
        format_x = "{:.2f}".format(meanx)
        sum_power.append(float(format_x))
        
        date_data.append(dateF)
        pass
    

    return date_data, sum_power, date_data2

def Saturday():
    #Path to Monday
            
    path= r'Z:\Project1_Logs\Saturday'
    #path= r'C:\Users\User1\Desktop\Project_1\Project1_Logs\Tuesday'
    
    os.chdir(path)

    date_data=[]
    date_data2=[]
    logList = []
    power_data=[]
    sum_power=[]
    for file2 in os.listdir():
        
        with open(file2,'r')as f2:
            d=(f2.read())
            k=d.count('Power')


        with open(file2,'r') as f:

            for jsonObj in f:
                dict_Log = json.loads(jsonObj)
                logList.append(dict_Log)

        
            for data in logList:
                power_data.append(data["Power"])
                pass
            
            pass
            
        x2=(power_data[-k+1:])    #correct
        meanx= mean(x2)

        date=file2.replace('.txt', '')
        date_data2.append(date)
        date2= datetime.strptime(date, '%d_%m_%Y')
        dateF= (date2.strftime('%A'))
        
        format_x = "{:.2f}".format(meanx)
        sum_power.append(float(format_x))
        
        date_data.append(dateF)
        pass
    

    return date_data, sum_power, date_data2

def Sunday():
    #Path to Monday
            
    path= r'Z:\Project1_Logs\Sunday'
    #path= r'C:\Users\User1\Desktop\Project_1\Project1_Logs\Tuesday'
    
    os.chdir(path)

    date_data=[]
    date_data2=[]
    logList = []
    power_data=[]
    sum_power=[]
    for file2 in os.listdir():
        
        with open(file2,'r')as f2:
            d=(f2.read())
            k=d.count('Power')


        with open(file2,'r') as f:

            for jsonObj in f:
                dict_Log = json.loads(jsonObj)
                logList.append(dict_Log)

        
            for data in logList:
                power_data.append(data["Power"])
                pass
            
            pass
            
        x2=(power_data[-k+1:])    #correct
        meanx= mean(x2)

        date=file2.replace('.txt', '')
        date_data2.append(date)
        date2= datetime.strptime(date, '%d_%m_%Y')
        dateF= (date2.strftime('%A'))
        
        format_x = "{:.2f}".format(meanx)
        sum_power.append(float(format_x))
        
        date_data.append(dateF)
        pass
    

    return date_data, sum_power, date_data2
=======
#BoxplotLiveS
import json
from datetime import datetime
from statistics import mean

import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import json
from statistics import mean
import os

import matplotlib.pyplot as plt
from datetime import datetime


datef=[]
powerf=[]
datef2=[]

def Monday():
#Path to Monday
            
    path= r'Z:\Project1_Logs\Monday'
    #path= r'C:\Users\User1\Desktop\Project_1\Project1_Logs\Tuesday'
    
    os.chdir(path)

    date_data=[]
    date_data2=[]
    logList = []
    power_data=[]
    sum_power=[]
    for file2 in os.listdir():
        
        with open(file2,'r')as f2:
            d=(f2.read())
            k=d.count('Power')


        with open(file2,'r') as f:

            for jsonObj in f:
                dict_Log = json.loads(jsonObj)
                logList.append(dict_Log)

        
            for data in logList:
                power_data.append(data["Power"])
                pass
            
            pass
            
        x2=(power_data[-k+1:])    #correct
        meanx= mean(x2)

        date=file2.replace('.txt', '')
        date_data2.append(date)
        date2= datetime.strptime(date, '%d_%m_%Y')
        dateF= (date2.strftime('%A'))
        
        format_x = "{:.2f}".format(meanx)
        sum_power.append(float(format_x))
        
        date_data.append(dateF)
        pass
    

    return date_data, sum_power, date_data2

def Tuesday():
    #Path to Monday
            
    path= r'Z:\Project1_Logs\Tuesday'
    #path= r'C:\Users\User1\Desktop\Project_1\Project1_Logs\Tuesday'
    
    os.chdir(path)

    date_data=[]
    date_data2=[]
    logList = []
    power_data=[]
    sum_power=[]
    for file2 in os.listdir():
        
        with open(file2,'r')as f2:
            d=(f2.read())
            k=d.count('Power')


        with open(file2,'r') as f:

            for jsonObj in f:
                dict_Log = json.loads(jsonObj)
                logList.append(dict_Log)

        
            for data in logList:
                power_data.append(data["Power"])
                pass
            
            pass
            
        x2=(power_data[-k+1:])    #correct
        meanx= mean(x2)

        date=file2.replace('.txt', '')
        date_data2.append(date)
        date2= datetime.strptime(date, '%d_%m_%Y')
        dateF= (date2.strftime('%A'))
        
        format_x = "{:.2f}".format(meanx)
        sum_power.append(float(format_x))
        
        date_data.append(dateF)
        pass
    

    return date_data, sum_power, date_data2


def Wednesday():
    #Path to Monday
            
    path= r'Z:\Project1_Logs\Wednesday'
    #path= r'C:\Users\User1\Desktop\Project_1\Project1_Logs\Tuesday'
    
    os.chdir(path)

    date_data=[]
    date_data2=[]
    logList = []
    power_data=[]
    sum_power=[]
    for file2 in os.listdir():
        
        with open(file2,'r')as f2:
            d=(f2.read())
            k=d.count('Power')


        with open(file2,'r') as f:

            for jsonObj in f:
                dict_Log = json.loads(jsonObj)
                logList.append(dict_Log)

        
            for data in logList:
                power_data.append(data["Power"])
                pass
            
            pass
            
        x2=(power_data[-k+1:])    #correct
        meanx= mean(x2)

        date=file2.replace('.txt', '')
        date_data2.append(date)
        date2= datetime.strptime(date, '%d_%m_%Y')
        dateF= (date2.strftime('%A'))
        
        format_x = "{:.2f}".format(meanx)
        sum_power.append(float(format_x))
        
        date_data.append(dateF)
        pass
    

    return date_data, sum_power, date_data2


def Thursday():
    #Path to Monday
            
    path= r'Z:\Project1_Logs\Thursday'
    #path= r'C:\Users\User1\Desktop\Project_1\Project1_Logs\Tuesday'
    
    os.chdir(path)

    date_data=[]
    date_data2=[]
    logList = []
    power_data=[]
    sum_power=[]
    for file2 in os.listdir():
        
        with open(file2,'r')as f2:
            d=(f2.read())
            k=d.count('Power')


        with open(file2,'r') as f:

            for jsonObj in f:
                dict_Log = json.loads(jsonObj)
                logList.append(dict_Log)

        
            for data in logList:
                power_data.append(data["Power"])
                pass
            
            pass
            
        x2=(power_data[-k+1:])    #correct
        meanx= mean(x2)
        
        date=file2.replace('.txt', '')
        date_data2.append(date)
        date2= datetime.strptime(date, '%d_%m_%Y')
        dateF= (date2.strftime('%A'))
        
        format_x = "{:.2f}".format(meanx)
        sum_power.append(float(format_x))
        
        date_data.append(dateF)
        pass
    

    return date_data, sum_power, date_data2


def Friday():
    #Path to Monday
            
    path= r'Z:\Project1_Logs\Friday'
    #path= r'C:\Users\User1\Desktop\Project_1\Project1_Logs\Tuesday'
    
    os.chdir(path)

    date_data=[]
    date_data2=[]
    logList = []
    power_data=[]
    sum_power=[]
    for file2 in os.listdir():
        
        with open(file2,'r')as f2:
            d=(f2.read())
            k=d.count('Power')


        with open(file2,'r') as f:

            for jsonObj in f:
                dict_Log = json.loads(jsonObj)
                logList.append(dict_Log)

        
            for data in logList:
                power_data.append(data["Power"])
                pass
            
            pass
            
        x2=(power_data[-k+1:])    #correct
        meanx= mean(x2)

        date=file2.replace('.txt', '')
        date_data2.append(date)
        date2= datetime.strptime(date, '%d_%m_%Y')
        dateF= (date2.strftime('%A'))
        
        format_x = "{:.2f}".format(meanx)
        sum_power.append(float(format_x))
        
        date_data.append(dateF)
        pass
    

    return date_data, sum_power, date_data2

def Saturday():
    #Path to Monday
            
    path= r'Z:\Project1_Logs\Saturday'
    #path= r'C:\Users\User1\Desktop\Project_1\Project1_Logs\Tuesday'
    
    os.chdir(path)

    date_data=[]
    date_data2=[]
    logList = []
    power_data=[]
    sum_power=[]
    for file2 in os.listdir():
        
        with open(file2,'r')as f2:
            d=(f2.read())
            k=d.count('Power')


        with open(file2,'r') as f:

            for jsonObj in f:
                dict_Log = json.loads(jsonObj)
                logList.append(dict_Log)

        
            for data in logList:
                power_data.append(data["Power"])
                pass
            
            pass
            
        x2=(power_data[-k+1:])    #correct
        meanx= mean(x2)

        date=file2.replace('.txt', '')
        date_data2.append(date)
        date2= datetime.strptime(date, '%d_%m_%Y')
        dateF= (date2.strftime('%A'))
        
        format_x = "{:.2f}".format(meanx)
        sum_power.append(float(format_x))
        
        date_data.append(dateF)
        pass
    

    return date_data, sum_power, date_data2

def Sunday():
    #Path to Monday
            
    path= r'Z:\Project1_Logs\Sunday'
    #path= r'C:\Users\User1\Desktop\Project_1\Project1_Logs\Tuesday'
    
    os.chdir(path)

    date_data=[]
    date_data2=[]
    logList = []
    power_data=[]
    sum_power=[]
    for file2 in os.listdir():
        
        with open(file2,'r')as f2:
            d=(f2.read())
            k=d.count('Power')


        with open(file2,'r') as f:

            for jsonObj in f:
                dict_Log = json.loads(jsonObj)
                logList.append(dict_Log)

        
            for data in logList:
                power_data.append(data["Power"])
                pass
            
            pass
            
        x2=(power_data[-k+1:])    #correct
        meanx= mean(x2)

        date=file2.replace('.txt', '')
        date_data2.append(date)
        date2= datetime.strptime(date, '%d_%m_%Y')
        dateF= (date2.strftime('%A'))
        
        format_x = "{:.2f}".format(meanx)
        sum_power.append(float(format_x))
        
        date_data.append(dateF)
        pass
    

    return date_data, sum_power, date_data2
>>>>>>> e8ef55a15fcaadd0bef0181c425ded070971dd49
    