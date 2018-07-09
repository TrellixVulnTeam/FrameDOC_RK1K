import geoip2.database 
from termcolor import cprint, colored
import os
from urllib.request import urlopen 
import os


def connection(host='http://duckduckgo.com'): 
    try: 
        urlopen(host) 
        return True 
    except: 
        return False


def NoCon(): 
    cprint("""
    __      _____    ___ ___ 
    \ \    / /_ _|__| __|_ _|
     \ \/\/ / | |___| _| | | 
      \_/\_/ |___|  |_| |___|
                 mm
              /^(  )^\  
              \,(..),/                
                V~~V           
                                      
      [!] Network error. Verify your Connection.\n                                     """, "green")
    exit(1)


if connection() == False: 
    print(NoCon())

def anime(): 
    animation = "|/-\\" 
    for i in range(19): 
        time.sleep(0.1) 
        s.stdout.write(f'\r' + animation[i % len(animation)]) 
        s.stdout.flush() 

def Ip():
    
    
    reader = geoip2.database.Reader('./GeoLite2-City_20180703/GeoLite2-City.mmdb') 
    print("\n")
    print("[!]Make sure to add the Ipv4 or Ipv6")
    print("")
    input("\033[1;91mTRace people by Ip. Enter to continue....\033[1;m ")
    print("\n")
    ip = input("\033[1;91m>FrameDOC@Enter IP addres:\033[1;m ") 
    res = reader.city(ip) 
    print(f"[+]Country - {res.country.iso_code}") 
    print(f"[+]State Info - {res.subdivisions.most_specific.name}")
    print(f"[+]More info - {res.subdivisions.most_specific.iso_code}") 
    print(f"[+]City Name - {res.city.name}") 
    print(f"[+]Postal Code - {res.postal.code}")
    reader.close()



def banner(): 
    os.system('clear && clear')
    x = colored('*B^)', 'blue')
    cprint("                        _..-'(                       )`-.._", 'red', attrs=['bold'] )
    cprint("	           ./'. '||\\.       (\_/)        .//||` .`\.", 'red', attrs=['bold'])
    cprint("                  '.|'.'||||\\|..    )-.-(     ..|//||||`.`|.`\.", 'red', attrs=['bold'])
    cprint("               '..|'.|| |||||\```````     '''''''/||||| ||.`|..`\.", 'red', attrs=['bold'])
    cprint("              '.||'.|||| |||||||||||\.     ./||||||||||| ||||.`||.`\.", 'red', attrs=['bold'])
    cprint("	    /'|||'.|||||| |||||||||||{     }||||||||||||| ||||||.`|||`\ ", 'red', attrs=['bold'])
    cprint("	  .|||'.||||||| |||||||||||||{     }|||||||||||| |||||||.`|||.` ", 'red', attrs=['bold'])
    cprint("	 '.||| ||||||||| |/'   ``\||/`     '\||/''   `\| ||||||||| |||.`  ", 'red', attrs=['bold'])
    cprint("         |/' \./'     `\./          |/\   /\|          \./'     `\./ `\|   ", 'red', attrs=['bold']) 
    cprint("	 V    V         V          }' `\ /' `{          V         V    V    ", 'red', attrs=['bold'])
    cprint("         `    '         '               V               '         '    '     ", 'red', attrs=['bold'])                                                                            
    cprint("  ########:'########:::::'###::::'##::::'##:'########:::'#######:::'######::", 'red', attrs=['bold'])
    cprint("  ##.....:: ##.... ##:::'## ##::: ###::'###: ##.... ##:'##.... ##:'##... ##:", 'red', attrs=['bold'])
    cprint("  ##::::::: ##:::: ##::'##:. ##:: ####'####: ##:::: ##: ##:::: ##: ##:::..::", 'red', attrs=['bold'])
    cprint("  ######::: ########::'##:::. ##: ## ### ##: ##:::: ##: ##:::: ##: ##:::::::", 'red', attrs=['bold']) 
    cprint("  ##...:::: ##.. ##::: #########: ##. #: ##: ##:::: ##: ##:::: ##: ##:::::::", 'red', attrs=['bold'])
    cprint("  ##::::::: ##::. ##:: ##.... ##: ##:.:: ##: ##:::: ##: ##:::: ##: ##::: ##:", 'red', attrs=['bold'])
    cprint("  ##::::::: ##:::. ##: ##:::: ##: ##:::: ##: ########::. #######::. ######::", 'red', attrs=['bold'])
    cprint("  ..::::::::..:::::..::..:::::..::..:::::..::........::::.......::::......::", 'red', attrs=['bold'])
    cprint("          ")
    cprint("                               VERSION: 1.50", 'white', attrs=['bold']) 
    cprint(f"          MADE BY: linux-fIsHeR, stilling learning Project is not done {x}",'white', attrs=['bold'])  
    print(Ip()) 


print(banner())
