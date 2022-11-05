import subprocess
from time import sleep
import argparse, os, random, sys, requests

parser = argparse.ArgumentParser()
parser.add_argument('--flag', dest='flag', ttype=str)
cmd_query=f"""curl -i -s -k -X PUT -H 'Host: 10.254.0.253:8080' -H 'Accept-Encoding: gzip, deflate' """ \
                            f"""-H 'Accept: /' -H 'Connection: close' -H 'X-Team-Token: e5902a784c4ca765' """ \
                            f"""-H 'Content-Length: 36' -H 'Content-Type: application/json' --data-binary """  \
                            f"""'["{args.flag}"]' 'http://10.254.0.253:8080/flags' """
p = subprocess.Popen(cmd_query, shell=True)