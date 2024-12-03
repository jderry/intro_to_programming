netsh advfirewall firewall set rule name="Active Directory Domain Controller (RPC-EPMAP)" new remoteip=10.0.0.0/255.0.0.0,172.16.0.0/255.240.0.0,192.168.0.0/255.255.0.0
netsh advfirewall firewall set rule name="Active Directory Domain Controller (RPC)" new remoteip=10.0.0.0/255.0.0.0,172.16.0.0/255.240.0.0,192.168.0.0/255.255.0.0
netsh advfirewall firewall set rule name="File Replication (RPC-EPMAP)" new remoteip=10.0.0.0/255.0.0.0,172.16.0.0/255.240.0.0,192.168.0.0/255.255.0.0
netsh advfirewall firewall set rule name="File Replication (RPC)" new remoteip=10.0.0.0/255.0.0.0,172.16.0.0/255.240.0.0,192.168.0.0/255.255.0.0
netsh advfirewall firewall set rule name="DFS Replication (RPC-EPMAP)" new remoteip=10.0.0.0/255.0.0.0,172.16.0.0/255.240.0.0,192.168.0.0/255.255.0.0
netsh advfirewall firewall set rule name="DFS Replication (RPC-In)" new remoteip=10.0.0.0/255.0.0.0,172.16.0.0/255.240.0.0,192.168.0.0/255.255.0.0
netsh advfirewall firewall set rule name="RPC (TCP, Incoming)" new remoteip=10.0.0.0/255.0.0.0,172.16.0.0/255.240.0.0,192.168.0.0/255.255.0.0
netsh advfirewall firewall set rule name="RPC Endpoint Mapper (TCP, Incoming)" new remoteip=10.0.0.0/255.0.0.0,172.16.0.0/255.240.0.0,192.168.0.0/255.255.0.0
netsh advfirewall firewall set rule name="Distributed Transaction Coordinator (RPC-EPMAP)" new remoteip=10.0.0.0/255.0.0.0,172.16.0.0/255.240.0.0,192.168.0.0/255.255.0.0
netsh advfirewall firewall set rule name="Distributed Transaction Coordinator (RPC)" new remoteip=10.0.0.0/255.0.0.0,172.16.0.0/255.240.0.0,192.168.0.0/255.255.0.0
netsh advfirewall firewall set rule name="Windows Firewall Remote Management (RPC-EPMAP)" new remoteip=10.0.0.0/255.0.0.0,172.16.0.0/255.240.0.0,192.168.0.0/255.255.0.0
netsh advfirewall firewall set rule name="Windows Firewall Remote Management (RPC)" new remoteip=10.0.0.0/255.0.0.0,172.16.0.0/255.240.0.0,192.168.0.0/255.255.0.0
netsh advfirewall firewall set rule name="Remote Service Management (RPC-EPMAP)" new remoteip=10.0.0.0/255.0.0.0,172.16.0.0/255.240.0.0,192.168.0.0/255.255.0.0
netsh advfirewall firewall set rule name="Remote Service Management (RPC)" new remoteip=10.0.0.0/255.0.0.0,172.16.0.0/255.240.0.0,192.168.0.0/255.255.0.0
netsh advfirewall firewall set rule name="File and Printer Sharing (Spooler Service - RPC-EPMAP)" new remoteip=10.0.0.0/255.0.0.0,172.16.0.0/255.240.0.0,192.168.0.0/255.255.0.0
netsh advfirewall firewall set rule name="File and Printer Sharing (Spooler Service - RPC)" new remoteip=10.0.0.0/255.0.0.0,172.16.0.0/255.240.0.0,192.168.0.0/255.255.0.0
netsh advfirewall firewall set rule name="Remote Event Log Management (RPC-EPMAP)" new remoteip=10.0.0.0/255.0.0.0,172.16.0.0/255.240.0.0,192.168.0.0/255.255.0.0
netsh advfirewall firewall set rule name="Remote Event Log Management (RPC)" new remoteip=10.0.0.0/255.0.0.0,172.16.0.0/255.240.0.0,192.168.0.0/255.255.0.0
netsh advfirewall firewall set rule name="Remote Volume Management (RPC-EPMAP)" new remoteip=10.0.0.0/255.0.0.0,172.16.0.0/255.240.0.0,192.168.0.0/255.255.0.0
netsh advfirewall firewall set rule name="Remote Volume Management - Virtual Disk Service Loader (RPC)" new remoteip=10.0.0.0/255.0.0.0,172.16.0.0/255.240.0.0,192.168.0.0/255.255.0.0
netsh advfirewall firewall set rule name="Remote Volume Management - Virtual Disk Service (RPC)" new remoteip=10.0.0.0/255.0.0.0,172.16.0.0/255.240.0.0,192.168.0.0/255.255.0.0
netsh advfirewall firewall set rule name="Remote Scheduled Tasks Management (RPC-EPMAP)" new remoteip=10.0.0.0/255.0.0.0,172.16.0.0/255.240.0.0,192.168.0.0/255.255.0.0
netsh advfirewall firewall set rule name="Remote Scheduled Tasks Management (RPC)" new remoteip=10.0.0.0/255.0.0.0,172.16.0.0/255.240.0.0,192.168.0.0/255.255.0.0
netsh advfirewall firewall set rule name="Netlogon Service Authz (RPC)" new remoteip=10.0.0.0/255.0.0.0,172.16.0.0/255.240.0.0,192.168.0.0/255.255.0.0
netsh advfirewall firewall set rule name="Remote Event Monitor (RPC-EPMAP)" new remoteip=10.0.0.0/255.0.0.0,172.16.0.0/255.240.0.0,192.168.0.0/255.255.0.0
netsh advfirewall firewall set rule name="Remote Event Monitor (RPC)" new remoteip=10.0.0.0/255.0.0.0,172.16.0.0/255.240.0.0,192.168.0.0/255.255.0.0
netsh advfirewall firewall set rule name="Inbound Rule for Remote Shutdown (RPC-EP-In)" new remoteip=10.0.0.0/255.0.0.0,172.16.0.0/255.240.0.0,192.168.0.0/255.255.0.0
netsh advfirewall firewall set rule name="Virtual Machine Monitoring (RPC)" new remoteip=10.0.0.0/255.0.0.0,172.16.0.0/255.240.0.0,192.168.0.0/255.255.0.0
