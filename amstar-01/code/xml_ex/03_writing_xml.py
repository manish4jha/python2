import xml.etree.ElementTree as ET

# create the file structure
data = ET.Element('data')

items = ET.SubElement(data, 'items')

item1 = ET.SubElement(items, 'item')
item2 = ET.SubElement(items, 'item')

item1.set('name','item1')
item2.set('name','item2')

item1.text = 'Cherries'
item2.text = 'Figs'

# create a new XML file with the results
xmldata = ET.tostring(data)
xmlfile = open("items2.xml", "w")
xmlfile.write(xmldata.decode())
xmlfile.close()
