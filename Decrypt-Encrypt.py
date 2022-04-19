#This program will Decypt and Encrypt your message.

import random
import time

print("")
print("Welcome to the Decrypt and Encrytion application.")
time.sleep(1)
print("")

decryptORencrypt = input("Do you want to decrypt or encrypt a message? (D / E): ")
if decryptORencrypt == "D":
    for i in range(1):
      keygen = (random.randint(11111111111, 999999999999999))
    print ("")
    message=input ('Enter message you want to decrypt: ')
    wholeAlphabet="abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{}|:<>?=-[]\;',./`~ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    firstkey = input("Encryption Key: ")
    encrypt =''
    for i in message:
      position=wholeAlphabet.find(i)
      newposition=(position+ -int(firstkey) )%94
      encrypt+=wholeAlphabet [newposition]
    firstoutput = (encrypt)
    keyout = (keygen)
    print("")
    print("Decrypting...")
    time.sleep(1)
    print ('Your Decryptet message is: '+ (firstoutput) )

    print("")
    encryptAfterDecrypt = input("Do you want to encrypt another message? (YES / SAMEMESSAGE / NO): ")
    if encryptAfterDecrypt == "YES":
        print("")
        message=input ('Enter message you want to encrypt : ')
        wholeAlphabet="abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{}|:<>?=-[]\;',./`~ABCDEFGHIJKLMNOPQRSTUVWXYZ "
        thekey = input("Enter a encrypt key of your Choice (Recommendet is a number larger then 8): ")
        encrypt =''
        for i in message:
          position=wholeAlphabet.find(i)
          newposition=(position+ int(thekey) )%94
          encrypt+=wholeAlphabet [newposition]
        output = (encrypt)
        print("Encrypting...")
        time.sleep(1)
        print ('Encrypted Message: '+ (output) )
        print ('The Encryption Key you used: '+ (thekey) )

    print("")
    if encryptAfterDecrypt == "SAMEMESSAGE":
        wholeAlphabet="abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{}|:<>?=-[]\;',./`~ABCDEFGHIJKLMNOPQRSTUVWXYZ "

        encrypt =''
        for i in firstoutput:
          position=wholeAlphabet.find(i)
          newposition=(position+ int(firstkey) )%94
          encrypt+=wholeAlphabet [newposition]
        output = (encrypt)
        print("Encrypting the last message...")
        print("")
        time.sleep(1)
        print("The decryption key you used was: ", firstkey)
        print ('Your message: '+ (output) )


    else:
        quit()

print("")
if decryptORencrypt == "E":
    message=input ('Enter message you want to encrypt: ')
    wholeAlphabet="abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{}|:<>?=-[]\;',./`~ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    secondkey = input("Enter a encrypt key of your Choice (Recommendet is a number larger then 8): ")
    encrypt =''
    for i in message:
      position=wholeAlphabet.find(i)
      newposition=(position+ int(secondkey) )%94
      encrypt+=wholeAlphabet [newposition]
    output = (encrypt)
    print("Encrypting...")
    time.sleep(1)
    print ('Encrypted Message: '+ (output) )
    print ('The Encryption Key you used: '+ (secondkey) )
