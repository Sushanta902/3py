if __name__ == "__main__":
    plen = int(input('Enter 1 for encrypt and 2 for decrypt\n')) #get the mode
    key = int(input('Enter the key\n')) #get the key
    if plen == 1:
        password = str(input('Enter your password\n'))
        print('Your encrypted password is on key ',key)

        for i in password:            
            print(chr(ord(i)+key),end ="")#convert the string by incrementing with key
            

    elif plen == 2:
        password = str(input('Enter your password\n'))
        print('Your encrypted password is on key ',key)

        for i in password:            
            print(chr(ord(i)-key),end ="")
    else:
        print('Wrong input')        
