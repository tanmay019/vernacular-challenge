import sys
import subprocess as sp
from datetime import datetime

globalCwd = "/home/ubuntu/audios"

if len(sys.argv)>1 and isinstance(sys.argv[1], str):
    globalCwd = sys.argv[1]

def run(x, cwd=globalCwd):
    command="cd {cwd} && ".format(cwd=cwd)+x
    return sp.getoutput(command)

x = run('find -iname "*wav" -mmin -2880 -print')

audioFiles = x.split("\n")
if audioFiles[0] is "":
    print("folder "+globalCwd+" does not contain files older than 48 hours.")
    exit()

print(audioFiles)

[dd, mm, yyyy] = datetime.now().strftime("%d/%m/%Y %H:%M:%S").split(' ')[0].split('/')

for i in audioFiles:
    deletedTime=datetime.now().astimezone().replace(microsecond=0).isoformat()
    deletedFileName="deleted-files-"+dd+"-"+mm+"-"+yyyy+".log"
    createdTime=run("date --iso-8601=seconds -r "+i)
    run("echo "+i+" "+deletedTime+" "+createdTime+" >> "+deletedFileName, ".")
    run("rm "+i)
