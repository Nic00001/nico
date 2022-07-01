#BoxplotLiveS
from datetime import datetime
from statistics import mean
import warnings
import json
import os

warnings.simplefilter(action="ignore", category=FutureWarning)
datef=[]
powerf=[]
datef2=[]

def Monday():
    path= r'Z:\Project1_Logs\Monday'
    os.chdir(path)

    day_of_week_container=[]
    date_format=[]
    logList = []
    raw_power_data=[]
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
                raw_power_data.append(data["Power"])
                pass            
            pass
            
        get_power_data_limited=(raw_power_data[-k+1:])    #correct
        mean_power= mean(get_power_data_limited)

        date_text=file2.replace('.txt', '')
        date_format.append(date_text)
        date_final_format= datetime.strptime(date_text, '%d_%m_%Y')
        day_of_week_format= (date_final_format.strftime('%A'))
        
        format_x = "{:.2f}".format(mean_power)
        sum_power.append(float(format_x))
        
        day_of_week_container.append(day_of_week_format)
        pass
    
    return day_of_week_container, sum_power, date_format

def Tuesday():            
    path= r'Z:\Project1_Logs\Tuesday'    
    os.chdir(path)

    day_of_week_container=[]
    date_format=[]
    logList = []
    raw_power_data=[]
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
                raw_power_data.append(data["Power"])
                pass            
            pass
            
        get_power_data_limited=(raw_power_data[-k+1:])    #correct
        mean_power= mean(get_power_data_limited)

        date_text=file2.replace('.txt', '')
        date_format.append(date_text)
        date_final_format= datetime.strptime(date_text, '%d_%m_%Y')
        day_of_week_format= (date_final_format.strftime('%A'))
        
        format_x = "{:.2f}".format(mean_power)
        sum_power.append(float(format_x))
        
        day_of_week_container.append(day_of_week_format)
        pass
    
    return day_of_week_container, sum_power, date_format


def Wednesday():            
    path= r'Z:\Project1_Logs\Wednesday'    
    os.chdir(path)

    day_of_week_container=[]
    date_format=[]
    logList = []
    raw_power_data=[]
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
                raw_power_data.append(data["Power"])
                pass            
            pass
            
        get_power_data_limited=(raw_power_data[-k+1:])    #correct
        mean_power= mean(get_power_data_limited)

        date_text=file2.replace('.txt', '')
        date_format.append(date_text)
        date_final_format= datetime.strptime(date_text, '%d_%m_%Y')
        day_of_week_format= (date_final_format.strftime('%A'))
        
        format_x = "{:.2f}".format(mean_power)
        sum_power.append(float(format_x))

        day_of_week_container.append(day_of_week_format)
        pass
    
    return day_of_week_container, sum_power, date_format


def Thursday():            
    path= r'Z:\Project1_Logs\Thursday'    
    os.chdir(path)

    day_of_week_container=[]
    date_format=[]
    logList = []
    raw_power_data=[]
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
                raw_power_data.append(data["Power"])
                pass            
            pass
            
        get_power_data_limited=(raw_power_data[-k+1:])    #correct
        mean_power= mean(get_power_data_limited)
        
        date_text=file2.replace('.txt', '')
        date_format.append(date_text)
        date_final_format= datetime.strptime(date_text, '%d_%m_%Y')
        day_of_week_format= (date_final_format.strftime('%A'))
        
        format_x = "{:.2f}".format(mean_power)
        sum_power.append(float(format_x))
        
        day_of_week_container.append(day_of_week_format)
        pass
    
    return day_of_week_container, sum_power, date_format


def Friday():            
    path= r'Z:\Project1_Logs\Friday'    
    os.chdir(path)

    day_of_week_container=[]
    date_format=[]
    logList = []
    raw_power_data=[]
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
                raw_power_data.append(data["Power"])
                pass
            
            pass
            
        get_power_data_limited=(raw_power_data[-k+1:])    #correct
        mean_power= mean(get_power_data_limited)

        date_text=file2.replace('.txt', '')
        date_format.append(date_text)
        date_final_format= datetime.strptime(date_text, '%d_%m_%Y')
        day_of_week_format= (date_final_format.strftime('%A'))
        
        format_x = "{:.2f}".format(mean_power)
        sum_power.append(float(format_x))
        
        day_of_week_container.append(day_of_week_format)
        pass
    return day_of_week_container, sum_power, date_format

def Saturday():
    path= r'Z:\Project1_Logs\Saturday'    
    os.chdir(path)

    day_of_week_container=[]
    date_format=[]
    logList = []
    raw_power_data=[]
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
                raw_power_data.append(data["Power"])
                pass            
            pass
            
        get_power_data_limited=(raw_power_data[-k+1:])    #correct
        mean_power= mean(get_power_data_limited)

        date_text=file2.replace('.txt', '')
        date_format.append(date_text)
        date_final_format= datetime.strptime(date_text, '%d_%m_%Y')
        day_of_week_format= (date_final_format.strftime('%A'))
        
        format_x = "{:.2f}".format(mean_power)
        sum_power.append(float(format_x))
        
        day_of_week_container.append(day_of_week_format)
        pass
    
    return day_of_week_container, sum_power, date_format

def Sunday():            
    path= r'Z:\Project1_Logs\Sunday'    
    os.chdir(path)

    day_of_week_container=[]
    date_format=[]
    logList = []
    raw_power_data=[]
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
                raw_power_data.append(data["Power"])
                pass            
            pass
            
        get_power_data_limited=(raw_power_data[-k+1:])    #correct
        mean_power= mean(get_power_data_limited)

        date_text=file2.replace('.txt', '')
        date_format.append(date_text)
        date_final_format= datetime.strptime(date_text, '%d_%m_%Y')
        day_of_week_format= (date_final_format.strftime('%A'))
        
        format_x = "{:.2f}".format(mean_power)
        sum_power.append(float(format_x))
        
        day_of_week_container.append(day_of_week_format)
        pass
    
    return day_of_week_container, sum_power, date_format
    