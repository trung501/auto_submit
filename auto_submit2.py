import subprocess
from time import sleep
    
while True:   
    try:
        p = subprocess.Popen("python3 pwn2.py", shell=True)
        sleep(60)  
    except:
        print("error get flag")
        sleep(30)  
   
    with open("pwn2.txt","r") as f:
        lines=f.readlines()
        for line in lines:
            line=line.replace('\n','').strip()
            try:
                if len(line)>0 :
                    cmd_query=f"""curl -i -s -k -X PUT -H 'Host: 10.254.0.253:8080' -H 'Accept-Encoding: gzip, deflate' """ \
                            f"""-H 'Accept: /' -H 'Connection: close' -H 'X-Team-Token: e5902a784c4ca765' """ \
                            f"""-H 'Content-Length: 36' -H 'Content-Type: application/json' --data-binary """  \
                            f"""'["{line}"]' 'http://10.254.0.253:8080/flags' """
                    print(cmd_query)
                    p = subprocess.Popen(cmd_query, shell=True)
                    sleep(5)

            except:
                print("error curl")
                sleep(5) 
    sleep(120)