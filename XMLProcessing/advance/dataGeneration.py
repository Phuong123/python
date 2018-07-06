# Read input file
import xml.etree.ElementTree as ET
import random
import sys

tree = ET.parse('CyberShake_100.xml')
root = tree.getroot()

taskids = ["ID00000", "ID00001", "ID00002", "ID00003", "ID00004"]

n = int(sys.argv[1])
#n = int(n)
for i in range(n):
    if i < 10:
        string = 'ID0000'
        string += str(i)
        print(string)
    else:
        string = 'ID000'
        string += str(i)
        print(string)


#numTask = (random.randint(1,5))
#for index in range(5):

for taskid in taskids:
    for task in tree.findall('{http://pegasus.isi.edu/schema/DAX}job'):
        if task.attrib['id'] == taskid:
            root.remove(task)
    for task in tree.findall('{http://pegasus.isi.edu/schema/DAX}child'):
        if task.attrib['ref'] == taskid:
            root.remove(task)
    for task in tree.findall('{http://pegasus.isi.edu/schema/DAX}child'):
        for element in task.findall('{http://pegasus.isi.edu/schema/DAX}parent'):
            if task.find('{http://pegasus.isi.edu/schema/DAX}parent').attrib['ref'] == taskid:
                task.remove(element)


## Store corresponding input to files
fileName = "output.xml"

## write first version
tree.write(fileName, xml_declaration=True, encoding='utf-8', method="xml")

## Converst to xml file with namespace
from lxml import etree, objectify

parser = etree.XMLParser(remove_blank_text=True)
tree = etree.parse(fileName, parser)
root = tree.getroot()

## Process first version to the right version with namespace
for elem in root.getiterator():
    if not hasattr(elem.tag, 'find'): continue  # (1)
    i = elem.tag.find('}')
    if i >= 0:
        elem.tag = elem.tag[i + 1:]
objectify.deannotate(root, cleanup_namespaces=True)
tree.write(fileName, pretty_print=True, xml_declaration=True, encoding='UTF-8')