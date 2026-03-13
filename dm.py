import time
import os, sys
import colorama

from telethon.sync import TelegramClient
# Defining the ANSI color codes
R = "\033[31m"  # Red
G = "\033[32m"  # Green
W = "\033[0m"   # Reset to White/Default


token = "8713699671:AAHwNw3WtYaxQIegAWFjI_83CO5opuZhV9Y"
with open("Message.txt", "r", encoding="utf-8", errors="ignore") as f:
    msg = f.read()

count = 0
sent = 0
notSent = 0

def screen_clear():
    _ = os.system('clear')

def send(lines):
    global count, sent, notSent, client
    with TelegramClient(phone, api_id, api_hash) as client:
        client.start()
        for i in lines:
            try:
                i = i.strip()
                i = i.replace("\n", "")
                print(client.send_message(int(i), str(msg)))
                with open("Sent.txt", "a", encoding="utf-8", errors="ignore") as f:
                    f.write(i+"\n")
                count += 1
                sent += 1
                #os.system(f"title : [+] RMYEN TELEGRAM SENDER - GOOD : {sent}  BAD : {notSent}")
                print(f"{G}[+] {W}{i} sent success!")
                if count % 10 == 0:
                    print(f"Total:{R} {count} {W}|{R} {sent} {W}Sended <3.")
                    print(f"{G} Waiting 1 Minute <3.{W}")
                    time.sleep(60)
    
            except:
                with open("Not-Sent.txt", "a", encoding="utf-8", errors="ignore") as f:
                    f.write(i+"\n")
                count += 1
                notSent += 1
                #os.system(f"title : [+] RMYEN TELEGRAM SENDER - GOOD : {sent}  BAD : {notSent}")
                if count % 10 == 0:
                    print(f"Total:{R} {count} {W}|{R} {sent} {W}Sended <3.")
                    print(f"{G} Waiting 1 Minute <3.{W}")
                    time.sleep(60)
                print(f"{R}[-] Total:{R} {count} {W}| {W}{i} Not sent.")
                print(f"{R} {notSent} {W}Total not sent.")

api_id = "32197656"
api_hash = "915e75fd81437e420ac4e4ef1fbd37ef"
phone = "+21650894631"

def Connect():
    with TelegramClient(phone, api_id, api_hash) as client:
        client.send_code_request(phone)
        client.sign_in(phone, input('Enter the code (in your telegram app): '))

if __name__ == "__main__":
    screen_clear()
    Connect()
    #ids = input(f"{R}> {W}Enter Your Members Ids List: ")
    #with open(ids, "r") as f:
        #lines = f.readlines()
    #send(lines)
