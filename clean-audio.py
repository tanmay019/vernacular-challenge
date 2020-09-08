import subprocess as sp
from datetime import datetime

globalCwd = "./ubuntu/audios/"

def run(x, cwd=globalCwd):
    command="cd {cwd} && ".format(cwd=cwd)+x
    return sp.getoutput(command)

def printRun(x, cwd=globalCwd):
    command="cd {cwd} && ".format(cwd=cwd)+x
    print(sp.getoutput(command))

x = run('find -iname "*wav" -mmin -2880 -print')

[dd, mm, yyyy] = datetime.now().strftime("%d/%m/%Y %H:%M:%S").split(' ')[0].split('/')

audioFiles = x.split("\n")
if audioFiles[0] is "":
    exit()

for i in audioFiles:
    deletedTime=datetime.now().astimezone().replace(microsecond=0).isoformat()
    deletedFileName="deleted-files-"+dd+"-"+mm+"-"+yyyy+".log"
    createdTime=run("date --iso-8601=seconds -r "+i)
    run("echo "+i+" "+deletedTime+" "+createdTime+" >> "+deletedFileName, ".")
    run("rm "+i)
