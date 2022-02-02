from ast import Lt
import time,os

while True:
    os.system('cls')
    Lt=time.localtime()
    result=time.strftime('%I:%M:%S %p',Lt)
    print(result)
    time.sleep(1)

