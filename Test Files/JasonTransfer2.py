import json
from datetime import datetime

def kkk(file2):
    with open(file2, 'r')as f:
        
        j= json.loads(f.read()) 
        
        j2= (j['data']['voltage'])
        j3= (j['data']['current'])
        j4= (j['data']['apower'])
        
        
        dt= dt= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print("\n timestamp:",dt," voltage:",j2,",  current:",j3,",  power:",j4,"\n")
        #jt2= ("\n timestamp:",dt," voltage:",j2,",  current:",j3,",  power:",j4,"\n")
        pass 

    
def kkk2(file1,file2):
    v={}
    dt2= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open (file2, 'r') as f2:
        
        jb= json.loads(f2.read()) 
        v['Timestamp']=dt2
        v['voltage']= (jb['data']['voltage'])
        v['current']= (jb['data']['current'])
        v['power']= (jb['data']['apower'])
        
      
        
        with open(file1, 'a')as f:
            d=json.dumps(v)
            f.write (d + ('\n'))
            pass
        
        pass
    
    
