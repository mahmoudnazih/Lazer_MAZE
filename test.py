import communication
import threading
import time
client = communication.Client()
flag = False
while True:
    data = client.info()
    flag = True
    if data =='1':
        score = 40
        while True:
            if flag:
                initialTime = time.time()
                flag = False   
                
            currentTime = time.time()-initialTime
            remainingTime = 5 - currentTime
            if remainingTime>0:
                print('Level One time:'+'\t'+str(remainingTime))
                if remainingTime>2 and remainingTime<3:
                    print('Turn 3 Btns On')
                else:
                    print('Turn 3 Btns Off')
            else:
                break
    if data =='2':
        score = 60
        while True:
            if flag:
                initialTime = time.time()
                flag = False   
                
            currentTime = time.time()-initialTime
            remainingTime = 10 - currentTime
            if remainingTime>0:
                print('Level Two time:'+'\t'+str(remainingTime))
                if remainingTime>5 and remainingTime<8:
                    print('Turn 3 Btns On')
            else:
                break

        
