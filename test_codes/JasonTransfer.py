import JasonTransfer2 as jt
file2= 'C:\\Users\\User1\\Desktop\\Py\\Json_text.json'
file1= 'C:\\Users\\User1\\Desktop\\Py\Json_text.txt'
#from time import time, sleep 
import time
    
def main():
    while True:
        #sleep(60 - time() % 60)
        
        time.sleep(5)
        
        jt.kkk(file2)
        
        jt.kkk2(file1, file2)
        
if __name__ == '__main__':
    main()
        