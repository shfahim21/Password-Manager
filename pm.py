#! python3
import pyperclip, os, shelve, sys

def UPDATE():
    print("Enter acName[single]:".center(27, '='))
    acName = input()
    print("Enter Password:".center(27, '='))
    passwords[acName] = input()
    print(("Updated account " + acName).center(27, '='))
    
    passFile = shelve.open('dataa')
    passFile['passwords'] = passwords
    passFile.close()

def COPY(accountCommand):
    if accountCommand in passwords:
        pyperclip.copy(passwords[accountCommand])
        print("Password copied".center(27, '-'))
    else:
        print("Account not found".center(27, '-'))

def HOME():
    print("Enter options:".center(27, '='))
    print("1.Update\n2.Copy Password\n0.Close")
    while True:
        option = input()
        if option == '0':
            sys.exit()
        elif option == '1':
            UPDATE()
            break
        elif option == '2':
            print("Enter accountName:".center(27, '='))
            acName = input()
            COPY(acName)
            break
        else:
            print("Invalid option, try again.".center(27, '-'))
    sys.exit()

passwords = {'test': '1234'}
passFile = shelve.open('dataa')

if 'passwords' in passFile:
    passwords = passFile['passwords']
else:
    print("File Error!!".center(27,'X'))
    input()
    sys.exit()


if len(sys.argv) != 2:
    HOME()
    

accountCommand = sys.argv[1]

if accountCommand in passwords:
    pyperclip.copy(passwords[accountCommand])
    print("Password copied".center(27, '-'))
elif accountCommand == 'update':
    UPDATE()
else:
    print("Command not recognized".center(27, '-'))

passFile.close()
