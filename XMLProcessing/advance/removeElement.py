import xml.etree.ElementTree as ET

tree = ET.parse('CyberShake_100.xml')
root = tree.getroot()

alljobs = tree.findall('{http://pegasus.isi.edu/schema/DAX}job')
print(alljobs[0].attrib['id'])

allchilds = tree.findall('{http://pegasus.isi.edu/schema/DAX}child')
print(allchilds[0].attrib['ref'])

# allparents = tree.findall('//{http://pegasus.isi.edu/schema/DAX}parent')
# print(allparents[0])

#for parent in tree.findall('{http://pegasus.isi.edu/schema/DAX}child'):
#    node = parent.find('{http://pegasus.isi.edu/schema/DAX}parent')
#    print(node.attrib['ref'])


######### Remove node ############
for task in tree.findall('{http://pegasus.isi.edu/schema/DAX}job'):
    if task.attrib['id'] == "ID00000":
        root.remove(task)
    if task.attrib['id'] == "ID00001":
        root.remove(task)
    if task.attrib['id'] == "ID00002":
        root.remove(task)
    if task.attrib['id'] == "ID00003":
        root.remove(task)

for task in tree.findall('{http://pegasus.isi.edu/schema/DAX}child'):
    if task.attrib['ref'] == "ID00000":
        root.remove(task)
    if task.attrib['ref'] == "ID00001":
        root.remove(task)
    if task.attrib['ref'] == "ID00002":
        root.remove(task)
    if task.attrib['ref'] == "ID00003":
        root.remove(task)

for parent in tree.findall('{http://pegasus.isi.edu/schema/DAX}child'):
    if parent.find('{http://pegasus.isi.edu/schema/DAX}parent').attrib['ref'] == "ID00003":
        root.remove(parent)

tree.write("output1.xml", xml_declaration=True, encoding='utf-8', method="xml")

from lxml import etree, objectify
metadata = 'output1.xml'
parser = etree.XMLParser(remove_blank_text=True)
tree = etree.parse(metadata, parser)
root = tree.getroot()

####
for elem in root.getiterator():
    if not hasattr(elem.tag, 'find'): continue  # (1)
    i = elem.tag.find('}')
    if i >= 0:
        elem.tag = elem.tag[i+1:]
objectify.deannotate(root, cleanup_namespaces=True)
####

tree.write('output2.xml', pretty_print=True, xml_declaration=True, encoding='UTF-8')
# # Find the parent element of each "weight" element, using XPATH
# for parent in root.findall('.//weight/..'):
#     # Find each weight element
#     for element in parent.findall('weight'):
#         # Remove the weight element from its parent element
#         parent.remove(element)
#
# print ElementTree.tostring(root)
