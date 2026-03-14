import time
import os, sys
import colorama

from telethon.sync import TelegramClient
# Defining the ANSI color codes
R = "\033[31m"  # Red
G = "\033[32m"  # Green
W = "\033[0m"   # Reset to White/Default


groupId = "-1001892250906"
with open("Message.txt", "r", encoding="utf-8", errors="ignore") as f:
    msg = f.read()

count = 0
sent = 0
notSent = 0

def screen_clear():
    _ = os.system('clear')



j = 0
idList = []
def makeMessage(i):
    global count
    
    count += 1
    
    
    
    try:
        idList.append(i)
        if count % 9 == 0 and count > 1:
            msg2 = ""
            
            j = count - 9
            while j < count:
                
                msg2 = str(msg2)+" @"+str(idList[j])
                j += 1
            msg3 = str(msg)+str(msg2)       
            #print(msg3)
            send(msg3)
            time.sleep(900)
    except:
        pass
    
    

def send(msg3):
    global sent, notSent, count
    groupId = "8465974996"
    try:
        with TelegramClient(phone, api_id, api_hash) as client:
            client.start()
            client.send_message(int(groupId), str(msg))
            with open("Total-Sent.txt", "w", encoding="utf-8", errors="ignore") as f:
                f.write(str(count)+"\n")
            sent += 1
            #os.system(f"title : [+] RMYEN TELEGRAM SENDER - GOOD : {sent}  BAD : {notSent}")
            print(f"{G}[+] {W}{sent} sent success!")
    
    except:
        notSent += 1
        print(f"{R}[+] {W}{sent} Not sent.")
        #os.system(f"title : [+] RMYEN TELEGRAM SENDER - GOOD : {sent}  BAD : {notSent}")
            

api_id = "32197656"
api_hash = "915e75fd81437e420ac4e4ef1fbd37ef"
phone = "+21650894631"

def Connect():
    with TelegramClient(phone, api_id, api_hash) as client:
        client.send_code_request(phone)
        client.sign_in(phone, input('Enter the code (in your telegram app): '))

if __name__ == "__main__":
    screen_clear()
    #Connect()
    ids = input(f"{R}> {W}Enter Your Members Ids List: ")
    with open(ids, "r") as f:
        lines = f.readlines()
    
    for i in lines:
        i = i.strip()
        i = i.replace("\n", "")
        makeMessage(i)
