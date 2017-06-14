
import subprocess

f = open("hostlist", 'r', encoding='utf-8')

for cnt, list in enumerate(f):
    cnt = subprocess.getoutput("bash ./getIPaddress.sh {}".format(list))
    print(cnt)

f.close()
