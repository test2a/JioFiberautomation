# JioFiberautomation
my attempt to update data on JioFiber router page using python selenium. Keep chrome driver in same folder and DO NOT run in sudo. 


## Script 1- Update IPV6 Firewall Rules from script
the file, updateipv6trial.py , takes input from ipv6address.txt in the same folder which can be updated by the following script
````
ifconfig eth0| grep 'inet6' | grep 'global' | awk '{ print $2}'
 
````
In Line 41, i have selected third item from the list of firewall rules. if you have only one, change to yours.


