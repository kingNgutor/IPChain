#Author: Ngutor Aaron Aben
#Datetime: 00:35 February 18, 2022
#Description: initialization script for IPFS Daemon subprocess
#Utility: automation for IPFS connection, a project dependency. IPFS node requied to store and retrieve
# program metadata.
# 

#_______________________________Dependencies_______________________________#

import ipfshttpclient
import os
import subprocess

#________________________________Main Code__________________________________#

print("Establishing connection to IPFS network...")
subprocess.run("/home/cen10ium/code/IPchain/IPFSDaemon.sh")  