# find ./ubuntu/audios/ -iname "*.wav" -mtime -60 -print -delete
import subprocess as sp
from datetime import datetime

globalCwd = "./ubuntu/audios/"

def run(x, cwd=globalCwd):
    print("lomdi")
    print("cd {cwd} && ".format(cwd=cwd)+x)
    return sp.getoutput("cd {cwd} && ".format(cwd=cwd)+x)

def printRun(x, cwd=globalCwd):
    print("bilauta")
    print("cd {cwd} && ".format(cwd=cwd)+x)
    print(sp.getoutput("cd {cwd} && ".format(cwd=cwd)+x))

x = run('find -iname "*wav" -mmin -2880 -print')

now = datetime.now()
[dd, mm, yyyy] = now.strftime("%d/%m/%Y %H:%M:%S").split(' ')[0].split('/')

for i in x.split("\n"):
    # printRun('ls -lh '+i)
    # printRun('echo '+i)
    # print(i)
    # ----------
    # print("echo "+i+" >> deleted-files-"+dd+"-"+mm+"-"+yyyy+".log")
    printRun("echo "+i+" >> deleted-files-"+dd+"-"+mm+"-"+yyyy+".log", ".")
    run("rm "+i)
    print(datetime.now().astimezone().replace(microsecond=0).isoformat())

# printRun("touch deleted-files-"+dd+"-"+mm+"-"+yyyy+".log")
