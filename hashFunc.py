#Ngutor Aben @ 03:56 05-12-2020
#Prototype hashFunc
# "/home/cen10ium/code/IPchain/Navigating [Master].flp"

#_________________________________Imports___________________________________#

import hashlib



#_________________________________Main Code__________________________________#



#_______Source File handling_________#

sourcefile = input("Enter source file path here: ")
BLOCKSIZE = 10485760                 #bytes (10 MB)
hasher = hashlib.sha3_512()
with open(sourcefile, 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
print("sourcefile hash output = ",hasher.hexdigest())



#_____________Derivative File handling_______#

userInputAudio = input("enter file path here: ")
hashy = hashlib.sha3_512()
with open(userInputAudio, 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hashy.update(buf)
        buf = afile.read(BLOCKSIZE)
        
print("audio hash output = ", hashy.hexdigest())

if hashy != hasher:
    print("The hashes are unidentical")
else:
    print("shit")
