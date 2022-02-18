#test pad for ideas and algorithms
#Ngutor Aben @ 00:13 May 11, 2020


#Blockchain integration layer

#_______________________________Dependencies_______________________________#

import ipfshttpclient
import os
import subprocess

#________________________________Main Code__________________________________#

print("Establishing connection to IPFS network...")
subprocess.run("/home/cen10ium/code/IPchain/IPFSDaemon.sh")
print("Opening IPFS Daemon...")

'''
def main():
    # Connect to local node
    try:
        api = ipfshttpclient.connect('127.0.0.1', 5001)
        print(api)
    except ipfshttpclient.exceptions.ConnectionError as ce:
        print(str(ce))



#if __name__ == '__main__':
 #   main()


with ipfshttpclient.connect() as client:
        print(client.version())  # These calls…
        print(client.version())  # …will reuse their TCP connection



'''    