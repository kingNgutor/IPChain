#Ngutor Aben @ 03:56 05-12-2020

#Prototype hashFunc

#_________________________________Imports___________________________________#

import hashlib



#_________________________________Main Code__________________________________#


sourcefile = "/home/ngutor/(java)-eclipse-workspace/IPchain/Navigating [Master].flp"
BLOCKSIZE = 10485760                 #bytes (10 MB)
hasher = hashlib.sha3_512()
with open(sourcefile, 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
print("sourcefile hash output = ",hasher.hexdigest())

hashy = hashlib.sha3_512()
with open("Navigating [Mastered].ogg", 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
        
print("audio hash output = ", hashy.hexdigest())

if hashy != hasher:
    print("The hashes are unidentical")
else:
    print("shit")
