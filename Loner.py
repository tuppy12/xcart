import os
import platform
import webbrowser
os.system('termux-setup-storage')
os.system('git pull')
try:os.system('mkdir /sdcard/CHI-DATA')
except:pass
try:os.system('mkdir /sdcard/CHI-DATA/OK')
except:pass
try:os.system('mkdir /sdcard/CHI-DATA/CP')
except:pass
try:os.system('mkdir /sdcard/CHI-DATA/TAP-A2F')
except:pass
try:os.system('touch .prox.txt')
except:pass
P = '\x1b[1;97m'
import os,requests
xr = requests.get("http://ip-api.com/json/").json()
try:
	fc = xr["country"]
except KeyError:
	print('%s\nBAD INTERNET CONNECTION\n'%(P))
	exit()

arc = platform.uname().machine
if 'aarch' in arc:
	from LONER import login
        login()
else:
	exit('machine not support!')
