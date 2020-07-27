import xml.etree.ElementTree as ET


tree =ET.parse(r"C:\Users\abhir\Desktop\WORK_DOM\FORMFC4.xml")
root=tree.getroot()
tag=root.tag
tag=root.tag
print(tag)
#bindma = tree.parse(r"C:\Users\abhir\Desktop\WORK_DOM\FORMFC4.xml")

attr=root.attrib
print(attr)
#for c in root.findall('')
 #    print   i   