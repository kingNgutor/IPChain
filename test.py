#test pad for ideas and algorithms
#Ngutor Aben @ 00:13 May 11, 2020


#Blockchain integration layer

#_______________________________Import_______________________________#

import multiprocessing as mp


def rice():

    x=1
    y = 0

    while y < 2**64:
        x += x**(2**y)
    

pool = mp.Pool(mp.cpu_count())
results = [pool.apply(rice())]
pool.close()

print("x = ", x)    


    