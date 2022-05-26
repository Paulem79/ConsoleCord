import requests
import time
from colorama import Fore
import os
import ctypes
from util.plugins.commun import * 
from cc import main

def webhookspam():
    antiratelimit = 0
    setTitle("WebHook Spammer")
    clear()
    webhspamtitle()
    print(f"""{y}[{w}+{y}]{w} Webhooks url for spam """)
    webhook = input(f"""{y}[{b}#{y}]{w} WebHooks: """)
    print(f"""\n{y}[{w}+{y}]{w} Message to spam """)
    message = input(f"""{y}[{b}#{y}]{w} Message: """)
    print(f"""\n{y}[{w}+{y}]{w} Amount of time for the attack (s) """)
    timer = input(f"""{y}[{b}#{y}]{w} Amount: """)
    print(f"""\n{y}[{w}+{y}]{w} Anti Rate-Limit ? (Y/N)""")
    ratelimit = input(f"""{y}[{b}#{y}]{w} Response : """)
    print(f"""{y}[{w}+{y}]{w} {r}ALPHA{w} Create Webhhok to bypass Rate-Limit ? (Y/N)""")
    bypassratelimit = input(f"""{y}[{b}#{y}]{w} Bypass ? : """)
    if bypassratelimit == "Y" or "y" or "yes":
        print(f"""{y}[{w}+{y}]{w} {r}ALPHA{w} Put a channel ID to activate the system : """)
        chidwh = input(f"""{y}[{b}#{y}]{w} Channel ID : """)
    input(f"""\n\n{y}[{b}#{y}]{w} Press ENTER to Valid""")

    #message.channel.create_webhook(name="mywebhook")
    try:
        timeout = time.time() + 1 * float(timer)

        while time.time() < timeout:
            response = requests.post(
                webhook,
                json = {"content" : message},
                params = {'wait' : True}
            )
            if antiratelimit != 30:
                if response.status_code == 204 or response.status_code == 200:
                    print(f"""{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Message sent""")
                    if ratelimit == "y" or "Y" or "yes":
                        antiratelimit += 1
                elif response.status_code == 429:
                    print(f"""{y}[{Fore.LIGHTRED_EX }!{y}]{w} Rate limited ({response.json()['retry_after']}ms)""")
                    time.sleep(response.json()["retry_after"] / 1000)
                else:
                    print(f"""{y}[{Fore.LIGHTRED_EX }!{y}]{w} Error code: {response.status_code}""")
            else:
                print("Anti Rate-Limit, pause for 15 seconds")
                time.sleep(15)
                antiratelimit = 0
    except:
        print(f"""      {y}[{Fore.LIGHTRED_EX }!{y}]{w} Your request is invalid !""")
        time.sleep(2)
        clear()
        main()

    clear()
    webhspamtitle()
    print(f"""{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Webhook has been spammed""")
    input(f"""\n{y}[{b}#{y}]{w} Press ENTER to exit""")
    main()
    
webhookspam()
