# parsing XML with namespaces
import xml.etree.ElementTree as ET

tree = ET.parse('CyberShake_100.xml')
root = tree.getroot()

print(root)
#print(root.tag, root.attrib)
alljobs = tree.findall('{http://pegasus.isi.edu/schema/DAX}job')

print(len(alljobs))
print(alljobs[0].attrib['id'])

#print("Traversing child")
#for child in root:
#    print(child.tag, child.attrib)

# Remove elements
for task in tree.findall('{http://pegasus.isi.edu/schema/DAX}job'):
     #print(task.attrib['id'])
     if task.attrib['id'] == "ID00000":
         root.remove(task)
     if task.attrib['id'] == "ID00001":
         root.remove(task)
     if task.attrib['id'] == "ID00002":
         root.remove(task)
     if task.attrib['id'] == "ID00003":
         root.remove(task)


#for node in tree.findall('//{http://pegasus.isi.edu/schema/DAX}parent'):
     # print(node.attrib['ref'])
for node in root.iter('child'):
    print(node.attrib)
    if node.attrib['ref'] == "ID00002":
        root.remove(node)
    if node.attrib['ref'] == "ID00003":
        root.remove(node)

for parent in root.iter('parent'):
    if parent.attrib['ref'] == "ID00003":
        root.remove(parent)

tree.write("output2.xml",
           xml_declaration=True,encoding='utf-8',
           method="xml")

from lxml import etree, objectify

metadata = 'output2.xml'
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

tree.write('output3.xml',
           pretty_print=True, xml_declaration=True, encoding='UTF-8')


####
for node in root.iter('child'):
    print(node.attrib)

for parent in root.iter('parent'):
    print(parent.attrib['ref'])

print("Traversing job")
# Find interesting elements


# for actor in root.findall('{http://pegasus.isi.edu/schema/DAX}job'):
#     name = actor.find('{http://pegasus.isi.edu/schema/DAX}name')
#     print(name.attr)

