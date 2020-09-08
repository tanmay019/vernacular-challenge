import subprocess as sp
from datetime import datetime

globalCwd = "./ubuntu/audios/"

def run(x, cwd=globalCwd):
    command="cd {cwd} && ".format(cwd=cwd)+x
    # print(command)
    return sp.getoutput(command)

def printRun(x, cwd=globalCwd):
    command="cd {cwd} && ".format(cwd=cwd)+x
    # print(command)
    print(sp.getoutput(command))

x = run('find -iname "*wav" -mmin -2880 -print')

now = datetime.now()
[dd, mm, yyyy] = now.strftime("%d/%m/%Y %H:%M:%S").split(' ')[0].split('/')

for i in x.split("\n"):
    # printRun('ls -lh '+i)
    # printRun('echo '+i)
    # print(i)
    # ----------
    deletedTime=datetime.now().astimezone().replace(microsecond=0).isoformat()
    # print("echo "+i+" >> deleted-files-"+dd+"-"+mm+"-"+yyyy+".log")
    deletedFileName="deleted-files-"+dd+"-"+mm+"-"+yyyy+".log"
    createdTime=run("date --iso-8601=seconds -r "+i)
    print(108, createdTime)
    printRun("echo "+i+" "+deletedTime+" "+createdTime+" >> "+deletedFileName, ".")
    run("rm "+i)
    print(deletedTime)

# printRun("touch deleted-files-"+dd+"-"+mm+"-"+yyyy+".log")
