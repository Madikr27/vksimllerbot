from subprocess import Popen, DEVNULL, PIPE, STDOUT
from time import sleep
from os import system
from random import randint

servers = ["185.169.134.3", "185.169.134.4", "185.169.134.43", "185.169.134.44", "185.169.134.45", "185.169.134.5", "185.169.134.59", "185.169.134.61", "185.169.134.107", "185.169.134.109", "185.169.134.166", "185.169.134.171", "185.169.134.172", "185.169.134.173", "185.169.134.174", "80.66.82.191", "80.66.82.190", "80.66.82.188", "80.66.82.168", "80.66.82.159", "80.66.82.200", "80.66.82.144", "80.66.82.132", "80.66.82.128"]

name = str("raksamp" + str(randint(100,999)))

Popen(['tmux', 'new-session', '-d', '-s', name, '-n', 'Bot0', '-d', str('wine "RakSamp Lite.exe" -h',server[0],'-p 7777')])

for i, server in enumerate(servers):
    Popen(['tmux', 'new-window', '-t', str(str(name)+":"+str(i)), '-n', str("Bot"+str(i)), '-d', str('wine "RakSamp Lite.exe" -h',server[0],'-p 7777')])
    print('['+str(i)+']',str(server))
    sleep(1)
print("total",len(servers),"servers")
