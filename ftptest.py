#!/usr/bin/env python
import ftplib
import pysftp
import time

#with pysftp.Connection('vps10240.dreamhostps.com', username='dh_m958u5', password='password') as sftp:
#    with sftp.cd('mattsmaplesyrup.com/releaser'):
#        sftp.put('testfile.csv')

import paramiko

#set username & password
hostname='vps10240.dreamhostps.com'
username='dh_m958u5'
password='password'
port=22
source= 'testfile.csv' 
destination ='mattsmaplesyrup.com/releaser/testfile.csv'


#SFTP
#client.load_system_host_keys()
t = paramiko.Transport((hostname, port)) 
t.connect(username=username,password=password)
sftp = paramiko.SFTPClient.from_transport(t)
sftp.put(source,destination)
#sftp.close()
#t.close()
