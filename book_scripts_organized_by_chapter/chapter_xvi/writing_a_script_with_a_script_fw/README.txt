in this exercise, we learn how we can write a python script that writes a script.
the resulting script is a windows .cmd file of netsh commands run sequentially to configure a windows machine's firewall.
in the examples given, inbound rules restrict access to the machine's services from private networks only.
in the first example, netsh commands are created for the entire inbound ruleset.
in the second example, netsh commands are created only for rules whose direction is 'In' and whose rulename includes 'RPC'
