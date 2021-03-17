###### vlan_ssh.py
import sys
from tqdm import tqdm
from netmiko import ConnectHandler
import getpass
#####################
###### Define Host
host=[]
devno=int(input('How many Device would you connect to: '))
for i in range (devno):
    ip=input('Please Enter ip address of device no.'+str(i))
    host.append(ip)
print('###### Device List #####\n')
print(host)

user=input('Enter user with privilege 15: ')
password=getpass.getpass()
######################
#### Define SSH Session
for i in range(devno):
    print('*'*10 + ' Connected to device: '+str(host[i]) +'*'*10)
    ciscosw={'ip':host[i] ,'username': user , 'password': password , 'device_type':'cisco_ios' }
    connect=ConnectHandler(**ciscosw)
    for n in tqdm(range(100,111)):
        command1='vlan '+ str(n)
        command2='name IT' + str(n)
        commands=[command1 , command2]
        connect.send_config_set(commands)
    print('\n\n' + '*'*10 + ' Vlan on device: '+str(host[i]) +'*'*10 + '\n\n')   
    output=connect.send_command_expect('show vlan')
    print(output)