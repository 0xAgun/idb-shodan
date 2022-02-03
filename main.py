import argparse
import json
import requests
import concurrent.futures

parser = argparse.ArgumentParser(description="InternetDB Shodan tool Help Menu")
parser.add_argument('-F', '--file', metavar='', required=True, help="Enter the IPs loaded file")
parser.add_argument('-O', '--output', metavar='', help="Enter the Output File")

args = parser.parse_args()


banner = '''
\033[1;35m
    ██ ██████  ██████      ███████ ██   ██  ██████  ██████   █████  ███    ██ 
    ██ ██   ██ ██   ██     ██      ██   ██ ██    ██ ██   ██ ██   ██ ████   ██ 
    ██ ██   ██ ██████      ███████ ███████ ██    ██ ██   ██ ███████ ██ ██  ██ 
    ██ ██   ██ ██   ██          ██ ██   ██ ██    ██ ██   ██ ██   ██ ██  ██ ██ 
    ██ ██████  ██████      ███████ ██   ██  ██████  ██████  ██   ██ ██   ████\033[0m 
                     \033[1;34mAn Opensource OpenPort scanner for IPs from internetdb shodan\033[0m
                        \033[1;36m- Author: [0xAgun]\033[0m
        \033[1;33muse: python3 main.py -F filename.txt -O outputfile.txt\033[0m
        \033[1;33muse: python3 main.py -h\033[0m                                                              
'''

print(banner)

with open(args.file) as files:
    reading = files.readlines()
    j = [s.replace("\n", "") for s in reading]

def mainbody(urls):
    try:
        mainurl = "https://internetdb.shodan.io/"+urls
        send_req = requests.get(mainurl)
        gg = send_req.text
        kk = json.loads(gg)
        tres = f"\033[0;35mIP:\033[0m \033[0;36m{kk['ip']}\033[0m  \033[0;34mPORT: \033[0;31m{kk['ports']}\033[0m"
        ggs = f"IP: {kk['ip']} PORT: {kk['ports']}"
        print(tres)
        if args.output:
            fileopn = open(args.output, 'a')
            fileopn.write(ggs+"\n")
            fileopn.close()
    except Exception as e:
        pass


with concurrent.futures.ThreadPoolExecutor(20) as executor:
    executor.map(mainbody, j)
