#!/bin/bash
#echo Boobies!!
#password="your password"
#username="dh_m958u5"
#Ip="vps10240.dreamhostps.com"
#sshpass -p "$password" scp scptest.txt $username@$Ip:scptest.txt>

# connect via scp
spawn scp "dh_m958u5@vps10240.dreamhostps.com:scptest.txt" scptest.txt
#######################
expect {
  -re ".*es.*o.*" {
    exp_send "yes\r"
    exp_continue
  }
  -re ".*sword.*" {
    exp_send "PASSWORD\r"
  }
}
interact
