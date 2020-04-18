import xml.etree.ElementTree as ET

tree = ET.parse('items.xml')
root = tree.getroot()
data = ['mangoes', 'cherries']
# changing a field text
i = 0
for elem in root.iter('item'):
    elem.text = data[i]
    i += 1


# modifying an attribute
for elem in root.iter('item'):
    elem.set('name', 'newitem')


# adding an attribute
for elem in root.iter('item'):
    elem.set('name2', 'newitem2')


tree.write('newitems.xml')

'''
NOTE:
he names of the item elements have changed to "newitem",
the text to "new text", and the attribute "name2" has been
added to both nodes
'''
