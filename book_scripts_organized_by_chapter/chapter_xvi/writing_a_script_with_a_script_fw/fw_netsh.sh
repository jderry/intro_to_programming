
 # on the windows machine, run:
 c:\>netsh advfirewall firewall show rule all > c:\fwrules.txt
 # this outputs a text file with all the firewall rules.

 # on the windows machine, run:
 c:\>netsh advfirewall export c:\firewallpolicy.wfw
 # this creates a file of all the firewall rules as they exist when the file is made

 # if you need to roll back your firewall rules to the earlier state, run:
 c:\>netsh advfirewall firewall import c:\firewallpolicy.wfw
 
 
