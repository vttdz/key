import os
import requests
from colorama import init, Fore, Style

init(autoreset=True)

keylist = ["xvtAb3xG5I", "WUCzz6lJiL", "admin", "iHXvBwGSty" ]
blacklist = ["CAB", "Axionix", "ABC", "123"]
webhook_url = "https://discord.com/api/webhooks/1295248104593031198/wTQWeZBfedh2UqLUCs--krKfV4MI5D6aajKddVRVjXw-Z8eiD91kn-DSc8iBGYUjTrdO"
key_file = "Key.bin"

def load_key():
    if os.path.exists(key_file):
        with open(key_file, "r") as f:
            return f.read().strip()
    return None

def save_key(key):
    with open(key_file, "w") as f:
        f.write(key)

input_key = load_key()

if input_key is None:
    print(Fore.GREEN + "REMAKE BY VTT" + Style.RESET_ALL)
    print(Fore.GREEN + "Wish You Have The Best Experience" + Style.RESET_ALL)
   
    
    print(Fore.RED + "This is a remake tool so it cannot avoid some errors from the original tool." + Style.RESET_ALL)
    input_key = input(Fore.YELLOW + "Please Enter Your Key: " + Style.RESET_ALL)
    print(Fore.CYAN + "If you don't have the key please DM me to get it" + Style.RESET_ALL)
    save_key(input_key)  

if input_key in blacklist:
    print(Fore.YELLOW + "Currently Whitelisting, Please Wait A Moment..." + Style.RESET_ALL)
    print(Fore.YELLOW + "Currently Whitelisting, Please Wait A Moment..." + Style.RESET_ALL)
    print(Fore.YELLOW + "Currently Whitelisting, Please Wait A Moment..." + Style.RESET_ALL)
    print(Fore.GREEN + "Key Check Done" + Style.RESET_ALL)
    print(Fore.RED + "Your Key Has Been Blacklisted" + Style.RESET_ALL)
    print(Fore.RED + "You Can't Use This Tool, Please Check Key Again Or Buy Key Again!" + Style.RESET_ALL)
    print(Fore.RED + "I Remind You That Your Key Has Been Blacklisted!" + Style.RESET_ALL)
    
    
    data = {
        "content": f"Someone Used VTT Tool With Blacklisted Key: {input_key}"
    }
    response = requests.post(webhook_url, json=data)

    if response.status_code == 204:
        print(Fore.GREEN + "Message Sent To VTT Webhook Successfully." + Style.RESET_ALL) 
    else:
        print(Fore.RED + f"An Error Occurred While Sending Message To VTT Webhook, Status Code Is: {response.status_code}" + Style.RESET_ALL)
    
    exit()

elif input_key in keylist:
    print(Fore.YELLOW + "Currently Whitelisting, Please Wait A Moment..." + Style.RESET_ALL)
    print(Fore.YELLOW + "Currently Whitelisting, Please Wait A Moment..." + Style.RESET_ALL)
    print(Fore.YELLOW + "Currently Whitelisting, Please Wait A Moment..." + Style.RESET_ALL)
    print(Fore.GREEN + "Key Check Done" + Style.RESET_ALL)
    print(Fore.GREEN + "Your Key Is Fine And Usable, Thank You For Using Tool" + Style.RESET_ALL)
    print(Fore.GREEN + "I Repeat That Your Key Is Correct And You Can Use The Tool" + Style.RESET_ALL)
    
    
    data = {
        "content": f"Someone Used VTT Tool With The Key Being: {input_key}"
    }
    response = requests.post(webhook_url, json=data)

    if response.status_code == 204:
        print(Fore.GREEN + "Message Sent To Axionix Webhook Successfully." + Style.RESET_ALL) 
    else:
        print(Fore.RED + f"An Error Occurred While Sending Message To  Webhook, Status Code Is: {response.status_code}" + Style.RESET_ALL)
else:
    print(Fore.YELLOW + "Currently Whitelisting, Please Wait A Moment..." + Style.RESET_ALL)
    print(Fore.YELLOW + "Currently Whitelisting, Please Wait A Moment..." + Style.RESET_ALL)
    print(Fore.YELLOW + "Currently Whitelisting, Please Wait A Moment..." + Style.RESET_ALL)
    print(Fore.GREEN + "Key Check Done" + Style.RESET_ALL)
    print(Fore.RED + "Your Key Is Wrong, Please Check And Try Again!" + Style.RESET_ALL)
    print(Fore.RED + "You Can't Use This Tool, Please Check Key Again Or Buy Key Again!" + Style.RESET_ALL)
    print(Fore.RED + "I Repeat Your Key Is Wrong!" + Style.RESET_ALL)
    
    
    data = {
        "content": f"Someone Used  Tool With Wrong Key: {input_key}"
    }
    response = requests.post(webhook_url, json=data)

    if response.status_code == 204:
        print(Fore.GREEN + "Message Sent To  Webhook Successfully." + Style.RESET_ALL) 
    else:
        print(Fore.RED + f"An Error Occurred While Sending Message To  Webhook, Status Code Is: {response.status_code}" + Style.RESET_ALL)
    
    exit()
