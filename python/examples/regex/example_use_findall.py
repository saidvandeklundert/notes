import re

config_data = """
interface 0/47
shutdown
exit

interface 0/48
shutdown          
exit

interface 0/49
description 'some description'
no spanning-tree auto-edge
switchport mode trunk
switchport trunk allowed vlan 123,223-225
exit 

interface 3/23
storm-control broadcast
description 'YOLOCOLO'
no spanning-tree auto-edge
switchport mode trunk
switchport trunk allowed vlan 124
exit 
    """
list_of_interfaces = re.findall("(?s)(^interface.*?exit)", config_data, re.MULTILINE)

print(list_of_interfaces)
