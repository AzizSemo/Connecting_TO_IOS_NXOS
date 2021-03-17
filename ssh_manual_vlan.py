######ssh_manual_vlan
import sys
from tqdm import tqdm
from netmiko import ConnectHandler
import getpass
#####################
###### Define Host
host=[] #for device or switch ip addresses
vlan_id_info=[] #for storing vlan id  
vlan_name_info=[] #for storing vlan names

################ User Data Entry #########################
user=input('Enter user with privilege 15: ')
password=getpass.getpass()
##########################################################


################ Switch Data Entry #######################
devno=int(input('How many Device would you connect to: '))
for i in range (devno):
    ip=input('Please Enter ip address of device no.'+str(i))
    host.append(ip)
print('###### Device List #####\n')
print(host)
###########################################################

################ VLAN Data Entry ##########################
vlan_count = int(input('How many vlans would you create?: '))
for m in range(vlan_count):
    vlan_id=input('Enter Vlan Id - please do not use 1,1002 -1005 : ')
    vlan_name=input('Enter VLAN name: ')
    vlan_id_info.append(vlan_id)
    vlan_name_info.append(vlan_name)
############################################################

######################
#### Define SSH Session and Switch vlan configuration
for i in range(devno): #for device selection
    print('*'*10 + ' Connected to device: '+str(host[i]) +'*'*10)
    ciscosw={'ip':host[i] ,'username': user , 'password': password , 'device_type':'cisco_ios' }
    connect=ConnectHandler(**ciscosw)
    for n in tqdm(range(vlan_count)): #for vlan creation on each switch
        command1='vlan '+ str(vlan_id_info[n])
        command2='name ' + str(vlan_name_info[n])
        commands=[command1 , command2]
        connect.send_config_set(commands)
    print('\n\n' + '*'*10 + ' Vlan on device: '+str(host[i]) +'*'*10 + '\n\n')   
    output=connect.send_command_expect('show vlan')
    print(output)