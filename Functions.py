import os
from netmiko import ConnectHandler
import json
import getpass
from tqdm import tqdm


#this Function to Connect to Network Devices
def SSH_Connecting(Username,Password,IP,Device_Type):
          device = {'device_type':Device_Type,'username':Username,'password':Password,'ip':IP}
          connect = ConnectHandler(**device)
          return connect
      # Raise this Exception if SSH Username or Password is wrong
      

#=================================================================================
######This Function for Open File and get Devices IP
def get_IPs():
    with open('IPs_IOS.txt') as f:
      IPs_ios = f.readlines()
    with open('IPs_Nexus.txt') as f1:
      IPs_nxos = f1.readlines()
      return IPs_ios, IPs_nxos

#=======================================================================================
########## Function for getting Commands  ##############################################
'''def get_commands():
    with open('D:\Online Courses\DevNets\My_Scripts\SSH\Commands.txt') as f:
      Commands_List = f.readlines()
      return Commands_List'''
#=======================================================================================
####### this is a Function to get Vlans ###############################################
user = input("Please Enter Username: ")
password = getpass.getpass()
def IOSv_Devices(Devices_IPs_ios):
    all_Device=[]
    for i in tqdm(Devices_IPs_ios) :
        ssh_connect = SSH_Connecting(user,password,i.strip(),'cisco_ios')#Connect to Devices
        if ssh_connect :
             #print("Succussfully connected to "+ str(i))
             output=ssh_connect.send_command('show version',use_textfsm=True)
             output1=json.dumps(output,indent=2)
             output2=json.loads(output1)
             all_Device.append(output2[0])
    return all_Device
    #=============================================================================================
    #=============================================================================================
def Nxos_Devices(Devices_IPs_nxos1):
    all_Device1=[]
    for i in tqdm(Devices_IPs_nxos1) :
        ssh_connect = SSH_Connecting(user,password,i.strip(),'cisco_nxos')#Connect to Devices
        if ssh_connect :
             #print("Succussfully connected to "+ str(i))
             output=ssh_connect.send_command('show ip interf brief | json-pretty')
             #print(output)
             #output1=json.dumps(output,indent=2)
             #print(type(output1))
             #output2=json.loads(output1)
             #print(type(output2))
             all_Device1.append(output)
    return all_Device1
'''def Writ_Date_in_File(my_Data,ip):
      file = open('Host {} - {}-config.txt'.format(ip, datetime.now().date()), 'a')
        file.write("-------------------------\n")
        file.write("Host {}".format(ip))
        file.write("\n")
        file.write(my_Data)
        file.close()
  '''