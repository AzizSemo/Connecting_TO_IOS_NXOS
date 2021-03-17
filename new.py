## Connect to Legacy IOS
## Get Structured Data from them "json format"
#### Script Created by
#Eng.Mohammed Ezzat
#ONELAB Training
##################################
########### CCNA 200-301 #########

###Notice
##git clone https://github.com/networktocode/ntc-templates/
#export NET_TEXTFSM='/home/onelabad/myprog/ntc-templates/templates'
#echo $NET_TEXTFSM
#### Import Section ##############
import os
from netmiko import ConnectHandler
import json
import Functions
import getpass
from tqdm import tqdm
##################################
#  ciscosw={'ip':host[i] ,'username': user , 'password': password , 'device_type':'cisco_ios' }
    #connect=ConnectHandler(**ciscosw
##################################
######### Connectivity

Devices_IPs_ios,Devices_IPs_nxos = Functions.get_IPs()
all_Device_IOSv=Functions.IOSv_Devices(Devices_IPs_ios)
all_Device_nxos=Functions.Nxos_Devices(Devices_IPs_nxos)
print(all_Device_IOSv)
print(all_Device_nxos)

             #for y in x:
             #print(str(output3["firstName"]) +"\t\t"+ str(output3["jobTitle"])+"\t\t"+ str(output3["emailAddress"]) )
#print(all_Device)
#index = 0
#print("Name\t  OS \t\t SN")
#print("====\t ===== \t\t ======")
#for y in all_Device_IOSv:
    #for y in x:
       #y= json.loads(x)
       #print(str(y["hostname"]) +"\t"+ str(y["hardware"])+"\t"+ str(y["serial"]) )
       #print(type(x))
#for x in all_Device_nxos:
    #print(x)
    #y1= json.loads(x)
    #print(type(x))
       #print(str(y1["host_name"]) +"\t"+ str(y1["chassis_id"])+"\t"+ str(y1["proc_board_id"]) )
