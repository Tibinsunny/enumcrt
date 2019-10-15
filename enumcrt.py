print("""\


 /$$$$$$$$ /$$   /$$ /$$   /$$ /$$      /$$  /$$$$$$  /$$$$$$$  /$$$$$$$$
| $$_____/| $$$ | $$| $$  | $$| $$$    /$$$ /$$__  $$| $$__  $$|__  $$__/
| $$      | $$$$| $$| $$  | $$| $$$$  /$$$$| $$  \__/| $$  \ $$   | $$   
| $$$$$   | $$ $$ $$| $$  | $$| $$ $$/$$ $$| $$      | $$$$$$$/   | $$   
| $$__/   | $$  $$$$| $$  | $$| $$  $$$| $$| $$      | $$__  $$   | $$   
| $$      | $$\  $$$| $$  | $$| $$\  $ | $$| $$    $$| $$  \ $$   | $$   
| $$$$$$$$| $$ \  $$|  $$$$$$/| $$ \/  | $$|  $$$$$$/| $$  | $$   | $$   
|________/|__/  \__/ \______/ |__/     |__/ \______/ |__/  |__/   |__/   
                                                                         
                                                        (Beta)      
                                                                         
     #Developed_By:Tibin Sunny #Contact:tibinsunny95@gmail.com
	        Huge Domain list are not supported
                     Feel Free to Report Bugs
 ________________________________________________________________  
   """)                  
                                                            



import urllib, json,argparse,sys
from termcolor import colored
from tld import get_fld
import psycopg2
import re
parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-u', action='store',dest='domain',  type=str, required=True)
parser.add_argument('-o', action='store', dest='output',  type=str, required=False)
args = parser.parse_args()
k=1
url1=str(args.domain)
output1=str(args.output)
if(output1!="None"):
    output=output1
    print ("Output:"+output)
    f1 = open(output, "a")
    k=0  
url2=url1
temp=""
num=0
url="https://crt.sh/?q=%25."+url2+"&output=json"
print ("Target:"+url2)
print ("\n")
try:
    try:
        f = urllib.urlopen(url)
        values = json.load(f)
        f.close()
        res = [ sub['name_value'] for sub in values ]
        res=list(dict.fromkeys(res))
        try:
            for i in range(0,10000):
                print(res[i])
                if k==0:
                    f1.write(res[i]+"\n")
        except:
            print("Domains Found: ",i)
    except:
        print("Error Retriving Data From API")
    try:
        unique_domains = set()
        print(colored("Connecting to crt.sh database","blue"))
        conn = psycopg2.connect("dbname=certwatch user=guest host=crt.sh")
        conn.autocommit =True
        postgres_cursor=conn.cursor()
        postgres_cursor.execute("SELECT ci.NAME_VALUE NAME_VALUE FROM certificate_identity ci WHERE ci.NAME_TYPE = 'dNSName' AND reverse(lower(ci.NAME_VALUE)) LIKE reverse(lower('%{}'));".format(url2))
        for result in postgres_cursor.fetchall():
            matches = re.findall(r"\'(.+?)\'", str(result))
            for subdomain in matches:
                try:
                    if get_fld("https://"+subdomain)==url2:
                        unique_domains.add(subdomain.lower())
                except:pass
        print(sorted(unique_domains))
    except:
        print("Error Pulling Data")
except:
    print("Something Went abolutely wrong....!")
