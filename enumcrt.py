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

parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-u', action='store',dest='domain',  type=str, required=True)
parser.add_argument('-o', action='store', dest='output',  type=str, required=False)
args = parser.parse_args()
k=1
check=sys.version
if "2.7" not in check:
    print ("Sorry this requires python version 2.7")
    exit()
url1=str(args.domain)
output1=str(args.output)
if(output1!="None"):
    output=output1
    print ("Output:"+output)
    f1 = open(output, "a")
    k=0
url2=url1
temp="";
num=0;
url="https://crt.sh/?q=%25."+url2+"&output=json"
print ("Target:"+url2)
print ("\n")
try:
    f = urllib.urlopen(url)
    values = json.load(f)
    f.close()
    res = [ sub['name_value'] for sub in values ]
    res=list(dict.fromkeys(res))

    try:
        for i in range(0,10000):
            index = i+1
            print(str(index) + ". " + res[i])
            if k==0:
                f1.write(res[i]+"\n")

    except:
        print("Completed")
        print "Domains Found:",i
except:
    print ("Looks like the server is taking too long to respond, This may be due to the huge domain list :) Try %25.yoursite.com")
