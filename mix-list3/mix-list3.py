#!/usr/bin/env python3
list1 = ['cisco_nxos', 'arista_eos', 'cisco_ios' ]
print(list1)
list1.extend(['juniper']) # this adds juniper to the end of the list
print(list1)
list1.append(['10.1.0.1', '10.2.0.1', '10.3.0.1'])  # This appends a list to the end of a list
print(list1)
print(list1[4])  # This print a list within a list..
print(list1[4][0]) # This prints the first item on the list at the end of the same list
list2 = ['dog', 'cat', 'pig', 'rat', 'cow' ]
print(list2) # This displays all items in list2