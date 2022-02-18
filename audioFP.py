#Ngutor Aben @ 03:22 05-12-2020

#Audio fingerprinter prototype

"""Currently the file can fingerprint the song and turn it into a python list of signed int values. In principle, this may be 
enough to identify an individual song, and allows for easy arithmetic operations to be performed for comparison."""




#__________________________________Dependencies_____________________________#

import acoustid
import matplotlib
#matplotlib.use("Agg")
import matplotlib.pyplot as plt
import hashlib as hl
import numpy as np
import chromaprint
#import tkinter



#______________________________________________Main Code______________________________________#

duration, fp_encoded = acoustid.fingerprint_file('IPchain/Navigating [Mastered].ogg')
fingerprint, version = chromaprint.decode_fingerprint(fp_encoded)
print("fingerprint =", fingerprint)
print("fingerprint is a type: ", type(fingerprint))

print("the length of fingerprint is: ", len(fingerprint))


fig = plt.figure()
bitmap = np.transpose(np.array([[b == '1' for b in list('{:32b}'.format(i & 0xffffffff))] for i in fingerprint]))
plt.imshow(bitmap)
plt.plot(bitmap)

print(type(bitmap))
print(bitmap)
