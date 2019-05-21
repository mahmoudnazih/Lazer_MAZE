import communication
import sys

client = communication.Client()




while True:
    
    data = str(client.info())
    if data == '1':
        print('Level One')
        
    elif data == '2':
        print('Level Two')
    elif data == '3':
        print('Level Three')
    elif data == '4':
        print('Level Four')
    elif data=='stop':
        print('stop')
        
