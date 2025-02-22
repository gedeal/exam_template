import subprocess, sys

computer_name = "Gerson"

p=subprocess.Popen(
    ["powershell.exe","ls"])
p.communicate()

p=subprocess.Popen(
    ["powershell.exe","clear"])
p.communicate()

p=subprocess.Popen(
    ["powershell.exe","echo 'TESTING POWERESHELL'"])
p.communicate()

p=subprocess.Popen(
    ["powershell.exe","python -m src.game"])
p.communicate()



    # ["powershell.exe", "Get-ADComputer " + computer_name+ " | Select-Object Name"],stdout=sys.stdout)


