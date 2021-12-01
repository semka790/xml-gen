import xml.etree.ElementTree as ET

tree = ET.parse("test.xml")
root = tree.getroot()

for item in root:
    for sub in item:
        print(sub.attrib)
